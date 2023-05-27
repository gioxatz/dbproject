# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:35:34 2023

@author: gioxa
"""

import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
import mysql.connector
from faker import Faker
import numpy as np

fake = Faker()



# for i in range(1, 81):
    # print("UPDATE users SET active = 1 WHERE userID = ", i , ";")
    
import random
import pandas as pd

df = pd.read_csv(r'\Users\gioxa\Downloads\books_new.csv')
data = pd.DataFrame(df, columns=['Title', 'Author', 'Genre', 'Subgenre', 'Height', 'Publisher'])
print(data['Title'][1])
isbns = random.randint(9782081011249, 9783081011249)
#isbn = 9782081011249
isbn = 9782081011312

schoolID = random.randint(1,3)
copies = random.randint(1,6)
urls = ['https://static.eudoxus.gr/books/preview/78/cover-77111878.jpg', 'https://static.eudoxus.gr/books/preview/https://static.eudoxus.gr/books/28/cover-77114128.jpg', 'https://static.eudoxus.gr/books/preview/https://static.eudoxus.gr/books/60/cover-86183160.jpg', 'https://static.eudoxus.gr/books/preview/25/cover-102075125.jpg', 'https://static.eudoxus.gr/books/preview/61/cover-32761.jpg', 'https://static.eudoxus.gr/books/preview/https://static.eudoxus.gr/books/91/cover-77108691.jpg', 'https://static.eudoxus.gr/books/preview/https://static.eudoxus.gr/books/68/cover-86055468.jpg', 'https://static.eudoxus.gr/books/preview/53/cover-102075353.jpg', 'https://static.eudoxus.gr/books/preview/04/cover-112692104.jpg']

url = random.choice(urls)

#10, 55
subj = ['Technology', 'Nonfiction', 'Philosophy']
 # INSERT INTO has_subject values(9780809501632,  1);



a = """
9780809501632, 1
9780081011249, 1
9780078022159, 2
9789603322092, 3
9789607309471, 2
 9782081011249 , 2
 9782081011250 , 2
9782081011294 , 1
9782081011295 , 1
 9782081011296 , 1 
9782081011297 , 3
9782081011298 , 1
 9782081011299 , 3
9782081011300 , 3 
9782081011301 , 2
9782081011302 , 1
9782081011303 , 2
9782081011304 , 1
9782081011305 , 1
 9782081011306 , 2
 9782081011307 , 3
 9782081011308 , 3
9782081011309 , 2
 9782081011310 , 1
9782081011311 , 1
 9782081011312 , 3
 9782081011313 , 3
9782081011314 , 3 
 9782081011315 , 1
9782081011316 , 3
9782081011317 , 2
9782081011318 , 2
9782081011319 , 2
9782081011320 , 2
9782081011321 , 1

"""

x = a.split("\n")
print(x[1])
# u = 20
# for i in range(156, 193):
#     print("INSERT INTO is_author  VALUES (", isbn, ", ", u ,");")
#     if u == 54:
#         u = 12
#     else:
#         u+=1
#     isbn+=1
    
xs = ['2, "Δεν θα σας το συνιστούσα"',  '3, "Μέτριο βιβλίο"', '4, "Καλό βιβλίο"', '5, "Εξαιρετικό βιβλίο"']
# for i in range (20):
#     schoolID = random.randint(20)
#     copies = random.randint(1,6)
#     url = random.choice(urls)
#     print("INSERT INTO books VALUES (", isbn, ",", schoolID, ", '", data['Title'][i], "','", data['Publisher'][i%150], "',", data['Height'][i], ", 'English', ", copies, ",'", url, "', '", 10*data['Title'][i],"' , default);")
#     isbn+=1
    
isbn = 9782081011265

for i in range (20):
    schoolID = random.randint(20, 80)
    copies = random.randint(9782081011250,9782081011348)
    url = random.choice(xs)
    print("INSERT INTO review VALUES (default, ", isbn, ",", schoolID, ", default, " ,url,  ");")
    isbn+=2
    
x ="""
INSERT INTO review VALUES (default,  9782081011266 , 77 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011268 , 50 , default,  4, "Καλό βιβλίο" );
INSERT INTO review VALUES (default,  9782081011270 , 48 , default,  5, "Εξαιρετικό βιβλίο" );
INSERT INTO review VALUES (default,  9782081011272 , 58 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011274 , 43 , default,  5, "Εξαιρετικό βιβλίο" );
INSERT INTO review VALUES (default,  9782081011276 , 64 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011278 , 48 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011280 , 76 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011282 , 72 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011284 , 37 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011286 , 25 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011288 , 37 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011290 , 80 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011292 , 53 , default,  4, "Καλό βιβλίο" );
INSERT INTO review VALUES (default,  9782081011294 , 30 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011296 , 70 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011298 , 33 , default,  4, "Καλό βιβλίο" );
INSERT INTO review VALUES (default,  9782081011300 , 45 , default,  3, "Μέτριο βιβλίο" );
INSERT INTO review VALUES (default,  9782081011302 , 73 , default,  2, "Δεν θα σας το συνιστούσα" );
INSERT INTO review VALUES (default,  9782081011304 , 28 , default,  4, "Καλό βιβλίο" );
"""

query1 = """
             select a.name, hs.subID from author a join is_author isa on isa.authorID = a.authorID
             join has_subject hs on hs.ISBN = isa.ISBN where hs.subID = 14"""
query2 = """ union
             select u.name, u.surname from users u
             join teacher t on t.userID = u.userID
             join has_loan hs on hs.userID = t.userID
             join loans l on l.loanID = hs.loanID 
             join has_subject hass on hass.ISBN = l.ISBN 
             WHERE DATEDIFF(current_date, l.loan_date) < 366
             and hass.subID = 14
        """
print(query1 + query2)
# for i in range(17, 31):
#     year = random.randint(1965, 2000)
#     month = random.randint(1, 12)
#     day = random.randint(1,30)
#     print("UPDATE users SET birthdate = ('", year, '-', month, '-', day, "') where userID = ", i, ';', sep = "" )

# print(random.randint(1965, 1998))

db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="lib1"
    )

userID = 50
cur = db.cursor()
query = """
          SELECT s1.subID AS subject1, s2.subID AS subject2, COUNT(*) AS loan_count
FROM has_subject hs1
JOIN has_subject hs2 ON hs1.ISBN = hs2.ISBN AND hs1.subID < hs2.subID
JOIN subjects s1 ON hs1.subID = s1.subID
JOIN subjects s2 ON hs2.subID = s2.subID
JOIN loans hl ON hl.ISBN = hs1.ISBN
GROUP BY hs1.subID, hs2.subID
ORDER BY loan_count DESC
LIMIT 3;
        """
cur.execute(query)
stu_rs = cur.fetchall()
cur.close()
print(stu_rs)
    



# Close the cursor and connection

# subs, auths = [], []
# cu = db.cursor()
# query = """
# SELECT subject FROM subjects
# """
# cu.execute(query)
# subjects1 = cu.fetchall()
# for sie in subjects1:
#     subs.append(sie[0])
# cu.close()
# cu = db.cursor()
# query = """
#       SELECT DISTINCT name FROM author join is_author on author.authorID = is_author.authorID
#       """
# cu.execute(query)
# auth = cu.fetchall()
# for aur in auth:
#    auths.append(aur[0])
# cu.close()
# print(auths)
# print(subs)
# cur = db.cursor()
# query = """
#     SELECT userID FROM users ORDER BY userID DESC LIMIT 1
#     """
# cur.execute(query)
# data = cur.fetchone()[0]
# print(data)
# cur.close()
 
# join handler h on h.schoolID = s.schoolID 
#  , h.firstname, h.lastname


# user1

# if user is None:
#         return render_template('teacher_login.html', message='Please log in first')
#     else:
#         if request.method == 'POST':
#             selected_subject_id = request.form['subject_id']
#             cursor = db.cursor()
#             query = """
#             SELECT b.ISBN, b.title, b.available_copies, b.schoolID 
#             FROM books b 
#             JOIN has_subject hs ON b.ISBN = hs.ISBN 
#             WHERE hs.subID = %s AND b.schoolID = %s
#             """
#             cursor.execute(query, (selected_subject_id, user[5]))
#             books = cursor.fetchall()
#             cursor.close()
#             return render_template('books.html', books=books)
#         else:
#             # cu = db.cursor()
#             # query = """
#             # SELECT * FROM subjects
#             # """
#             # cu.execute(query)
#             # subjects = cu.fetchall() 
#             # cu.close()
#             return render_template('teacher.html', user=user, subjects=subjects)

#     if user is None:
#         return render_template('teacher_login.html', message='Please log in first')
#     else:
#         if request.method == 'POST':
#             selected_subject_id = request.form['subject_id']
#             return redirect(url_for('books', school_id=user[5], subject_id=selected_subject_id))
#         else:
#             return render_template('teacher.html', user=user, subjects=subjects)