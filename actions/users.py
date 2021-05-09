from lib.api.rest_client import Method, execute_rest_api
from dataclasses import asdict
from lib.api import build_url, Headers
from requests import Response
from testdata.datafactory.user_factory import UserModel
from typing import List
import logging


class Endpoints:
    CREATE_USER_WITH_ARRAY = 'user/createWithArray'
    CREATE_USER = '/user'
    UPDATE_USER = 'user/{username}'
    GET_USER = 'user/{username}'


class Users(Headers):

    def create_user(self, user: UserModel) -> Response:
        """ Executes POST API call to create 1 user
        :param user: User data model
        :return:
        """
        logging.info('Creating User')
        json_body = asdict(user)
        url = build_url(Endpoints.CREATE_USER)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def create_users(self, users: List[UserModel]) -> Response:
        """ Executes POST API call to create multiple users with array / list
        :param users: list of User models
        :return:
        """
        logging.info('Creating multiple Users')
        json_body = []
        for u in users:
            json_body.append(asdict(u))

        url = build_url(Endpoints.CREATE_USER_WITH_ARRAY)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def get_user(self, username: str) -> Response:
        """ Executes GET API call for getting User details using username
        :param username:
        :return:
        """
        logging.info(f'Getting User details for username {username}')
        url = build_url(Endpoints.GET_USER.replace('{username}', username))
        response = execute_rest_api(Method.GET, url, headers=self.request_headers)
        return response

    def update_user(self, username: str, data: UserModel) -> Response:
        """ Executes PUT API call to update User details using username
        :param username: string username
        :param data: New user data model
        :return:
        """
        logging.info(f'Updating User details for username {username}')
        json_body = asdict(data)
        url = build_url(Endpoints.UPDATE_USER.replace('{username}', username))
        response = execute_rest_api(Method.PUT, url, json_body=json_body, headers=self.request_headers)
        return response
