import pytest
import logging
from actions.pets import Pets as PetActions
from testdata.datafactory.pet_factory import PetModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from dataclasses import asdict


@pytest.mark.pet
def test_update_pet():

    pet1 = PetModel()
    pet_actions = PetActions()
    resp = pet_actions.create_pet(pet1)

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    updated_pet1_details = PetModel()
    # Update pet details based on Id hence assigning old id to newly created data
    updated_pet1_details.id = pet1.id
    response = pet_actions.update_pet(updated_pet1_details)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {response.status_code}'
    logging.info('Validating Response SCHEMA for update_pet()')
    assert validate_schema(response, PetModel), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for update_pet()')
    assert validate_response_body(response, updated_pet1_details), f'expected: {response.json()} \n ' \
                                                                   f'actual: {asdict(updated_pet1_details)}'
    logging.info(f'Pet with id {pet1.id} updated successfully.')

    response = pet_actions.get_pet(updated_pet1_details.id)
    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({updated_pet1_details.id})')
    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(response, PetModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(response, updated_pet1_details), f'expected: {response.json()} \n ' \
                                                                   f'actual: {asdict(updated_pet1_details)}'

    logging.info(f'Pet with id {pet1.id} was updated and validated successfully.')

