from django.shortcuts import render
import json
from PoW.generate_random_string import generate_random_string
from databases.mysql_db import client_mysqldb
from Configs.Exceptions import ErrorSameLogins, NotFoundCookieIntoPowTable
from django.http import JsonResponse

# from Tools_for_rabbitmq.producer import producer
# from Configs.Commands_For_RMQ import Commands
# from Configs.Responses_from_consumer import Responses


def request_on_create_new_account_page(requests):
    response = render(requests, 'create_new_account_page.html')
    cookie = generate_random_string(10)

    client_mysqldb.create_cookie_into_pow_table(cookie)
    response.set_cookie('auth_sessionid', cookie)
    return response


def request_on_create_new_account(request):
    try:
        json_data = json.loads(request.body)
        login = json_data.get('login')
        password = json_data.get('password')
        pow = json_data.get('pow', '')
        nickname = json_data.get('nickname', '')

        assert pow != ''
        assert 'auth_sessionid' in request.COOKIES

        cookie = request.COOKIES['auth_sessionid']

        pow_from_db = client_mysqldb.get_pow(cookie)

        assert pow == pow_from_db

        client_mysqldb.create_user(login, password, 1, nickname)
        client_mysqldb.delete_pow_entry_from_pow_table(cookie)

        _, id_of_user = client_mysqldb.get_user_password_and_id_of_user_from_table(login)
        client_mysqldb.create_entry_into_sessions_table(cookie, 'auth_sessionid', id_of_user)

        return JsonResponse({'response': 200})
    except AssertionError:
        return JsonResponse({'response': 1, 'message': 'Не найдено значение pow в запросе либо не найден куки файл.'})
    except ErrorSameLogins:
        return JsonResponse({'response': 2, 'message': 'Данный логин уже занят.'})
    except NotFoundCookieIntoPowTable:
        return JsonResponse({'response': 3, 'message': 'Повторите попытку'})