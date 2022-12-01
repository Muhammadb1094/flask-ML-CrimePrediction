import os
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user, current_user
import pandas as pd
from .ml_recidivism import GetDataVisualizations, GetImageDataVisualizations
from app import app, lm, bc
from app.models import Users
from app.forms import LoginForm, RegisterForm
from .utilities import remove_old_files, get_new_files


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/import-data/', methods=['GET', 'POST'])
def import_data():
    msg = None
    success = False

    if request.method == 'GET':
        remove_old_files()
        return render_template('import_data.html', msg=msg)

    if request.method == 'POST':
        excel_sheet = request.files["excelsheet"]
        if excel_sheet:
            data = pd.read_csv(excel_sheet, error_bad_lines=False)
            visualizer = GetImageDataVisualizations()

            visualizer.convicting_offense(data)
            visualizer.age_at_release(data)
            visualizer.who_didnt_return(data)
            visualizer.algo_accuracy()

            return render_template('import_data.html', images=get_new_files())

        else:
            msg = "Excel sheet Required"
        return render_template('import_data.html', msg=msg, success=success)
    else:
        msg = 'Input error'

    return render_template('import_data.html', msg=msg, success=success)


# Register a new user
@app.route('/register/', methods=['GET', 'POST'])
def register():
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None
    success = False

    if request.method == 'GET':
        return render_template('register.html', form=form, msg=msg)

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'

        else:

            pw_hash = bc.generate_password_hash(password)

            user = Users(username, email, pw_hash)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True

    else:
        msg = 'Input error'

    return render_template('register.html', form=form, msg=msg, success=success)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:

            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template('login.html', form=form, msg=msg)


@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        if request.method == "GET":
            return render_template('index.html')


@app.route('/import-web-view/', methods=['POST', 'GET'])
def web_view():
        if request.method == "POST":
            msg = None
            success = True
            excel_sheet = request.files["excelsheet"]
            if excel_sheet:
                data = pd.read_csv(excel_sheet, error_bad_lines=False)
                visualizer = GetDataVisualizations()

                if request.form.get("convicting_offence", False):
                    visualizer.convicting_offense(data)
                if request.form.get("age_release", False):
                    visualizer.age_at_release(data)

                if request.form.get("accuracy", False):
                    visualizer.algo_accuracy()

                if request.form.get("not_released", False):
                    visualizer.who_didnt_return(data)
                else:
                    msg = "Select at least one option!"
                    return render_template('index.html', msg=msg)

                return render_template('index.html', msg=msg)
            else:
                msg = "Excel sheet Required"
            return render_template('index.html', msg=msg, success=success)
        else:
            if not current_user.is_authenticated:
                return render_template('index.html')
            else:
                    return render_template('index.html')


@app.route('/sitemap.xml/')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
