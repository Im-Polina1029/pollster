from django.shortcuts import render
import json
from databases.mysql_db import client_mysqldb
from PoW.generate_random_string import generate_random_string
from django.http import JsonResponse, HttpResponseForbidden
import datetime


def request_on_sign_in_page(requests):
    response = render(requests, 'sign_in_page.html')
    cookie = generate_random_string(10)

    client_mysqldb.create_cookie_into_pow_table(cookie)
    response.set_cookie('auth_sessionid', cookie)

    return response


def request_on_sign_in_account(request):
    try:
        json_data = json.loads(request.body)

        login = json_data.get('login')
        password = json_data.get('password')

        assert 'auth_sessionid' in request.COOKIES

        cookie = request.COOKIES['auth_sessionid']

        pow = json_data.get('pow', '')
        pow_from_db = client_mysqldb.get_pow(cookie)

        if pow == '' or pow != pow_from_db:
            return HttpResponseForbidden(403)

        password_from_db, id_of_user = client_mysqldb.get_user_password_and_id_of_user_from_table(login)
        assert password == password_from_db
        assert password_from_db is not None

        expired = datetime.datetime.now()
        expired = expired + datetime.timedelta(days=3)

        if client_mysqldb.check_availability_entry_in_sessions(id_of_user):
            client_mysqldb.update_cookie_in_session_table(cookie, id_of_user, 'auth_sessionid', expired)
        else:
            client_mysqldb.create_entry_into_sessions_table(cookie, 'auth_sessionid', id_of_user)

        return JsonResponse({'response': 'ok'})
    except AssertionError:
        return JsonResponse({'response': 'Неправильный пароль или почта'})