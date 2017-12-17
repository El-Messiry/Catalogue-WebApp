'''
Created on Dec 15, 2017

@author: messiry
'''
from flask import Flask, render_template, request, redirect,\
                  jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Cat_Item, Category, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalogue Item Application"

# Connect to Database and create database session
engine = create_engine('sqlite:///Catalogue.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Web app routes
@app.route('/login',methods=['GET'])
def login():
    return 'this is Login HTML'

@app.route('/main',methods=['GET'])
def main_index():
    return 'this is Main Index HTML'

@app.route('/category/new',methods=['GET','POST'])
def New_Category(cat_id):
    return 'NEW Category HTML'

@app.route('/category/<int:cat_id>',methods=['GET'])
def Show_Category(cat_id):
    return 'SHOW Category HTML'

@app.route('/category/<int:cat_id>/edit',methods=['GET','POST'])
def Edit_Category(cat_id):
    return 'EDIT Category HTML'

@app.route('/category/<int:cat_id>/delete',methods=['GET','POST'])
def Delete_Category(cat_id):
    return 'DELETE Category HTML'

@app.route('/category/<int:cat_id>/items',methods=['GET'])
def Show_Items(cat_id):
    return 'SHOW all items in Category HTML'

@app.route('/category/<int:cat_id>/item/new',methods=['GET','POST'])
def New_Item(cat_id,item_id):
    return 'New item in Category HTML'

@app.route('/category/<int:cat_id>/item/<int:item_id>',methods=['GET'])
def Show_Item(cat_id,item_id):
    return 'SHOW specific item in Category HTML'

@app.route('/category/<int:cat_id>/item/<int:item_id>/edit',methods=['GET','POST'])
def Edit_Item(cat_id,item_id):
    return 'EDIT specific item in Category HTML'

@app.route('/category/<int:cat_id>/item/<int:item_id>',methods=['GET','POST'])
def Delete_Item(cat_id,item_id):
    return 'DELETE specific item in Category HTML'



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
