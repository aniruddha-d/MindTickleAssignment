from requests import Response
from dataclasses import asdict
from testdata.datafactory import Model


def validate_schema(response: Response, schema_model: Model) -> bool:
    try:
        response_type = schema_model.__class__
        payload = response.json()
        d = response_type.from_dict(payload)
        return True
    except:
        return False


def validate_response_body(response: (Response, dict), expected_response_model: Model) -> bool:
    if isinstance(response, Response):
        response = response.json()
    response_model = Model.parse(response, expected_response_model.__class__)
    return True if expected_response_model == response_model else False


def validate_response_body_as_json(response: (Response, dict), expected_response_model: (Model, dict)) -> bool:
    if isinstance(response, Response):
        response = response.json()
    if isinstance(expected_response_model, Model):
        expected_response_model = asdict(expected_response_model)
    return True if expected_response_model == response else False


# class Validator:
#     """
#     Validate schema
#     Validate response status and body
#     Validate headers
#     """
#
#     def validate_schema(self, response: Response, schema_model: Model)-> bool:
#         try:
#             response_type = schema_model.__class__
#             payload = response.json()
#             d = response_type.from_dict(payload)
#             return True
#         except:
#             return False
#
#     def validate_response_body(self, response: (Response, dict), expected_response_model: Model) -> bool:
#         if isinstance(response, Response):
#             response = response.json()
#         response_model = Model.parse(response, expected_response_model.__class__)
#         return True if expected_response_model == response_model else False
#
#     def validate_response_body_as_json(self, response: (Response, dict), expected_response_model: (Model, dict)) -> bool:
#         if isinstance(response, Response):
#             response = response.json()
#         if isinstance(expected_response_model, Model):
#             expected_response_model = asdict(expected_response_model)
#         return True if expected_response_model == response else False
#
#
