from flask import Blueprint,g
# coding=utf-8
import pprint
from app import mongo,user_utils,projects
from bson import json_util, ObjectId
from flask import Blueprint, render_template, request, Response, redirect, url_for, flash,session
import os, json
import time
from datetime import datetime
from flask.ext.security import current_user
mod_main = Blueprint('main', __name__,static_folder="static")


@mod_main.route('/', methods=['GET'])
def index():
    return redirect("/en/theme/default")

@mod_main.route('/<lang_code>/theme/<theme>/', methods=['GET'])
def root():
    return render_template('mod_main/index.html', theme=g.current_theme, lang_code=g.current_lang,projects=projects)


@mod_main.route('/<lang_code>/theme/<theme>/notes/projectId/<int:project_id>', methods=['GET'])
def notes(project_id):
    for project in projects:
        if project["id"] == project_id:
            target_project = project
    return render_template('mod_main/notes.html', theme=g.current_theme, lang_code=g.current_lang,project=target_project)