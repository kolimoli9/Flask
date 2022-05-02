from distutils.log import debug
from flask import Flask, redirect,render_template, request, url_for, Blueprint, flash
import sqlite3
from sqlite3 import Error
import json
from admin import admin



con=sqlite3.connect('users.db',check_same_thread=False)
cur=con.cursor()

app = Flask(__name__)

app.register_blueprint(admin)

def createDB():
    cur.execute("CREATE TABLE Admins('Name' text,'Password' text,'Email' text)")
    con.commit()


def initDB(name,pwd,mail):
    cur.execute(f"INSERT INTO Admins VALUES('{name}' ,'{pwd}' ,'{mail}')")
    con.commit()

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/create',methods=['GET','POST'])
def create_account():
    pwd = request.form.get('password')
    mail = request.form.get('email')
    name = request.form.get('username')
    initDB(name,pwd,mail)
    return redirect('/')

@app.route('/')
def Login():
    return render_template('loginPage.html')

@app.route('/login',methods=['GET','POST'])
def validate():
    Admins={'Pwd': 0, 'Mail':0}
    mail=request.form.get('email') 
    pwd=request.form.get('password')
    cur.execute("SELECT * from Admins")
    for line in cur:
        Admins['Pwd']=line[1]
        Admins['Mail']=line[2]
        print(line[1], line[2])
    if mail == Admins['Mail'] and pwd == Admins['Pwd']:    
        return redirect('/home')
    else:
        return render_template('loginPage.html',admin=False)    
    
@app.route('/shop')
def about():
    return render_template('shop.html')

@app.route('/home')
def get_home():
    return render_template('main.html',link1='active')

@app.route('/gallery')
def get_education():
    return render_template('gallery.html',link4='active')


if __name__=='__main__':
    app.run(debug=True) 