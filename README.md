# Catalogue WepApp
<br>
### Description:
This is Udacity 4th project of the Full Stack Web development Nano degree.
Creating an Item Catalogue that serves clients to show avaiable categories and items within each category.
**Authintication** by Providing Google & Facebook  ***OAuth2***  **Authorization** for each client to only *update ,  create  , delete* items only for their own created *category* or *item*.
**JSON** API endpoint `GET requests` to show availabel categories and items.

<br>
<hr>
<br>
### Contents:
- **`config.sh`** file which contains Linux commands to install needed modules and libs for the app to run.
- **`templates`** folder which contains all the **.html** files of the page
- **`static`** folder which contains all the styling **.css** files & images 
- **`database_setup.py`** script which is responsible for building the database required for this app to work
- **`db_seeds.py`** script for providing initial seeds to the database also used to display contents by `app.py`
- **`fb_client_secerts`** & **`g_client_secrets`** for 3rd party ( `facebook` - `google` ) Authintication 
- **`app.py`** Flask/Python3 WebApp  
<br>
<hr>
<br>
### Prerquisetes:
- Install ***Python3*** , Follow the link [here](https://www.python.org/downloads/).
- Install ***Flask*** form [here](http://flask.pocoo.org/docs/0.12/installation/).
- install ***SQLite*** , Follow the link [here](https://mislav.net/rails/install-sqlite3/).
- If you running on Linux Use config.sh to install and update other rquirements If not please install these ( [SQLAlchemy](https://www.pythoncentral.io/how-to-install-sqlalchemy/) - [oauth2client](https://pypi.python.org/pypi/oauth2client/4.0.0)  - [requests](http://docs.python-requests.org/en/master/)  -  [httplib2](https://pypi.python.org/pypi/httplib2/0.10.3)  ) 


<br>
<hr>
<br>
### Walkthrough `app.py`:
- Import required libs & modules 
	
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
		
> if import errors occur please install any missing module

- Flask `app` object 

		app = Flask(__name__) 
		app_port = 8000

- Connecting to the `Catalogue.db` 
		
		# Connect to Database and create database session
		engine = create_engine('sqlite:///Catalogue.db')
		Base.metadata.bind = engine

		DBSession = sessionmaker(bind=engine)
		session = DBSession()

- 3rd party Authintication section 
		
		@app.route('/login', methods=['GET'])
		@app.route('/fbconnect', methods=['POST'])
		@app.route('/gconnect', methods=['POST'])
		@app.route('/disconnect', methods=['GET'])
		
		
> disconnect from Google or Facebook by corresponding functions

- This section contains all the routes provided by the server
		
		# Main routes with CRUD 
		@app.route('/')
		@app.route('/main', methods=['GET'])
		
		@app.route('/category/new', methods=['GET', 'POST'])
		@app.route('/category/<int:cat_id>', methods=['GET'])
		@app.route('/category/<int:cat_id>/edit', methods=['GET', 'POST'])
		@app.route('/category/<int:cat_id>/delete', methods=['GET', 'POST'])
		
		@app.route('/category/<int:cat_id>/item/new', methods=['GET', 'POST'])
		@app.route('/category/<int:cat_id>/item/<int:item_id>', methods=['GET'])
		@app.route('/category/<int:cat_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
		@app.route('/category/<int:cat_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
		
		# JSON endpoint 
		@app.route('/main/JSON', methods=['GET'])
		@app.route('/category/<int:cat_id>/JSON', methods=['GET'])
		@app.route('/category/<int:cat_id>/items/JSON', methods=['GET'])
		@app.route('/category/<int:cat_id>/item/<int:item_id>/JSON', methods=['GET'])
		
- Main section 

		if __name__ == '__main__':
		    app.static_folder='static'
		    app.secret_key = ''.join(random.choice(
				            string.ascii_uppercase + string.digits)
				            for x in range(32))
		    app.debug = True
		    app.run(host='0.0.0.0', port=app_port)
> `port=app_port` number is used by browser in url `http://localhost:PORT_NUMBER/`

<br>		    
<hr>
<br>
### Running the App:
- Run **`database_setup.py`** to create the database and relations needed by the `app.py`
- Run **`db_seeds.py`** to create dummy inputs as database seeds 
- Finally, run **`app.py`**.and go to [localhost:8000/main](http://localhost:8000/main) & enjoy the app. 

<br>		    
<hr>
<br>
### How to Use :
- In `/main` you will find 
	- `login`button to redirect to login page.
	- `add new category` button to redirect to creat new category
> Only logged in user can add new category
	
	- All the available *categories* will be shown along with latest 10 *items* add by users

- In each **Category** list of *items* within will be available to display 
> Only Authorized users will be able to `Edit` or `Delete` the category

- In each **Item** you can display its description by clicking it
> Only Authorized users willbe able to `Edit` or `Delete` and Item

- any Edit, Delete or Add new (item/category), user must be logged in. Any action trying to do any of the previous will redirect to `/main` or `/login`.