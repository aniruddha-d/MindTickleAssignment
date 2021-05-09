from lib.api.rest_client import Method, execute_rest_api
from dataclasses import asdict
from lib.api import build_url
from requests import Response
from lib.api import Headers


class Endpoints:
    CREATE_USER_WITH_ARRAY = 'user/createWithArray'
    CREATE_USER = '/user'
    UPDATE_USER = 'user/{username}'
    GET_USER = 'user/{username}'


class Users(Headers):

    def create_user(self, user) -> Response:
        json_body = asdict(user)
        url = build_url(Endpoints.CREATE_USER)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def create_users(self, users) -> Response:
        json_body = []
        for u in users:
            json_body.append(asdict(u))

        url = build_url(Endpoints.CREATE_USER_WITH_ARRAY)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def get_user(self, username: str) -> Response:
        url = build_url(Endpoints.GET_USER.replace('{username}', username))
        response = execute_rest_api(Method.GET, url, headers=self.request_headers)
        return response

    def update_user(self, username, data) -> Response:
        pass
