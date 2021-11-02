import psycopg2
from config import config as config

# Päivitä olemassa olevaa riviä person taulussa. Arvot otetaan function parametreinä.
def person_update(age, name):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "UPDATE person SET age = %s WHERE name = %s"
        val = (age, name)
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


# Päivitä olemassa olevaa riviä certificate taulussa. Arvot otetaan function parametreinä
def certificates_update(name, id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "UPDATE certificates SET name = %s WHERE id = %s"
        val = (name, id)
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
    #person_update(10, "RolliPeikko")
    certificates_update("GCP",4)