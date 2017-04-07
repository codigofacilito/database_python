#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install MySQL-python
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'dbpython' #s

USERSTABLE = """CREATE TABLE users ( 
         id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(50) NOT NULL,
         password VARCHAR(50) NOT NULL
         )"""

DROPUSERTABLE = "DROP TABLE IF EXISTS `users`"
SHOWTABLES = "SHOW TABLES"

INSERTUSER = "INSERT INTO users (username, password) VALUES( '{username}', '{password}' );"
SELECTUSER = "SELECT * FROM users WHERE Id = {id}"

if __name__ == '__main__':
  connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
  cursor = connection.cursor()
  
  cursor.execute(DROPUSERTABLE)
  cursor.execute(USERSTABLE)
  cursor.execute(SHOWTABLES)
  tables = cursor.fetchall()
  
  for table in tables:
    print(table[0])
  
  query = INSERTUSER.format(username='codigofacilito', password='codigo123')
  print(query)
  
  try:
    cursor.execute(query)
    connection.commit()
  except:
      db.rollback()

  query = SELECTUSER.format(id=1)
  cursor.execute(query)
  
  results = cursor.fetchall()
  user = results[0]
    
  print("username : " + user[1])
  print("password : " + user[2])

  connection.close()
  



