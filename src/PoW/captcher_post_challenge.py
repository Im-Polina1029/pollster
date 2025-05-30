from PoW.engine_of_PoW import EnginePoW
from django.http import JsonResponse, HttpResponseForbidden
from databases.mysql_db import client_mysqldb


def request_on_challenge(requests):
    try:
        assert 'auth_sessionid' in requests.COOKIES
        cookie = requests.COOKIES['auth_sessionid']
        engine_of_pow = EnginePoW()

        client_mysqldb.update_pow_in_pow_table(cookie, engine_of_pow.hash_cash_algorithm())

        return JsonResponse(engine_of_pow.__dict__)
    except AssertionError:
        return HttpResponseForbidden()