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

postgresql_func1 = """
    CREATE or REPLACE PROCEDURE delete(data varchar)
    as 
    $$
        BEGIN
            DELETE FROM Phonebook WHERE name = $1  or phone = $1; 
        END;
    $$ 
    LANGUAGE plpgsql;
"""

create_proc(postgresql_func1)

