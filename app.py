from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import flask_assets

app = Flask('bread', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bread.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

import models

assets = flask_assets.Environment(app)

styles = flask_assets.Bundle(
    'css/base.less',
    output='css/bread.css',
    filters='less,cssmin'
)

assets.register('css', styles)

# Blueprints
#import account
#app.register_blueprint(account.blueprint, url_prefix='/account')

@app.route('/')
def home():
    return render_template('home.jinja')

@app.route('/account/')
def all_accounts():
    return render_template('account/all.jinja')
