
import psycopg2
from config import config as config

# Lisää uusi rivi certificate tauluun siten, että arvot otetaan function parametreinä.
def certificate_lisaa_rivi(name, person_id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "INSERT INTO certificates (name, person_id) VALUES (%s,%s) RETURNING *;"
        val = (name, person_id)
        cur.execute(SQL, val)

        print(cur.rowcount, "record inserted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def person_lisaa_rivi(name, age, student):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "INSERT INTO person (name, age, student) VALUES (%s,%s, %s);"
        val = (name, age, student)
        cur.execute(SQL, val)

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
    #certificate_lisaa_rivi('Oddball',5)
    person_lisaa_rivi("Qwerty", 5, True)