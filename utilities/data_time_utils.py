from datetime import datetime
import logging
import time
import uuid


def get_timestamp() -> str:
    """ Return unique time stamp from uuid module
    :return:
    """
    datetime_stamp = str(uuid.uuid1().time)
    logging.debug(datetime_stamp)
    return datetime_stamp
