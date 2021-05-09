from requests import Response
from dataclasses import asdict
from testdata.datafactory import Model


def validate_schema(response: dict, schema_model: type) -> bool:
    Model.parse(response, schema_model)
    return True


def validate_response_body(response: (Response, dict), expected_response_model: Model) -> bool:
    if isinstance(response, Response):
        response = response.json()
    response_model = Model.parse(response, type(expected_response_model))
    return True if expected_response_model == response_model else False


def validate_response_body_as_json(response: (Response, dict), expected_response_model: (Model, dict)) -> bool:
    if isinstance(response, Response):
        response = response.json()
    if isinstance(expected_response_model, Model):
        expected_response_model = asdict(expected_response_model)
    return True if expected_response_model == response else False


def validate_headers(headers_to_be_present: dict, response: Response) -> bool:
    response_headers = response.headers
    if headers_to_be_present.items() <= response_headers.items():
        return True
    else:
        return False

