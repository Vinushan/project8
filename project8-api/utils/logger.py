import os
import sys
import logging
import configparser

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, base_dir)
config = configparser.ConfigParser()
config.read(base_dir+"/conf/config.ini")

logger = None

def get_logger():
    global logger
    if logger:
        return logger
    else:
        return __create_logger()


def __create_logger():
    global logger
    logging.basicConfig(filename=base_dir+"/logs/api.log",
                        format='%(asctime)s %(message)s',
                        filemode='a+')
    logger = logging.getLogger()
    logger.setLevel(level = config["LOG"]["level"])
    return logger  
    