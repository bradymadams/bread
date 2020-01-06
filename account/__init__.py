from flask import Blueprint, render_template

account = Blueprint('account', __name__)

@account.route('/')
def all():
    return render_template('account/all.jinja')

blueprint = account
