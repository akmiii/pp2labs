import psycopg2
from lab10.config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

create_table = '''
CREATE TABLE Phonebook(
    name VARCHAR PRIMARY KEY,
    phone VARCHAR(15),
    city VARCHAR(15)
);
'''
cursor.execute(create_table)

cursor.close()
db.commit()
db.close()