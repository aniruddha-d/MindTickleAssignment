import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from testdata.responsemodels.user_response_model import SuccessResponse
from dataclasses import asdict


@pytest.mark.user
def test_create_users_using_array():
    users_list = []
    for i in range(5):
        users_list.append(UserModel())

    user_actions = Users()
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
