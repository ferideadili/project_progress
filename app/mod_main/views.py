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
    theme = request.args.get('theme')
    return render_template('mod_main/index.html',theme=theme)


