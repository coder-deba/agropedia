import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, time as dt_time, timedelta


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Welcome Page"""
    return render_template("index.html")

@app.route("/pests")
def pests():
    """Crop pests page"""
    return render_template("pests.html")

@app.route("/diseases")
def diseases():
    """Crop pests page"""
    return render_template("diseases.html")

@app.route("/crops")
def rice():
    """Crop pests page"""
    return render_template("crops.html")

@app.route("/wheat")
def wheat():
    """Crop pests page"""
    return render_template("wheat.html")

@app.route("/maize")
def maize():
    """Crop pests page"""
    return render_template("maize.html")

@app.route("/sorghum")
def sorghum():
    """Crop pests page"""
    return render_template("sorghum.html")

@app.route("/barley")
def barley():
    """Crop pests page"""
    return render_template("barley.html")

@app.route("/pearl millet")
def pearl_millet():
    """Crop pests page"""
    return render_template("pearl millet.html")

@app.route("/finger millet")
def finger_millet():
    """Crop pests page"""
    return render_template("finger millet.html")

@app.route("/foxtail millet")
def foxtail_millet():
    """Crop pests page"""
    return render_template("foxtail millet.html")

@app.route("/proso millet")
def proso_millet():
    """Crop pests page"""
    return render_template("proso millet.html")

@app.route("/barnyardmillet")
def barnyard_millet():
    """Crop pests page"""
    return render_template("barnyardmillet.html")

@app.route("/greengram")
def greengram():
    """Crop pests page"""
    return render_template("greengram.html")

@app.route("/blackgram")
def blackgram():
    """Crop pests page"""
    return render_template("blackgram.html")

@app.route("/bengalgram")
def bengalgram():
    """Crop pests page"""
    return render_template("bengalgram.html")

@app.route("/pigeonpea")
def pigeonpea():
    """Crop pests page"""
    return render_template("pigeonpea.html")

@app.route("/horsegram")
def horsegram():
    """Crop pests page"""
    return render_template("horsegram.html")

@app.route("/cowpea")
def cowpea():
    """Crop pests page"""
    return render_template("cowpea.html")

if __name__ == "__main__":
    app.run(debug=True)