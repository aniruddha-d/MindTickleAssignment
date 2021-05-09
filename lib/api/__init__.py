api_version = 'v2'
from config import Configs


def build_url(endpoint: str):
    base_url = Configs.base_url if Configs.base_url[-1] != '/' else Configs.base_url[:-1]
    endpoint = endpoint if endpoint[0] != '/' else endpoint[1:]
    return f'{base_url}/{api_version}/{endpoint}'


class Headers:
    request_headers = dict(Configs.request_headers)
    response_headers = dict(Configs.response_headers)

