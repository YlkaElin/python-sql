import psycopg2
from config import config as config

# Poista olemassa oleva rivi person taulusta. Poistettavan rivin id otetaan function parametrinä.
def person_delete(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL1 = "DELETE FROM certificates WHERE person_id=%s;"
        SQL2 = "DELETE FROM person WHERE person.id=%s;"
        val = (id,)
        cur.execute(SQL1,val)
        cur.execute(SQL2,val)

        print(cur.rowcount, "record deleted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


# Poista olemassa oleva rivi certificate taulusta. Poistettavan rivin id otetaan function parametrinä.

def certificates_delete(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "DELETE FROM certificates WHERE id = %s;"
        val = (id,)
        cur.execute(SQL, val)

        print(cur.rowcount, "record deleted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
    #person_delete(2)
    certificates_delete(1)