import pytest
import logging
from actions.pets import Pets as PetActions
from testdata.datafactory.pet_factory import PetModel, Model
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema, validate_response_body_as_json
from dataclasses import asdict, astuple
from typing import List


@pytest.mark.pet
def test_get_pet_by_valid_status():
    pet_list = [PetModel() for _ in range(10)]
    pet_actions = PetActions()
    response_list = []

    for pet in pet_list:
        resp = pet_actions.create_pet(pet)
        response_list.append(resp)
        logging.info('Validating STATUS_CODE is OK')
        assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    # for pet in pet_list:
    #     logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({pet.id})')
    #     resp = pet_actions.get_pet(pet.id)
    #     logging.info('Validating STATUS_CODE is OK')
    #     assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    #     logging.info('Validating Response SCHEMA')
    #     assert validate_schema(resp, PetModel), 'Response schema is incorrect'
    #     logging.info(f'Validating Response BODY')
    #     assert validate_response_body(resp, pet), f'expected: {resp.json()} \n actual: {asdict(pet)}'

    status_available_pets = list(filter(lambda x: x.status == 'available', pet_list))
    status_pending_pets = list(filter(lambda x: x.status == 'pending', pet_list))
    status_sold_pets = list(filter(lambda x: x.status == 'sold', pet_list))

    # status=sold
    resp = pet_actions.get_pets_by_status(status='sold')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    list_response = []
    for item in resp.json():
        try:
            obj = Model.parse(item, PetModel)
            list_response.append(obj)
        except:
            pass

    for sold_pet in status_sold_pets:
        assert sold_pet in list_response, f'Pet with id {sold_pet.id} is not present in the response'

    # status=available
    resp = pet_actions.get_pets_by_status(status='available')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    list_response = []
    for item in resp.json():
        try:
            obj = Model.parse(item, PetModel)
            list_response.append(obj)
        except:
            pass

    for sold_pet in status_available_pets:
        assert sold_pet in list_response, f'Pet with id {sold_pet.id} is not present in the response'

    # status=pending
    resp = pet_actions.get_pets_by_status(status='pending')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    list_response = []
    for item in resp.json():
        try:
            obj = Model.parse(item, PetModel)
            list_response.append(obj)
        except:
            pass

    for sold_pet in status_pending_pets:
        assert sold_pet in list_response, f'Pet with id {sold_pet.id} is not present in the response'


@pytest.mark.pet
def test_get_pet_by_invalid_status():

    logging.info(f'Executing\t{__name__}')

    pet_actions = PetActions()
    resp = pet_actions.get_pets_by_status(status='invalid_3455746353dfghfgdsf')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    assert validate_response_body_as_json(resp.json(), []), ''
