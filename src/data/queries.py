
import psycopg2
import src.config.config as config

def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        print("Connection created")
    except (Exception,
    psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
    connect()

