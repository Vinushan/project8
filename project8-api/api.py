import os
import sys
from flask import Flask
import configparser
import json

base_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, base_dir)

from classes.product import product
from classes.seller import seller

config = configparser.ConfigParser()
config.read(base_dir+"/conf/config.ini")

cl_product = product()
cl_seller = seller()


app = Flask(__name__)


@app.route('/seller/create_user/', methods=["POST"])
def create_user():
    pass


@app.route('/product/add_product/', methods=["POST"])
def add_product():
    return cl_product.insert_product(product)


@app.route('/product/get/<offset>/<size>', methods=["GET"])
def get_products(offset=0, size=20):
    return cl_product.get_all(offset, size)


if __name__ == '__main__':
    app.run(host=config["SYSTEM"]["host"], 
            port=int(config["SYSTEM"]["port"]))