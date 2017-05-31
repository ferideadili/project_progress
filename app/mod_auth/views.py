from flask import Blueprint, render_template, request, redirect,Response, url_for, g, current_app
from app import user_datastore, bcrypt, user_utils, mongo,UPLOAD_FOLDER,ALLOWED_EXTENSIONS
from flask.ext.security import login_user, logout_user
import os, json


mod_auth = Blueprint('auth', __name__, url_prefix='/<lang_code>/theme/<theme>/auth')

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        email= form['email']
        user = user_datastore.find_user(email=email)
        if user:
            if user['role'] == 'basic-user':
                if bcrypt.check_password_hash(user['password'].encode('utf-8'), form['password'].encode('utf-8')):
                    remember_me = False
                    login_user(user, remember_me)
                    return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))
                else:
                    error = "Invalid username/password"
                    return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))
            elif user['role'] == 'admin-user':
                if bcrypt.check_password_hash(user['password'].encode('utf-8'), form['password'].encode('utf-8')):
                    remember_me = False
                    login_user(user, remember_me)
                    return redirect(url_for('admin.index'))
                else:
                    error = "Invalid username/password"
                    return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))
        else:
            return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))


@mod_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))


@mod_auth.route('/register/user', methods=['GET', 'POST'])
def registeruser():
    if request.method == "GET":
        return render_template('mod_auth/register.html',theme=g.current_theme,lang_code=g.current_lang)
    else:
        form = request.form
        email = form['email']
        password = form['password']

        if user_datastore.find_user(email=email):
            error = "A user with that e-mail already exists in the database"
            return render_template('mod_main/index.html', error=error)
        else:
            user_datastore.create_user(
                email=email,
                role='basic-user',
                password=bcrypt.generate_password_hash(password, rounds=12),
            )
            role = user_datastore.find_role('basic-user')
            user = user_datastore.find_user(email=email)
            result = None
            if role:
                result = user_datastore.add_role_to_user(user, role)
            else:
                user_datastore.create_role(name="basic-user")
                role = user_datastore.find_role('basic-user')
                result = user_datastore.add_role_to_user(user, role)
                login_user(user)

        return redirect(url_for('main.root',theme=g.current_theme,lang_code=g.current_lang))