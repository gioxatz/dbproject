# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:32:48 2023

@author: gioxa
"""

from faker import Faker
import random
import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
import mysql.connector

fake = Faker('el_GR') # Use Greek language for fake data

# Generate random data for 10 books
for i in range(10):
    ISBN = random.randint(1000000000000, 9999999999999) # 13-digit ISBN
    schoolID = random.randint(1, 3)
    title = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
    publisher = fake.company()
    num_pages = random.randint(50, 500)
    lang = fake.language_code()
    copies = random.randint(1, 10)
    image = fake.image_url()
    summary = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    available_copies = copies

    # Print the generated data
    print(f"INSERT INTO books (ISBN, schoolID, title, publisher, num_pages, lang, copies, image, summary, available_copies) VALUES ({ISBN}, {schoolID}, '{title}', '{publisher}', {num_pages}, '{lang}', {copies}, '{image}', '{summary}', {available_copies});")


from flask import Flask, render_template, request, redirect, url_for
#from flask_mysqldb import MySQL

db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="lib1"
    )

cur = db.cursor()
query = """Select s.name, s.city, d.name, d.surname, h.firstname, h.lastname
    from schools s join school_director d on schoolID = d.schoolID
    join handler h on h.schoolID = s.schoolID
    """
cur.execute(query)
data = cur.fetchall()
cur.close()
 



@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE email = %s AND password = %s", (email, password))
    admin = cur.fetchone()
    cur.close()
    if admin is None:
        return render_template('adminlogin.html', message='Invalid email or password')
    else:
        return redirect(url_for('admin', adminID=admin[0]))

@app.route('/admin/<int:adminID>')
def admin(adminID):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE adminID = %s", (adminID,))
    admin = cur.fetchone()
    cur.close()
    if admin is None:
        return render_template('adminlogin.html', message='Please log in first')
    else:
        return render_template('admin.html', admin=admin)

if __name__ == '__main__':
    app.run(debug=True)



#-------------------
@app.route('/adminloginauth', methods=['GET', 'POST'])
def adminlogin():
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="lib1"
    )
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        query = "SELECT admin_id, name, surname, email, username from admin where username=%s AND password=%s"
        cursor.execute(query, (username, password))
        admin = cursor.fetchone()
        if admin:
            session['admin_id'] = admin[0]
            session['admin_name'] = admin[1] + " " + admin[2]
            return redirect('/admin')
        else:
            error = "Invalid username or password"
            return render_template('admin_login.html', error=error)
    else:
        return render_template('admin_login.html')
    
@app.route('/admin')
def admin():
    
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="lib1"
    )
    if 'admin_id' in session:
        admin_id = session['admin_id']
        admin_name = session['admin_name']
        cursor = mydb.cursor()
        query = "SELECT name, surname, email, username FROM admin WHERE adminID=%s"
        cursor.execute(query, (admin_id,))
        admininfo = cursor.fetchone()
        return render_template('admin.html', admin=admininfo)
    else:
        return redirect('/admin_login')
    