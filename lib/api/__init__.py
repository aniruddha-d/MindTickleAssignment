from config import Configs
import logging


def build_url(endpoint: str):
    base_url = Configs.base_url if Configs.base_url[-1] != '/' else Configs.base_url[:-1]
    endpoint = endpoint if endpoint[0] != '/' else endpoint[1:]
    api_version = Configs.api_version
    url = f'{base_url}/{api_version}/{endpoint}'
    logging.debug(f'URL --  {url}')
    return url


class Headers:
    request_headers = dict(Configs.request_headers)
    response_headers = dict(Configs.response_headers)
