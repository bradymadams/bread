from flask import Flask, request, render_template
import flask_assets

import account

app = Flask('bread', template_folder='templates')

app.register_blueprint(account.blueprint, url_prefix='/account')

assets = flask_assets.Environment(app)

styles = flask_assets.Bundle(
    'css/base.less',
    output='css/bread.css',
    filters='less,cssmin'
)

assets.register('css', styles)

@app.route('/')
def home():
    return render_template('home.jinja')
