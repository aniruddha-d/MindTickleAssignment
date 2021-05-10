from lib.api.rest_client import Method, execute_rest_api
from dataclasses import asdict
from lib.api import build_url, Headers
from requests import Response
from typing import List
from testdata.datafactory.pet_factory import PetModel
import logging


class Endpoints:
    CREATE_PET = '/pet'
    UPDATE_PET = 'pet'
    GET_PET = 'pet/{id}'
    FIND_BY_STATUS = 'pet/findByStatus'


class Pets(Headers):

    def create_pet(self, pet: PetModel) -> Response:
        """ Executes POST API call to create 1 pet
        :param pet: Pet data model
        :return:
        """
        logging.info('Creating Pet')
        json_body = asdict(pet)
        url = build_url(Endpoints.CREATE_PET)
        response = execute_rest_api(Method.POST, url, json_body=json_body, headers=self.request_headers)
        return response

    def create_pets(self, pets: List[PetModel]) -> List[Response]:
        """ Executes create_pet() for multiple pets
        :param pets: list of Pet models
        :return:
        """
        logging.info('Creating multiple Pets')
        responses = []
        for pet in pets:
            response = self.create_pet(pet)
            responses.append(response)
        return responses

    def get_pet(self, pet_id: int) -> Response:
        """ Executes GET API call for getting Pet details using pet id
        :param pet_id: int pet id
        :return:
        """
        logging.info(f'Getting Pets details for id {pet_id}')
        url = build_url(Endpoints.GET_PET.replace('{id}', str(pet_id)))
        response = execute_rest_api(Method.GET, url, headers=self.request_headers)
        return response

    def update_pet(self, pet: PetModel) -> Response:
        """ Executes PUT API call for updating Pet. If Pet is not found by pet id new pet is created
        :param pet: pet model
        :return:
        """
        logging.info(f'Updating Pet details for pet id {pet.id}')
        json_body = asdict(pet)
        url = build_url(Endpoints.UPDATE_PET)
        response = execute_rest_api(Method.PUT, url, json_body=json_body, headers=self.request_headers)
        return response

    def get_pets_by_status(self, **status) -> Response:
        """ Executes GET API call for getting list of details of all Pet using with given status
        :param status: status of a Pet
        :return:
        """
        logging.info(f'Getting all Pets with status {status}')
        url = build_url(Endpoints.FIND_BY_STATUS)
        response = execute_rest_api(Method.GET, url, headers=self.request_headers, query_params=status)
        return response
