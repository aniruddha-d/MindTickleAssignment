import pytest
import logging
from actions.pets import Pets
from testdata.datafactory.pet_factory import PetModel
from http import HTTPStatus
from lib.api.validator import validate_response_body, validate_response_body_as_json, validate_schema, validate_response_headers
from dataclasses import asdict
from dataclasses_jsonschema import ValidationError
from config import Configs


@pytest.mark.pet
def test_create_pet():
    m1 = PetModel()  # model
    resp = Pets().create_pet(m1)

    assert validate_response_headers(Configs.response_headers, resp), f'Header is incorrect. ' \
                                                                      f'expected: {Configs.response_headers} \n ' \
                                                                      f'actual: {resp.headers}'
    assert resp.status_code == 200

    resp2 = Pets().get_pet(m1.id)  # response
    assert validate_response_body(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'
    resp2 = resp2.json()
    assert validate_response_body(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2 = Pets().get_pet(m1.id)  # response
    assert validate_response_body_as_json(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'
    assert validate_response_body_as_json(resp2, asdict(m1)), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2 = resp2.json()
    assert validate_response_body_as_json(resp2, m1), f'expected: {resp2.json()} \n actual: {asdict(m1)}'
    assert validate_response_body_as_json(resp2, asdict(m1)), f'expected: {resp2.json()} \n actual: {asdict(m1)}'

    resp2.pop('tags')

    with pytest.raises(ValidationError):
        assert validate_schema(resp2, PetModel), 'Schema validated. ValidationError not raised'


