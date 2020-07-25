import os
import sys
from flask import Flask, request
import configparser
import json

base_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, base_dir)

from classes.product import product
from classes.merchant import merchant
from classes.category import category
from classes.city import city

config = configparser.ConfigParser()
config.read(base_dir+"/conf/config.ini")

cl_product = product()
cl_merchant = merchant()
cl_category = category()
cl_city = city()


app = Flask(__name__)

## CITY
@app.route('/city/get/', methods=["GET"])
def get_city():
    return cl_city.get_all()


## CATEGORY
@app.route('/category/get/<city>/', methods=["GET"])
def get_category(city):
    return cl_category.get_category_by_city(city) 


## PRODUCT
@app.route('/product/get/<city>/<offset>/', methods=["GET"])
def get_product(city, offset):
    return cl_product.get_for_city(city, offset)


@app.route('/product/get/category/<category>/<offset>/', methods=["GET"])
def get_product_by_category(category, offset):
    return cl_product.get_for_city_category(city, category, offset)


@app.route('/product/get/merchant/<username>/<offset>/', methods=["GET"])
def get_product_by_merchant(username, offset):
    return cl_product.get_for_merchant(username, offset)              


@app.route('/product/create/', methods=["POST"])
def create_product():
    return cl_product.insert_product(request.data)


## MERCHANT
@app.route('/merchant/create/', methods=["POST"])
def create_merchant():
    pass


if __name__ == '__main__':
    app.run(host=config["SYSTEM"]["host"], 
            port=int(config["SYSTEM"]["port"]))