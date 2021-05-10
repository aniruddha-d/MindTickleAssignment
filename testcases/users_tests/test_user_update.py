import pytest
import logging
from actions.users import Users as UserActions
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from testdata.responsemodels.user_response_model import SuccessResponse
from utilities.randomizer import Randomize
from dataclasses import asdict


@pytest.mark.user
def test_update_existing_user():

    user1 = UserModel()
    user_actions = UserActions()
    resp = user_actions.create_user(user1)

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    updated_user1_details = UserModel()
    updated_user1_details.username = Randomize().random_username()
    response = user_actions.update_user(user1.username, updated_user1_details)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {response.status_code}'

    success = SuccessResponse(200, 'unknown', str(updated_user1_details.id))

    logging.info('Validating Response SCHEMA for update_user()')
    assert validate_schema(response, SuccessResponse), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY for update_user()')
    assert validate_response_body(response, success), f'expected: {response.json()} \n actual: {asdict(success)}'

    logging.info(f'User with username {user1.username} updated successfully.')

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_user({updated_user1_details.username})')
    response = user_actions.get_user(updated_user1_details.username)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(response, UserModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(response, updated_user1_details), f'expected: {response.json()} \n ' \
                                                                    f'actual: {asdict(updated_user1_details)}'

    logging.info(f'User with username {user1.username} was updated and validated successfully.')


@pytest.mark.user
def test_update_existing_user_with_invalid_data():
    """ Validates whether This case is expected failure
    :return:
    """

    user1 = UserModel()
    user_actions = UserActions()
    resp = user_actions.create_user(user1)

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    # Expected type of Email and phone is string
    # Invalid data created with values as int and string with special chars
    updated_user1_details = UserModel()
    updated_user1_details.email = Randomize().random_integer()
    updated_user1_details.phone = Randomize().random_password()

    response = user_actions.update_user(user1.username, updated_user1_details)

    logging.info('Validating STATUS_CODE is BAD_REQUEST')
    assert response.status_code == HTTPStatus.BAD_REQUEST, f'Response is - {response.status_code}'

