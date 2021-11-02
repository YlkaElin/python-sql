
import psycopg2
import config as config

def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
    except (Exception,
    psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()