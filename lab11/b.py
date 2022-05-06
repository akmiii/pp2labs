import psycopg2
from config import params

def create_func(query):
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

# postgresql_func = """
#     DROP FUNCTION insert_many"""

postgresql_func = """
CREATE OR REPLACE FUNCTION insert_many(name varchar [], numbers varchar [], city varchar [], n int)
RETURNS TABLE(wrong_name varchar, wrong_number varchar, wrong_city varchar) AS $$
BEGIN
    FOR i in 1..n LOOP
        IF numbers[i] LIKE '87_________' THEN
            INSERT INTO Phonebook 
            VALUES (names[i], numbers[i]);
        ELSE 
            wrong_name:= names[i];
            wrong_number:= numbers[i];
            wrong_city:= city[i];
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
"""
create_func(postgresql_func)