from configparser import ConfigParser


class Configs:
    base_url: str
    request_headers: dict
    response_headers: dict

    @staticmethod
    def parse(filename, env='qa'):
        conf = ConfigParser()
        conf.read(filename)
        Configs.base_url = conf[env]['base_url']

        Configs.request_headers = dict(conf['request-headers'])
        Configs.response_headers = dict(conf['response-headers'])
