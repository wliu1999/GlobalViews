# Flask imports
import flask
from flask import Flask
from flask import render_template

# Login tools
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_required
from flask_login import login_user
from flask_login import current_user

# Database imports
from flask_sqlalchemy import SQLAlchemy

# API tools
import os

# Flask app initialization and db setup
app = Flask(__name__)
db = SQLAlchemy(app)

# App Routing
@app.route("/")
def index():
    #Probably doesn't need to be modified
    return flask.redirect(flask.url_for("login_page"))

@app.route("/login")
def login_page():
    # Expected input: none (redirects only)
    # Expected user input: Click on google login button
    # Expected output: Redirect user to Google's authorization endpoint, where they will log in

    # Probably just a button to login with
    return render_template("login.html")

@app.route("/login/callback")
def callback():
    # Expected input: Authorization code from google
    # Expected output: 
        # If user is authenticated properly, send them to the home endpoint
            # If they are not already in the database, add their info to the database
        # If user is not authenticated properly, send them back to the login endpoint

    # Authentication happens here!
    
@app.route("/home")
def home_page():
    # Expected input: none (redirects only)
    # Expected user input: click on country, click on logout button
    # Expected outputs: 
        # Selected country (redirect to user endpoint)
            # Url should be in format "/user/country=USA"
        # Log Out (redirect to logout endpoint)
    return render_template("home.html")

@app.route("/user")
def user_page():
    # Expected input: Selected country
        # Input should be received through url in format "user/country=USA"
    # Expected user input: click on video, click on logout button, click on home button
    # Expected outputs
        # Video (Redirect to youtube)
        # Home (redirect to home endpoint)
        # Log Out (redirect to logout endpoint)
    # Url should come in format "/user/country=USA"
    
    # Load user info

    # Load country video info
        # Youtube API calls here
            # Expected input for API call: country name (string)
            # Expected output: the top 5 trending videos in that country
                # This should be a list of urls extracted from a JSON response.

    # Pass info to render in page
    return render_template("user.html")

@app.route("/logout")
def logout():
    # Expected input: none
    # Expected output: redirect user to login endpoint
    
    # Log out user here


#Initialize db and run application
db.create_all()
app.run(
    debug=True
    # host="0.0.0.0",
    # port=int(os.getenv("PORT", 8080)),
)