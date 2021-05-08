from lib.api.rest_client import Method, execute_rest_api
from dataclasses import asdict
from lib.api import build_url


class Endpoints:
    CREATE_USER_WITH_ARRAY = 'user/createWithArray'
    CREATE_USER = '/user'
    UPDATE_USER = 'user/{username}'
    GET_USER = 'user/{username}'


class Users:

    def create_user(self, user):
        json_body = asdict(user)
        url = build_url(Endpoints.CREATE_USER)
        response = execute_rest_api(Method.POST, url, json_body=json_body)
        return response

    def create_users(self, users):
        json_body = []
        for u in users:
            json_body.append(asdict(u))

        url = build_url(Endpoints.CREATE_USER_WITH_ARRAY)
        response = execute_rest_api(Method.POST, url, json_body=json_body)
        return response


    def get_user(self, username: str):
        pass

    def update_user(self, username, data):
        pass
