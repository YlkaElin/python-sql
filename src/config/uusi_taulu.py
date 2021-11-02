
import psycopg2
from config import config as config

def uusi_taulu():
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL= "CREATE TABLE naamataulu (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL, age int NOT NULL);"
        cur.execute(SQL)

        print(cur.rowcount, "record inserted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
    uusi_taulu()