import os
import sys
import psycopg2
import configparser
from psycopg2.extras import RealDictCursor
from .logger import get_logger

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, base_dir)
config = configparser.ConfigParser()
config.read(base_dir+"/conf/config.ini")

pgsql_connection = None
pgsql_cursor = None


def get_pgsql_cursor():
    global pgsql_connection, pgsql_cursor
    if pgsql_connection and pgsql_cursor:
        return pgsql_cursor
    else:
        return __create_pgsql_connection()


def __create_pgsql_connection():
    logger = get_logger()
    try:
        global pgsql_connection, pgsql_cursor
        pgsql_connection = psycopg2.connect(host=config["POSTGRES"]["host"],
                                            port=int(config["POSTGRES"]["port"]),
                                            database=config["POSTGRES"]["database"],
                                            user=config["POSTGRES"]["user"],
                                            password=config["POSTGRES"]["password"])
        pgsql_cursor = pgsql_connection.cursor(cursor_factory=RealDictCursor)
        logger.info("Connection Made with postgres server.")
        return pgsql_cursor
    except:
        logger.error("Couldn't connect to postgres server.")
        sys.exit()


def pgsql_commit():
    global pgsql_connection
    pgsql_connection.commit()


def pgsql_rollback():
    global pgsql_connection
    pgsql_connection.rollback()


def close_pgsql_connection():  
    global pgsql_connection, pgsql_cursor      
    pgsql_cursor.close()
    pgsql_connection.close()