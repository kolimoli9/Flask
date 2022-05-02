from re import template
from flask import Flask,Blueprint,render_template

admin = Blueprint('admin',__name__,url_prefix='/admin')


@admin.route('/')
def admin_main():
    return render_template('main.html')


@admin.route('/add')
def admin_add():
    pass


@admin.route('/del')
def admin_del():
    pass