"""
This module will contain method for calling rest api
"""

import requests
import json


class InvalidMethodException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MethodNotImplementedException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Method:
    GET = 'GET'
    PUT = 'PUT'
    POST = 'POST'
    HEAD = 'HEAD'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'


def execute_rest_api(method, target, headers: dict = None, data: (dict, list, bytes) = None,
                     json_body: (list, dict) = None, query_params: dict = None,
                     tls_verify=True, validate_response=True) -> requests.Response:
    """
    :param method:
    :param target:
    :param headers:
    :param data:
    :param json_body:
    :param query_params:
    :param tls_verify:
    :param validate_response:
    :return:
    """
    method = method.upper()
    resp: requests.Response = None

    if method == Method.GET:
        resp = __get(target, query_params=query_params, headers=headers)
    elif method == Method.PUT:
        resp = __put(target, data=data, json_body=json_body, headers=headers)
    elif method == Method.POST:
        resp = __post(target, data=data, json_body=json_body, headers=headers)
    elif method == Method.HEAD:
        resp = __head(target, headers=headers)
    elif method == Method.PATCH:
        resp = __patch(target, data=data, json_body=json_body, headers=headers)
    elif method == Method.DELETE:
        resp = __delete(target, headers=headers)
    elif method in [Method.OPTIONS]:
        raise MethodNotImplementedException(f"'{method}' method not implemented")
    else:
        raise InvalidMethodException(f"'{method}' is invalid HTTP method")

    if validate_response:
        pass

    return resp


def __get(url, query_params: dict = None, headers: dict = None):
    return requests.get(url, params=query_params, headers=headers, verify=True)


def __put(url, data: (dict, list, bytes) = None, json_body: dict = None, headers: dict = None):
    return requests.put(url, data=data, json=json_body, headers=headers)


def __post(url, data: (dict, list, bytes) = None, json_body: dict = None, headers: dict = None):
    return requests.post(url, data=data, json=json_body, headers=headers)


def __head(url, headers: dict = None):
    return requests.head(url, headers=headers)


def __patch(url, data: (dict, list, bytes) = None, json_body: dict = None, headers: dict = None):
    return requests.patch(url, data=data, json=json_body, headers=headers)


def __delete(url, headers: dict = None):
    return requests.patch(url, headers=headers)


if __name__ == '__main__':
    dct = {"id": 0, "category": {"id": 0, "name": "string"}, "name": "doggie",
           "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}

    x = execute_rest_api(Method.POST, 'https://petstore.swagger.io/v2/pet', json_body=dct)
    print(x.status_code, json.loads(x.text))

    x = execute_rest_api(Method.GET, 'https://petstore.swagger.io/v2/pet/9222968140498746236')
    print(x.status_code, json.loads(x.text))

    x = execute_rest_api(Method.GET, 'https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    print(x.status_code, json.loads(x.text))

    x = execute_rest_api(Method.GET, 'https://petstore.swagger.io/v2/pet/findByStatus',
                         query_params={'status': 'available'})
    print(x.status_code, json.loads(x.text))

    lst = [{"id": 0, "username": "string", "firstName": "string", "lastName": "string", "email": "string",
            "password": "string", "phone": "string", "userStatus": 0}]
    x = execute_rest_api(Method.POST, 'https://petstore.swagger.io/v2/user/createWithArray', json_body=lst)
    print(x.status_code, json.loads(x.text))

    x = execute_rest_api(Method.GET, 'https://petstore.swagger.io/v2/user/string')
    print(x.status_code, json.loads(x.text))
