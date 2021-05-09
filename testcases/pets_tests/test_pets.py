import pytest
import logging
from actions.pets import Pets
from testdata.datafactory.pet_factory import ModelPet
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_response_body_as_json, validate_schema

from dataclasses import asdict

@pytest.mark.pet
def test_create_pet():
    m1 = ModelPet()   # model
    resp = Pets().create_pet(m1)
    assert resp.status_code == 200

    resp2 = Pets().get_pet(m1.id)  # response
    assert validate_response_body(resp2, m1) == True
    resp2 = resp2.json()
    assert validate_response_body(resp2, m1) == True

    resp2 = Pets().get_pet(m1.id)  # response
    assert validate_response_body_as_json(resp2, m1) == True
    assert validate_response_body_as_json(resp2, asdict(m1)) == True

    resp2 = resp2.json()
    assert validate_response_body_as_json(resp2, m1) == True
    assert validate_response_body_as_json(resp2, asdict(m1)) == True

