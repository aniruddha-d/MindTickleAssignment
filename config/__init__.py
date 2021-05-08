from configparser import ConfigParser


class Configs:
    base_url: str

    @staticmethod
    def parse(filename, env='qa'):
        conf = ConfigParser()
        conf.read(filename)
        Configs.base_url = conf[env]['base_url']
