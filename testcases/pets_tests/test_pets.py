import pytest
import logging
from actions.users import Users
from testdata.datafactory.user_factory import ModelUser, ModelUserList


@pytest.mark.pet
def test_create_pets():
    assert 1 + 1 == 2


@pytest.mark.pet
def test_create_pet():
    assert 1 + 1 == 2
