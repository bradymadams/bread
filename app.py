from flask import Flask, request, render_template
import flask_assets

app = Flask('bread')

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
