from flask import Flask, render_template, request,redirect,url_for,jsonify
import os
import psycopg2
from werkzeug.utils import secure_filename

import matricule
import sqlite3
app = Flask(__name__)
# Get PostgreSQL database URL from environment variable
#DATABASE_URL = os.environ['postgresql-dimensional-32478']
# SQLite database initialization
conn = psycopg2.connect(
    dbname="d4jg1r8t17hpvo",
    user="hmbzjivfzhxhva",
    password="a0ab1c769cfaae679c0770f359ce01f9601f37627d7b251a5735ae9d96b12b6b",
    host="ec2-107-21-67-46.compute-1.amazonaws.com"
)

def create_table():
    
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER ,
            email TEXT,
            phone TEXT,
            message TEXT,
            services TEXT  -- Add a new field to store selected services
        )
    ''')
    conn.commit()

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
        id = matricule.unique_number
        
        # Save form data to the PostgreSQL database
        #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (id,email, phone, message, services) VALUES (%s, %s, %s, %s,%s)',
                       (id,email, phone, message, ', '.join(services)))
        conn.commit()
        #conn.close()

        return redirect(url_for('index'))
        
if __name__ == '__main__':
    create_table()
    app.run(debug=True,host="172.16.0.101")