import sqlite3

db = sqlite3.connect("test.db")

cursor = db.cursor()
# cursor.execute("""
#     CREATE TABLE articles (
#       title text,
#       full text,
#       views integer,
#       avtor text
#     )
               
#                """)

cursor.execute("INSERT INTO articles VALUES ('Google is cool!', 'Google play', 100, 'admin')")

db.commit()


db.close()
# cursor = db.cursor()

# cursor.execute("""
#                """)