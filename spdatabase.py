import os

#os.system("pip install psycopg2")


import psycopg2


conn = psycopg2.connect(database="emlvwsts",
                        host="mahmud.db.elephantsql.com",
                        user="emlvwsts",
                        password="QZplqRjrPc5y3n2cf6VwgdvhcUZJ1hXV",
                        port="5432")

cursor = conn.cursor()

def create_table():
  cursor.execute("DROP TABLE IF EXISTS PHLinks")

  sql ='''CREATE TABLE PHLinks(
   LINK VARCHAR(255) NOT NULL
)'''

  cursor.execute(sql)
  print("Table created successfully........")
  conn.commit()


def insert_db(lin):
    query = "INSERT INTO PHLinks (url) VALUES('{}')".format(lin)
    cursor.execute(query)
    conn.commit()

def read_db():
   cursor.execute("SELECT * FROM PHLinks")
   data = cursor.fetchall()
   return data

def delall_db(name):
    cursor.execute(f"DELETE FROM {name}")
    conn.commit()




if 1==1:
  #create_table()
  #insert_db("www.google.com","Google")
  for t in read_db():
      if "Goo" in t:
         print(t)