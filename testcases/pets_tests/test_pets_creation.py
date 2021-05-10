import pytest
import logging
from actions.pets import Pets as PetActions
from testdata.datafactory.pet_factory import PetModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from testdata.responsemodels.pet_response_model import PetNotFoundResponse
from dataclasses import asdict


@pytest.mark.pet
def test_create_single_pet():
    pet1 = PetModel()
    pet_actions = PetActions()
    resp = pet_actions.create_pet(pet1)

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for {pet1.id}')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info('Validating Response SCHEMA for create_pet()')
    assert validate_schema(resp, PetModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY for create_pet()')
    assert validate_response_body(resp, pet1), f'expected: {resp.json()} \n actual: {asdict(pet1)}'

    resp = pet_actions.get_pet(pet1.id)
    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({pet1.id})')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info('Validating Response SCHEMA for get_pet()')
    assert validate_schema(resp, PetModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY for get_pet()')
    assert validate_response_body(resp, pet1), f'expected: {resp.json()} \n actual: {asdict(pet1)}'
    logging.info(f'Pet with id {pet1.id} created successfully.')


@pytest.mark.pet
def test_create_single_pet_using_put():
    pet1 = PetModel()
    pet_actions = PetActions()

    resp = pet_actions.get_pet(pet1.id)

    pnf = PetNotFoundResponse()

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({pet1.id})')
    logging.info('Validating STATUS_CODE is NOT_FOUND')
    assert resp.status_code == HTTPStatus.NOT_FOUND, f'Response is - {resp.status_code}'
    logging.info(f'Validating Response SCHEMA for get_pet({pet1.id})')
    assert validate_schema(resp, type(pnf)), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for get_pet({pet1.id})')
    assert validate_response_body(resp, pnf), f'expected: {resp.json()} \n actual: {asdict(pnf)}'
    logging.info(f'Pet with id {pet1.id} is not found.')

    # create a pet1 with put method
    resp = pet_actions.update_pet(pet1)
    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for update_pet()')

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    logging.info(f'Validating Response SCHEMA for update_pet()')
    assert validate_schema(resp, type(pet1)), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for get_pet()')
    assert validate_response_body(resp, pet1), f'expected: {resp.json()} \n actual: {asdict(pet1)}'

    # Validate details of the pet created with PUT method
    resp = pet_actions.get_pet(pet1.id)
    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({pet1.id})')
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    logging.info('Validating Response SCHEMA for get_pet()')
    assert validate_schema(resp, PetModel), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for get_pet()')
    assert validate_response_body(resp, pet1), f'expected: {resp.json()} \n actual: {asdict(pet1)}'

    logging.info(f'Pet with id {pet1.id} created successfully.')


@pytest.mark.pet
def test_create_multiple_pets():
    pet_list = [PetModel() for _ in range(10)]
    pet_actions = PetActions()
    response_list = []

    for pet in pet_list:
        resp = pet_actions.create_pet(pet)
        response_list.append(resp)
        logging.info('Validating STATUS_CODE is OK')
        assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    for i in range(len(pet_list)):
        pet = pet_list[i]
        resp = response_list[i]
        logging.info(f'Validating SCHEMA and RESPONSE BODY for create_pet({pet.id})')
        logging.info('Validating Response SCHEMA')
        assert validate_schema(resp, PetModel), 'Response schema is incorrect'
        logging.info(f'Validating Response BODY ')
        assert validate_response_body(resp, pet), f'expected: {resp.json()} \n actual: {asdict(pet)}'

    # Validate details of all the newly created pets
    for pet in pet_list:
        logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_pet({pet.id})')
        resp = pet_actions.get_pet(pet.id)
        logging.info('Validating STATUS_CODE is OK')
        assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
        logging.info('Validating Response SCHEMA')
        assert validate_schema(resp, PetModel), 'Response schema is incorrect'
        logging.info(f'Validating Response BODY')
        assert validate_response_body(resp, pet), f'expected: {resp.json()} \n actual: {asdict(pet)}'

    logging.info('All Pets are created successfully.')


