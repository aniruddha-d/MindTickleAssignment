import pytest
import logging
from actions.users import Users as UserActions
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from testdata.responsemodels.user_response_model import SuccessResponse, InternalServerErrorResponse
from dataclasses import asdict
from utilities.randomizer import Randomize

@pytest.mark.user
def test_create_users_using_array():
    users_list = []
    for i in range(5):
        users_list.append(UserModel())

    user_actions = UserActions()
    resp = user_actions.create_users(users_list)

    success = SuccessResponse(200, 'unknown', 'ok')

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info('Validating Response SCHEMA for create_users()')
    assert validate_schema(resp, SuccessResponse), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY for create_users()')
    assert validate_response_body(resp, success), f'expected: {resp.json()} \n actual: {asdict(success)}'
    logging.info(f'{len(users_list)} users created successfully.')

    for user in users_list:
        logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for {user.username}')
        response = user_actions.get_user(user.username)

        logging.info('Validating STATUS_CODE is OK')
        assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

        logging.info(f'Validating Response SCHEMA')
        assert validate_schema(response, UserModel), 'Response schema is incorrect'

        logging.info(f'Validating Response BODY')
        assert validate_response_body(response, user), f'expected: {response.json()} \n actual: {asdict(user)}'

        logging.info(f'{user.username} was created and validated successfully.')

    logging.info('All Users created successfully.')


@pytest.mark.user
def test_create_duplicate_users():

    user1 = UserModel()
    user_actions = UserActions()
    resp = user_actions.create_user(user1)

    success_response = SuccessResponse(message=str(user1.id))
    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for create_user())')

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(resp, type(success_response)), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(resp, success_response), f'expected: {resp.json()} \n ' \
                                                           f'actual: {asdict(success_response)}'

    # create same user again. Assuming the creation should fail due to duplicate id and username
    resp = user_actions.create_user(user1)

    logging.info('Validating STATUS_CODE is CONFLICT')
    assert resp.status_code == HTTPStatus.CONFLICT, f'Response is - {resp.status_code}'


@pytest.mark.user
def test_create_user_with_alphanumeric_id():

    user1 = UserModel()
    user1.id = "abc123"

    user_actions = UserActions()
    resp = user_actions.create_user(user1)

    error_response = InternalServerErrorResponse()

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for create_user())')

    logging.info('Validating STATUS_CODE is INTERNAL_SERVER_ERROR')
    assert resp.status_code == HTTPStatus.INTERNAL_SERVER_ERROR, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(resp, type(error_response)), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(resp, error_response), f'expected: {resp.json()} \n ' \
                                                           f'actual: {asdict(error_response)}'


@pytest.mark.user
def test_create_user_with_int_parsable_string_id():

    user = UserModel()
    user.id = str(user.id)

    user_actions = UserActions()
    resp = user_actions.create_user(user)

    # convert user id into integer for further validations
    user.id = int(user.id)

    success_response = SuccessResponse(message=str(user.id))

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for create_user())')

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(resp, type(success_response)), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(resp, success_response), f'expected: {resp.json()} \n ' \
                                                           f'actual: {asdict(success_response)}'

    logging.info(f'Validating STATUS_CODE, SCHEMA and RESPONSE BODY for get_user({user.username})')
    response = user_actions.get_user(user.username)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating Response SCHEMA')
    assert validate_schema(response, UserModel), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY')
    assert validate_response_body(response, user), f'expected: {response.json()} \n actual: {asdict(user)}'
