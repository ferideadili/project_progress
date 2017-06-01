from flask import Blueprint
# coding=utf-8
import pprint
from app import mongo,project_utils,settings_utils
from bson import json_util, ObjectId
from flask import Blueprint, render_template, request, Response, redirect, url_for, flash,session
import os, json
import time
from datetime import datetime
from flask.ext.security import roles_accepted, roles_required

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/', methods=['GET'])
@roles_accepted('admin-user')
def index():
    return render_template('mod_admin/index.html')


@mod_admin.route('/projects')
@roles_accepted('admin-user')
def manage_projects():
    langs = settings_utils.get_supported_languages()
    return render_template('mod_admin/projects/manage.html',langs=langs)


@mod_admin.route('/projects/add', methods=['GET', 'POST'])
@mod_admin.route('/projects/upsert/<project_id>', methods=['GET', 'POST'])
@roles_accepted('admin-user')
def upsert_project(project_id=None):
    # Add a project
    langs = settings_utils.get_supported_languages()
    if request.method == 'POST':
        project = json.loads(request.data)
        project_utils.upsert(project_id, project)
        return redirect(url_for('admin.manage_projects'))
    # Load add project form
    else:
        if project_id is not None:
            project = project_utils.get_project(project_id)
            return render_template('mod_admin/projects/add_update.html', project_id=project_id, project=json.dumps(project),langs=langs)
        else:
            return render_template('mod_admin/projects/add_update.html', project_id='', project='{}',langs=langs)

@mod_admin.route('/projects/all')
def get_projects():
    projects = project_utils.all()
    return Response(response=json_util.dumps(projects), status=200, mimetype='application/json')


@mod_admin.route('/language/add', methods=['GET', "POST"])
@roles_accepted('admin-user')
def add_language():
    # Save new language settings
    if request.method == 'POST':
        lang = json.loads(request.data)
        print lang
        settings_utils.add_supported_language(lang)
        return Response(response=json_util.dumps({}), status=200, mimetype='application/json')

    # Load language settings page
    else:
        langs = settings_utils.get_supported_languages()
        return render_template('mod_admin/language/add.html', langs=json.loads(json_util.dumps(langs)))

@mod_admin.route('/manage/languages')
@roles_accepted('admin-user')
def manage_language():
    langs = settings_utils.get_supported_languages()
    return render_template('mod_admin/language/manage.html', langs=langs)

@mod_admin.route('/languages/all')
@roles_accepted('admin-user')
def get_all_languages():
    langs = settings_utils.get_supported_languages()
    return Response(response=json_util.dumps(langs), status=200, mimetype='application/json')


@mod_admin.route('/languages/update',methods=["POST"])
@roles_accepted('admin-user')
def update_languages():
    langs_doc = json_util.loads(request.data)
    settings_utils.update_supported_languages(langs_doc)
    return Response(response=json_util.dumps({}), status=200, mimetype='application/json')
