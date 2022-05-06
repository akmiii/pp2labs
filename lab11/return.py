import psycopg2
from config import params

try:
    db = psycopg2.connect(**params)

    cursor = db.cursor()
    #our procedure 
    cursor.callproc('filter')

    result = cursor.fetchall()
    for row in result:
        print("name = ", row[0])
        print("number = ", row[1])
        print("city = ", row[2])
        print('\n')
except (Exception) as error:
    print("ERROR:", error)
finally:
    if db:
        cursor.close()
        db.close()
        print("Connection with PostgreSQL is closed")