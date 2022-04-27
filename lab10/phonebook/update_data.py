import psycopg2
from lab10.config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

upd = """
    UPDATE Phonebook SET phone = %s WHERE name = %s;
"""

name = input()
number = input()

cursor.execute(upd, (number,name))
print('Successfully changed')

cursor.close()
db.commit()
db.close()