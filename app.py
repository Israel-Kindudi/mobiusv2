from flask import Flask, render_template, request,redirect,url_for,jsonify
import os
import psycopg2
from werkzeug.utils import secure_filename
#import matricule
import sqlite3
app = Flask(__name__)
# Get PostgreSQL database URL from environment variable
DATABASE_URL = os.environ['postgresql-dimensional-32478']
# SQLite database initialization
def create_table():
    conn = conn = psycopg2.connect(
    dbname="dp1aisj2jigt7",
    user="hjnnmurviuxgrd",
    password="0cd80e9d3f10ac459adbf8e80ae5518e19f7b83dfbb6d9b2f706df4194a9bd4a",
    host="ec2-34-193-110-25.compute-1.amazonaws.com"
)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            email TEXT,
            phone TEXT,
            message TEXT,
            services TEXT  -- Add a new field to store selected services
        )
    ''')

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        services = request.form.getlist('services[]')  # Retrieve selected services as a list

        
        # Save form data to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (email, phone, message, services) VALUES (?, ?, ?, ?)',
                       (email, phone, message, ', '.join(services)))
        conn.commit()
        conn.close()

        return 'Form submitted successfully!'
        
if __name__ == '__main__':
    app.run(debug=True,host="172.16.0.103")