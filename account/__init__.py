from flask import Blueprint, render_template
from app import db

account = Blueprint('account', __name__)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

@account.route('/')
def all():
    return render_template('account/all.jinja')

blueprint = account
