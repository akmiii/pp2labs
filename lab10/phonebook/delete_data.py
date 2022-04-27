import psycopg2
from lab10.racer.config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

upd = """
    DELETE FROM PhoneBook WHERE name = %s;
"""

name = input()

cursor.execute(upd, (name,))
print('Successfully deleted')

cursor.close()
db.commit()
db.close()