from flask import Blueprint,g
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
    return redirect("/en/theme/default")

@mod_main.route('/<lang_code>/theme/<theme>', methods=['GET'])
def root():
    print g.current_lang
    return render_template('mod_main/index.html',theme=g.current_theme,lang_code=g.current_lang)

