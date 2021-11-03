# Flask imports
import flask
from flask import Flask
from flask import render_template

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
    db.create_all()
    return flask.redirect(flask.url_for("login_page"))

@app.route("/login")
def login_page():
    return render_template("login.html")
    
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/user")
def user_page():
    return render_template("user.html")

app.run(
    debug=True
    # host="0.0.0.0",
    # port=int(os.getenv("PORT", 8080)),
)