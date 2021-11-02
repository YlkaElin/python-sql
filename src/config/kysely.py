
import psycopg2
from config import config

con = None
try:
    con = psycopg2.connect(**config())
    cursor = con.cursor()
    cursor.execute("SELECT * FROM person;")
    cursor.fetchone()

    cursor.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if con is not None:
        con.close()

