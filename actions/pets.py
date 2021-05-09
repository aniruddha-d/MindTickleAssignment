from lib.api.rest_client import Method, execute_rest_api
from dataclasses import asdict
from lib.api import build_url, Headers
from requests import Response
from typing import List
import logging
from lib.api import Headers


class Endpoints:
    CREATE_PET = '/pet'
    UPDATE_PET = 'pet'
    GET_PET = 'pet/{id}'
    FIND_BY_STATUS = 'pet/findByStatus?status={status}'


class Pets(Headers):

    def create_pet(self, pet) -> Response:
        json_body = asdict(pet)
        url = build_url(Endpoints.CREATE_PET)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def create_pets(self, pets) -> List[Response]:
        responses = []
        for pet in pets:
            url = build_url(Endpoints.CREATE_PET)
            response = execute_rest_api(Method.POST, url, json_body=asdict(pet), headers=self.request_headers)
            responses.append(response)
        return responses

    def get_pet(self, pet_id: int) -> Response:
        url = build_url(Endpoints.GET_PET.replace('{id}', str(pet_id)))
        response = execute_rest_api(Method.GET, url, headers=self.request_headers)
        return response

    def update_pet(self, username, data) -> Response:
        pass

    def get_pets_by_status(self, status) -> Response:
        url = build_url(Endpoints.FIND_BY_STATUS.replace('{status}', status))
        response = execute_rest_api(Method.GET, url, headers=self.request_headers)
        return response
