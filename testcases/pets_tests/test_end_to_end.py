
from actions.pets import Pets as PetActions
from testdata.datafactory.pet_factory import PetModel, Model
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from dataclasses import asdict
from utilities.randomizer import Randomize
import pytest
import logging
import random


@pytest.mark.pet
def test_create_multiple_pets_edit_status_and_find_by_edited_status():
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

    chosen_pet:PetModel = random.choice(pet_list)
    chosen_pet.status = 'updated_' + chosen_pet.status
    chosen_pet.name = 'updated_' + chosen_pet.name
    chosen_pet.photoUrls.extend(Randomize().random_urls(2))

    response = pet_actions.update_pet(chosen_pet)
    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {response.status_code}'
    logging.info('Validating Response SCHEMA for update_pet()')
    assert validate_schema(response, PetModel), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for update_pet()')
    assert validate_response_body(response, chosen_pet), f'expected: {response.json()} \n ' \
                                                                   f'actual: {asdict(chosen_pet)}'
    logging.info(f'Pet with id {chosen_pet.id} updated successfully.')

    resp = pet_actions.get_pets_by_status(status=chosen_pet.status)
    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    list_response = []
    for item in resp.json():
        try:
            obj = Model.parse(item, PetModel)
            list_response.append(obj)
        except:
            pass

    assert chosen_pet in list_response, f'Pet with id {chosen_pet.id} is not present in the response'
    logging.info(f'Pet with id {chosen_pet.id} and status {chosen_pet.status} is found using findByStatus()')
