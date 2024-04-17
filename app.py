from flask import Flask, render_template, request,redirect,url_for,jsonify
import os
#import registerDB
from werkzeug.utils import secure_filename
#import matricule

app = Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True,host="172.16.0.103")