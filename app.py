'''
Created on Dec 15, 2017

@author: messiry
'''
from flask import Flask, render_template, request, redirect,\
                  jsonify, url_for, flash
from sqlalchemy import create_engine, desc
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
app_port = 8000

CLIENT_ID = json.loads(
    open('g_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalogue Menu App"

# Connect to Database and create database session
engine = create_engine('sqlite:///Catalogue.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Web app routes

# ----------------------------------------------------- #
# ----------------  Login Routes  --------------------- #
# ----------------------------------------------------- #

# <<<<<<<<<<<<<<<<<<<< Methods >>>>>>>>>>>>>>>>>>>>>>>>>>


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def getUser(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user
    except:
        return None


def html_output(login_session):
    output = ''
    output += '<div class="welocme-container"><div class="welcome-header">'
    output += '<h1>Welcome'
    output += login_session['username']
    output += '!</h1></div>'
    output += '<div class="welcome-img"><img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    output += '</div></div>'
    return output
# <<<<<<<<<<<<<<<<<<<< Routes >>>>>>>>>>>>>>>>>>>>>>>>>>


@app.route('/login', methods=['GET'])
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = (request.data).decode('utf-8')
    print ("access token received %s " % access_token)


    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = (h.request(url, 'GET')[1]).decode('utf-8')


    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    '''
        Due to the formatting for the result from the server token exchange we have to
        split the token first on commas and select the first index which gives us the key : value
        for the server access token then we split it on colons to pull out the actual token value
        and replace the remaining quotes with nothing so that it can be used directly in the graph
        api calls
    '''
    print("result is "+str(result))
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = (h.request(url, 'GET')[1]).decode('utf-8')
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = (h.request(url, 'GET')[1]).decode('utf-8')
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    login_session['provider'] = 'facebook'
    
    
    flash("Now logged in as %s" % login_session['username'])
    return html_output(login_session)



@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('g_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    req = h.request(url, 'GET')[1]
    result = json.loads(req.decode('utf-8'))

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    print(access_token)
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                                'Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'
    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    flash("you are now logged in as %s" % login_session['username'])

    return html_output(login_session)

def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = (h.request(url, 'DELETE')[1]).decode('utf-8')

    del login_session['access_token']
    del login_session['facebook_id']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['provider']
    response = make_response(json.dumps('Successfully disconnected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return True


def gdisconnect():
        # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    print(access_token)
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['provider']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return True
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route("/disconnect", methods=['GET'])
def disconnect():
    if login_session['provider']=='google':
        if gdisconnect() :
            return redirect(url_for('Main_Index'))
    elif login_session['provider']=='facebook':
        if fbdisconnect():
            return redirect(url_for('Main_Index'))
    
    return

# <<<<<<<<<<< End Of Login Methods & Routes >>>>>>>>>>>>>

# ----------------------------------------------------- #
# ---------------- WebApp Routes  --------------------- #
# ----------------------------------------------------- #


def to_dict(obj):
    '''
        Returns Dictionary type of the object given
    '''
    result = []
    try:
        for item in obj:
            result.append(item.__dict__)
    except:
        return obj.__dict__
    return result


def validate_data(cat=0, catItem=0):
    if cat:
        if cat['name'] == '' or cat['desc'] == '':
            return False
            # should implement Regression to check validity of name and minimum
            # number of characters for the description
    if catItem:
        if catItem['name'] == '' or catItem['desc'] == '':
            return False
            # should implement Regression to check validity of name and minimum
            # number of characters for the description

    return True


def bool_username():
    if 'username' not in login_session:
        return False
    else:
        return True


@app.route('/')
@app.route('/main', methods=['GET'])
def Main_Index():
    # fetch all categories
    cats = session.query(Category).all()
    # convert it to Dict type
    #cats = to_dict(cats_obj)
    # fetch latest added items .
    items = session.query(Cat_Item).order_by(desc(Cat_Item.date)).limit(10)
    # convert it to Dict type
    #items = to_dict(items_obj)

    return render_template("main.html",
                           items=items,
                           cats=cats,
                           username=bool_username())


@app.route('/category/new', methods=['GET', 'POST'])
def New_Category():
    if 'username' not in login_session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template("new_category.html")

    if request.method == 'POST':
        cat = {}

        # fetch form data & assign it to corresponding Dict key
        cat['name'] = request.form.get('cat_name')
        cat['desc'] = request.form.get('cat_desc')
        # DB commit
        session.add(Category(name=cat['name'],
                             description=cat['desc'],
                             user_id=login_session['user_id']))

        session.commit()
        return redirect(url_for('Main_Index'))


@app.route('/category/<int:cat_id>', methods=['GET'])
def Show_Category(cat_id):
    # fetch all categories
    cat = session.query(Category).filter_by(id=cat_id).one()
    items = session.query(Cat_Item).filter_by(category_id=cat_id).all()
    
    if 'username' not in login_session:
        return render_template('puplic_category.html',
                               items=items,
                               cat=cat,
                               cat_id=cat_id)
    
    user_auth = True
    if cat.user_id != login_session['user_id']:     # Non Authorized user
        user_auth = False      # Flash error
    
    
    # convert it to Dict type
    #cat = to_dict(cat)
    #items = to_dict(items)

    return render_template("category_items.html",
                           cat=cat,
                           items=items,
                           username=bool_username(),
                           user_auth=user_auth)


@app.route('/category/<int:cat_id>/edit', methods=['GET', 'POST'])
def Edit_Category(cat_id):
    # fetch all categories
    cat = session.query(Category).filter_by(id=cat_id).one()
    # check if user logged in
    if 'username' not in login_session:
        return redirect(url_for('login'))

    if cat.user_id != login_session['user_id']:     # Non Authorized user
        return redirect(url_for('Main_Index'))      # Flash error

    if request.method == 'GET':
        # convert item to dict
        #cat = to_dict(cat)
        #print(cat)
        return render_template("edit_category.html", cat=cat)

    if request.method == 'POST':
        cat = {}
        cat['name'] = request.form.get('cat_name')
        cat['desc'] = request.form.get('cat_desc')

        # data form validation should go here !
        if not (validate_data(cat)):
            return redirect(url_for('Main_Index'))

        # retrieving DB object to modify
        category = session.query(Category).filter_by(id=cat_id).one()

        # updating Values
        category.name = cat['name']
        category.description = cat['desc']

        # Add & Commit changes
        session.add(category)
        session.commit()
        print("category has been edited successfully !")
        return redirect(url_for('Main_Index'))


@app.route('/category/<int:cat_id>/delete', methods=['GET', 'POST'])
def Delete_Category(cat_id):
    # fetch all categories
    cat = session.query(Category).filter_by(id=cat_id).one()
    # check if user logged in
    if 'username' not in login_session:
        return redirect(url_for('login'))

    if cat.user_id != login_session['user_id']:      # Non Authorized user
        return redirect(url_for('Main_Index'))       # Flash error

    if request.method == 'GET':
        # fetch all categories
        cat = session.query(Category).filter_by(id=cat_id).one()
        #cat = to_dict(cat)
        return render_template("delete_category.html", cat=cat)

    if request.method == 'POST':
        cat = session.query(Category).filter_by(id=cat_id).one()
        session.delete(cat)
        session.commit()
        return redirect(url_for('Main_Index'))


@app.route('/category/<int:cat_id>/items', methods=['GET'])
def Show_Items(cat_id):
    if request.method == 'GET':
        cat = session.query(Category).filter_by(id=cat_id).one()
        # fetch latest added items .
        items = session.query(Cat_Item).filter_by(category_id=cat_id).all()
        # convert it to Dict type
        #items = to_dict(items)

        return render_template("category_items.html",
                               cat=cat,
                               items=items,
                               username=bool_username())


@app.route('/category/<int:cat_id>/item/new', methods=['GET', 'POST'])
def New_Item(cat_id):
    category = session.query(Category).filter_by(id=cat_id).one()
    if 'username' not in login_session:
        return redirect(url_for('login'))

    if category.user_id != login_session['user_id']:
        return redirect(url_for('Main_Index'))

    if request.method == 'GET':
        return render_template("new_catItem.html",
                               cat_id=cat_id)

    if request.method == 'POST':
        catItem = {}

        # fetch form data & assign it to corresponding Dict key
        catItem['name'] = request.form.get('catItem_name')
        catItem['desc'] = request.form.get('catItem_desc')
        # DB commit
        category_item = Cat_Item(name=catItem['name'],
                                 description=catItem['desc'],
                                 user_id=login_session['user_id'],
                                 category_id=cat_id)
        session.add(category_item)
        session.commit()
        return redirect(url_for('Show_Items', cat_id=cat_id))


@app.route('/category/<int:cat_id>/item/<int:item_id>', methods=['GET'])
def Show_Item(cat_id, item_id):
    # fetch all categories
    item = session.query(Cat_Item).filter_by(id=item_id).one()

    if 'username' not in login_session:
        return render_template("puplic_item.html",
                               cat_id=cat_id,
                               item=item)    

    user_auth = True
    if item.user_id != login_session['user_id']:     # Non Authorized user
        user_auth = False      # Flash error

    if request.method == 'GET':
        return render_template("cat_item.html",
                               cat_id=cat_id,
                               item=item,
                               username=bool_username(),
                               user_auth=user_auth)


@app.route('/category/<int:cat_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
def Edit_Item(cat_id, item_id):
    # fetch all Items
    item = session.query(Cat_Item).filter_by(id=item_id).one()
    # check if user logged in
    if 'username' not in login_session:
        return redirect(url_for('login'))

    if item.user_id != login_session['user_id']:          # Non Authorized user
        return redirect(url_for('Show_Items', cat_id=cat_id))     # Flash error

    if request.method == 'GET':
        # convert item to dict
        # item = to_dict(item)
        return render_template("edit_catItem.html",
                               cat_id=cat_id,
                               item=item)

    if request.method == 'POST':
        item = {}
        item['name'] = request.form.get('catItem_name')
        item['desc'] = request.form.get('catItem_desc')

        # data form validation should go here !

        # retrieving DB object to modify
        Citem = session.query(Cat_Item).filter_by(id=item_id).one()

        # updating Values
        Citem.name = item['name']
        Citem.description = item['desc']

        # Add & Commit changes
        session.add(Citem)
        session.commit()
        print("category Item has been edited successfully !")
        return redirect(url_for('Show_Items', cat_id=cat_id))


@app.route('/category/<int:cat_id>/item/<int:item_id>/delete',
           methods=['GET', 'POST'])
def Delete_Item(cat_id, item_id):
    # fetch all Items

    # check if user logged in
    if 'username' not in login_session:
        return redirect(url_for('login'))
    try:
        item = session.query(Cat_Item).filter_by(id=item_id).one()
    except:
        print("Trying to delete not existing row")
        return redirect(url_for('Show_Items', cat_id=cat_id))
    if item.user_id != login_session['user_id']:         # Non Authorized user
        return redirect(url_for('Show_Items', cat_id=cat_id))    # Flash error

    if request.method == 'GET':
        # fetch all categories
        item = session.query(Cat_Item).filter_by(id=item_id).one()
        # item = to_dict(item)
        return render_template("delete_catItem.html", cat_id=cat_id, item=item)

    if request.method == 'POST':
        try:
            item = session.query(Cat_Item).filter_by(id=item_id).one()
            session.delete(item)
            session.commit()
            return redirect(url_for('Show_Items', cat_id=cat_id))
        except:
            print("Trying to delete not existing row")
            return redirect(url_for('Show_Items', cat_id=cat_id))

# ----------------------------------------------------- #
# -------------- WebApp JSON API  --------------------- #
# ----------------------------------------------------- #


@app.route('/main/JSON', methods=['GET'])
def main_index_JSON():
    # fetch all categories
    cats = session.query(Category).all()
    # fetch latest added items .
    items = session.query(Cat_Item).order_by(desc(Cat_Item.date)).limit(10)
    # convert it to JSON type
    json_result = jsonify(categories=[i.serialize for i in cats],
                          top_items=[i.serialize for i in items])

    return json_result


@app.route('/category/<int:cat_id>/JSON', methods=['GET'])
def Show_Category_JSON(cat_id):
    if request.method == 'GET':
        # fetch latest added items .
        cat = session.query(Category).filter_by(id=cat_id).one()

        return jsonify(item=cat.serialize)


@app.route('/category/<int:cat_id>/items/JSON', methods=['GET'])
def Show_Items_JSON(cat_id):
    if request.method == 'GET':
        # fetch latest added items .
        items = session.query(Cat_Item).filter_by(category_id=cat_id).all()
        # convert it to Dict type
        json_result = jsonify(items=[i.serialize for i in items])
        return json_result


@app.route('/category/<int:cat_id>/item/<int:item_id>/JSON', methods=['GET'])
def Show_Item_JSON(cat_id, item_id):
    # user login Validation

    if request.method == 'GET':
        # fetch latest added items .
        item = session.query(Cat_Item).filter_by(id=item_id).one()
        # convert it to Dict type
        json_result = jsonify(item=item.serialize)
        return json_result


# <<<<<<<<<<<<<<<<<< Reserved for JSON post >>>>>>>>>>>>>>>>>>




@app.route('/category/<int:cat_id>/edit/JSON', methods=['GET', 'POST'])
def Edit_Category_JSON(cat_id):
    return render_template("edit_category.html")


@app.route('/category/<int:cat_id>/delete/JSON', methods=['GET', 'POST'])
def Delete_Category_JSON(cat_id):
    return render_template("delete_category.html")


@app.route('/category/<int:cat_id>/item/new/JSON', methods=['GET', 'POST'])
def New_Item_JSON(cat_id, item_id):
    return render_template("new_catItem.html")


@app.route('/category/<int:cat_id>/item/<int:item_id>/edit/JSON',
           methods=['GET', 'POST'])
def Edit_Item_JSON(cat_id, item_id):
    return render_template("edit_catItem")


@app.route('/category/<int:cat_id>/item/<int:item_id>/JSON',
           methods=['GET', 'POST'])
def Delete_Item_JSON(cat_id, item_id):
    return render_template("delete_catItem.html")


# ----------------------------------------------------- #
# ------------------ Running App  --------------------- #
# ----------------------------------------------------- #

if __name__ == '__main__':
    app.static_folder='static'
    app.secret_key = ''.join(random.choice(
                            string.ascii_uppercase + string.digits)
                            for x in range(32))
    app.debug = True
    app.run(host='0.0.0.0', port=app_port)
