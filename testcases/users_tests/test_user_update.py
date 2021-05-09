import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_schema
from testdata.responsemodels.user_creation_model import SuccessResponse
from utilities.data_time_utils import get_timestamp


@pytest.mark.user
def test_create_users_using_array():

    user1 = UserModel()
    user_actions = Users()
    resp = user_actions.create_user(user1)

    logging.info('Validating STATUS_CODE is OK')
    assert resp.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    updated_user1_details = UserModel()
    updated_user1_details.username += get_timestamp()
    response = user_actions.update_user(user1.username, updated_user1_details)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {response.status_code}'

    success = SuccessResponse(200, 'unknown', str(updated_user1_details.id))
    logging.info('Validating response schema for update_user()')
    assert validate_schema(response, SuccessResponse) == True, 'Response schema is incorrect'

    logging.info(f'Validating response body for update_user()')
    assert validate_response_body(response, success)
    logging.info(f'User with username {user1.username} updated successfully.')

    logging.info(f'Validation STATUS_CODE, SCHEMA and RESPONSE BODY for {updated_user1_details.username}')
    response = user_actions.get_user(updated_user1_details.username)

    logging.info('Validating STATUS_CODE is OK')
    assert response.status_code == HTTPStatus.OK, f'Response is - {resp.status_code}'

    logging.info(f'Validating response schema')
    assert validate_schema(response, UserModel) == True, 'Response schema is incorrect'

    logging.info(f'Validating response body')
    assert validate_response_body(response, updated_user1_details)

    logging.info(f'User with username {user1.username} was updated and validated successfully.')



