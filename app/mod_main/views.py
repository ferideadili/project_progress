from flask import Blueprint
# coding=utf-8
import pprint
from app import mongo,UPLOAD_FOLDER,ALLOWED_EXTENSIONS,user_utils
from bson import json_util, ObjectId
from flask import Blueprint, render_template, request, Response, redirect, url_for, flash,session
import os, json
import time
from datetime import datetime
from flask.ext.security import current_user
mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    producers = user_utils.find_all_producers()

    return render_template('mod_main/index.html',producers=json.loads(json_util.dumps(producers)))

@mod_main.route('/products', methods=['GET'])
def products():
    return render_template('mod_products/products.html')

@mod_main.route('/add/product', methods=['GET'])
def addproducts():
    return render_template('mod_products/add.html')

@mod_main.route('/admin/add/vehicles', methods=['GET', 'POST'])
def addvehicle():
    if request.method == "GET":
        # Return the login form template
        return render_template('mod_main/add_vehicles.html')
    else:
        data = request.form.to_dict()
        docs=mongo_utils.insert_vehicle(data)
    flash('Vehicle is added')
    return redirect(url_for('main.managevehicles'))


@mod_main.route('/admin/manage/vehicles', methods=['GET'])
def managevehicles():
    return render_template('mod_main/admin_vehicles.html')

@mod_main.route('/get/vehicles', methods=['GET', 'POST'])
def find_all_vehicles():
    if request.method == 'GET':
        result=mongo_utils.find_all_vehicles()
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')