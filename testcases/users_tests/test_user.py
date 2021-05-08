import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import ModelUser, ModelUserList


@pytest.mark.user
def test_create_users():
    assert 1 + 1 == 2
    u1 = ModelUser()
    u2 = ModelUser()
    u3 = ModelUser()
    u4 = ModelUser()

    resp = Users().create_users([u1, u2, u3, u4])
    assert resp.status_code == 200
    logging.info(resp.status_code)


@pytest.mark.user
def test_create_user():
    resp = Users().create_user(ModelUser())
    assert resp.status_code == 200
    logging.info(resp.status_code)
