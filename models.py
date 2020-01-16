
from app import db

class SpendCategory(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))
    starting_balance = db.Column(db.Integer)
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))
    null_category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    budget = db.relationship('Budget', backref=db.backref('accounts'))
    null_category = db.relationship('SpendCategory')

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(length=128))
    comments = db.Column(db.String(length=128))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    account = db.relationship('Account', backref=db.backref('transactions'))
    category = db.relationship('SpendCategory', backref=db.backref('transactions'))

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))

class BudgetCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    months = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    budget = db.relationship('Budget', backref=db.backref('categories'))
    category = db.relationship('SpendCategory')
