import psycopg2
from config import params

def create_proc(query):
    try:
        #Connection to db
        db = psycopg2.connect(**params)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

    except (Exception) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if db:
            cursor.close()
            db.close()
            print("Connection with PostgreSQL is closed")
#insert:
# postgresql_func1 = """
# DROP PROCEDURE inserting"""
# postgresql_func2= """
# DROP PROCEDURE updating"""
postgresql_func1 = """
    CREATE or REPLACE PROCEDURE inserting(name varchar, phonenumber varchar, city varchar)
    as 
    $$
        BEGIN
            INSERT INTO Phonebook(name, phone, city) VALUES ($1, $2, $3);
        END; 
    $$ 
    LANGUAGE plpgsql;  
"""
postgresql_func2 = """
    CREATE or REPLACE PROCEDURE updating(name varchar, n_phone varchar, n_city varchar)
    as
    $$
        BEGIN
            UPDATE Phonebook 
            SET phone = $2, city = $3
            WHERE Phonebook.name = $1;
        END; 
    $$ 
    LANGUAGE plpgsql;  
"""
create_proc(postgresql_func1)
create_proc(postgresql_func2)