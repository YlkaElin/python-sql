
import psycopg2
from config import config as config

#Hae kaikki person taulun rivit ja tulosta ne.
def hae_kaikki():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute("SELECT * FROM person")
        #print("Kaikki tiedot: ", cursor.rowcount)
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 2. Hae person taulun sarakkeiden nimet ja tulosta ne.
def sarakkeiden_nimet():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'person'"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 3. Hae certificate taulun sarakkeiden nimet, sekä rivit ja tulosta ne.
def certificate_sarakkeet():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute("SELECT * FROM certificates;")
        row = cursor.fetchone()

        num_fields = len(cursor.description)
        field_names = [i[0]
            for i in cursor.description ]
        print(field_names)

        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 4. Hae kaikki AWS sertifikaattien omistajat.
def certificate_hae_gcp():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute("SELECT person.name, certificates.name FROM person INNER JOIN certificates ON person.id = certificates.person_id WHERE certificates.name='GCP';")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def summaa_iat():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute("SELECT SUM(age) FROM person;")
        print(cursor.fetchone())
        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == '__main__':
    #hae_kaikki()
    #sarakkeiden_nimet()
    #certificate_sarakkeet()
    #certificate_hae_gcp()
    summaa_iat()