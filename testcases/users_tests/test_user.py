import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_response_body_as_json, validate_schema
from dataclasses import asdict
from utilities.data_time_utils import get_timestamp
from testdata.responsemodels.user_response_model import NotFoundResponse


@pytest.mark.user
def test_create_user():
    m1 = UserModel()  # model
    resp = Users().create_user(m1)
    assert resp.status_code == 200

    resp2 = Users().get_user(m1.username)  # response
    assert validate_response_body(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2 = resp2.json()
    assert validate_response_body(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2 = Users().get_user(m1.username)  # response
    assert validate_response_body_as_json(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    assert validate_response_body_as_json(resp2, asdict(m1)), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2 = resp2.json()
    assert validate_response_body_as_json(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    assert validate_response_body_as_json(resp2, asdict(m1)), f'expected: {resp2.json()} \n actual: {asdict(m1)}'


@pytest.mark.user
def test_get_non_existing_user():
    username = get_timestamp()
    resp = Users().get_user(username)  # response
    not_found_model = NotFoundResponse()

    logging.info('Validating STATUS_CODE is NOT_FOUND')
    assert resp.status_code == HTTPStatus.NOT_FOUND, f'Response is - {resp.status_code}'

    logging.info('Validating Response SCHEMA for get_user()')
    assert validate_schema(resp, type(not_found_model)), 'Response schema is incorrect'

    logging.info(f'Validating Response BODY for update_user()')
    assert validate_response_body(resp, not_found_model), f'expected: {resp.json()} \n actual: {asdict(not_found_model)}'

    logging.info(f'User with username {username} not found.')

