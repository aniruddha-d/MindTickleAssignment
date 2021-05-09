import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import UserModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_response_body_as_json, validate_schema
from dataclasses import asdict


@pytest.mark.user
def test_create_users():
    assert 1 + 1 == 2
    u1 = UserModel()
    u2 = UserModel()
    u3 = UserModel()
    u4 = UserModel()

    resp = Users().create_users([u1, u2, u3, u4])
    assert resp.status_code == HTTPStatus.OK
    logging.info(resp.status_code)


@pytest.mark.user
def test_create_user():
    m1 = UserModel()  # model
    resp = Users().create_user(m1)
    assert resp.status_code == 200

    resp2 = Users().get_user(m1.username)  # response
    assert validate_response_body(resp2, m1) == True
    resp2 = resp2.json()
    assert validate_response_body(resp2, m1) == True

    resp2 = Users().get_user(m1.username)  # response
    assert validate_response_body_as_json(resp2, m1) == True
    assert validate_response_body_as_json(resp2, asdict(m1)) == True

    resp2 = resp2.json()
    assert validate_response_body_as_json(resp2, m1) == True
    assert validate_response_body_as_json(resp2, asdict(m1)) == True
