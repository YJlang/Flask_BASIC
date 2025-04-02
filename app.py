from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL 연결 설정
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="wnsgk677400",
    database="practice"
)

# 데이터베이스와 테이블 생성
cursor = db.cursor()
#cursor.execute("CREATE DATABASE IF NOT EXISTS flask_db")
cursor.execute("USE practice")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
""")
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect(url_for('users'))

@app.route('/users')
def users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True) 