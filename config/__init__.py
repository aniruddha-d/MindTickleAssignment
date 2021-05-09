from configparser import ConfigParser


class Configs:
    base_url: str
    api_version: str
    request_headers: dict
    response_headers: dict

    @staticmethod
    def parse(filepath, env='qa'):
        """ Parses configs.ini file for given environment
        :param filepath: filepath of the configs.ini file
        :param env: environment section from ini file
        :return:
        """
        conf = ConfigParser()
        conf.read(filepath)
        Configs.base_url = conf[env]['base_url']
        Configs.api_version = conf[env]['api_version']

        Configs.request_headers = dict(conf['request-headers'])
        Configs.response_headers = dict(conf['response-headers'])
