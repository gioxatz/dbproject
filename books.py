# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:22:09 2023

@author: gioxa
"""

#!/usr/bin/env python3
import cgi
import cgitb
import mysql.connector

cgitb.enable()

# establish connection to the database
cnx = mysql.connector.connect(user='root', password='', database='lib1')
cursor = cnx.cursor()

# get schoolID from the form
form = cgi.FieldStorage()
schoolID = form.getvalue('schoolID')

# retrieve books for the selected school
query = "SELECT * FROM books WHERE schoolID = %s"
cursor.execute(query, (schoolID,))
books = cursor.fetchall()

# print HTML page with list of books
print("Content-type: text/html\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>List of Books</title>")
print("<link rel='stylesheet' type='text/css' href='style.css'>")
print("</head>")
print("<body>")
print("<h1>List of Books</h1>")
print("<table>")
print("<tr>")
print("<th>ISBN</th>")
print("<th>Title</th>")
print("<th>Publisher</th>")
print("<th>Number of Pages</th>")
print("<th>Language</th>")
print("<th>Copies</th>")
print("<th>Summary</th>")
print("</tr>")
for book in books:
    print("<tr>")
    print("<td>{}</td>".format(book[0]))
    print("<td>{}</td>".format(book[2]))
    print("<td>{}</td>".format(book[3]))
    print("<td>{}</td>".format(book[4]))
    print("<td>{}</td>".format(book[5]))
    print("<td>{}</td>".format(book[6]))
    print("<td>{}</td>".format(book[8]))
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")

# close the database connection
cursor.close()
cnx.close()
