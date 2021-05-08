from pytest import fixture
from utilities import loggers
from datetime import datetime
from config import Configs
import logging
import os


def pytest_addoption(parser):
    logging.debug("Running pytest_addoption...")
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--loglevel", action="store", default="DEBUG")


def pytest_configure(config):
    logging.debug("Running pytest_configure... ")
    rootdir = os.path.join(config.rootdir).split('testcases')[0]

    os.environ['ENV'] = config.getoption("--env")
    config_file_path = os.path.join(rootdir, 'config', 'configs.ini')
    Configs.parse(config_file_path, config.getoption("--env"))

    log_file_name_format = datetime.now().strftime('%d-%b-%Y-%H-%M-%S')
    result_dir = os.path.join(rootdir, 'results')
    try:
        os.makedirs(result_dir)
    except OSError as ose:
        logging.error(ose)
    except Exception as e:
        logging.error(e)

    txt_log_file = f'auto_log_{log_file_name_format}.log'
    html_log_file = f'auto_log_{log_file_name_format}.html'
    xml_log_file = f'auto_log_{log_file_name_format}.xml'
    fo = open(os.path.join(result_dir, txt_log_file), "w+")
    fo.close()

    config.option.htmlpath = os.path.join(result_dir, html_log_file)
    config.option.log_file = os.path.join(result_dir, txt_log_file)
    config.option.xmlpath = os.path.join(result_dir, xml_log_file)
    loggers.init_logging(os.path.join(result_dir, txt_log_file), config.getoption("--loglevel"))
    logging.debug(f'Result directory is created as {result_dir}')


def pytest_sessionstart(session):
    """ Pytest session begins here """
    session.results = dict()


def pytest_sessionfinish(session, exitstatus):
    """ Pytest session ends here """

    logging.info("Execution completed")


@fixture(scope='session')
def setup():
    pass

