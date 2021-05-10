from actions.users import Users as UserActions
from testdata.datafactory.user_factory import UserModel, Model
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from dataclasses import asdict
from utilities.randomizer import Randomize
from testdata.responsemodels.user_response_model import SuccessResponse
import pytest
import logging
import random


@pytest.mark.user
def test_create_multiple_users_edit_details_and_get_user_by_username():
    user_list = [UserModel() for _ in range(5)]

    user_actions = UserActions()
    resp = user_actions.create_users(user_list)

    success = SuccessResponse(200, 'unknown', 'ok')

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'
    logging.info('Validating Response SCHEMA for create_users()')
    assert validate_schema(resp, SuccessResponse), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for create_users()')
    assert validate_response_body(resp, success), f'expected: {resp.json()} \n actual: {asdict(success)}'
    logging.info(f'{len(user_list)} users created successfully.')

    for user in user_list:
        logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for {user.username}')
        response = user_actions.get_user(user.username)

        logging.info('Validating STATUS_CODE is OK')
        assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

        logging.info(f'Validating Response SCHEMA')
        assert validate_schema(response, UserModel), 'Response schema is incorrect'

        logging.info(f'Validating Response BODY')
        assert validate_response_body(response, user), f'expected: {response.json()} \n actual: {asdict(user)}'

        logging.info(f'{user.username} was created and validated successfully.')
    
    logging.info('All Users are created successfully.')

    chosen_user:UserModel = random.choice(user_list)
    chosen_user.firstName = 'updated_' + chosen_user.firstName
    chosen_user.lastName = 'updated_' +chosen_user.lastName
    chosen_user.email = 'updated_' + chosen_user.email
    chosen_user.password = 'updated_' + chosen_user.password
    chosen_user.phone += '1234567890'
    chosen_user.userStatus += 10

    update_success_response = SuccessResponse(message=str(chosen_user.id))
    response = user_actions.update_user(chosen_user.username, chosen_user)
    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {response.status_code}'
    logging.info('Validating Response SCHEMA for update_user()')
    assert validate_schema(response, type(update_success_response)), 'Response schema is incorrect'
    logging.info(f'Validating Response BODY for update_user()')
    assert validate_response_body(response, update_success_response), f'expected: {response.json()} \n ' \
                                                                   f'actual: {asdict(update_success_response)}'
    logging.info(f'User with username {chosen_user.username} updated successfully.')

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_user({chosen_user.username})')
    response = user_actions.get_user(chosen_user.username)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(response, UserModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(response, chosen_user), f'expected: {response.json()} \n ' \
                                                                    f'actual: {asdict(chosen_user)}'

    logging.info(f'User with username {chosen_user.username} was updated and validated successfully.')

