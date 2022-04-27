import psycopg2
from lab10.racer.config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

num = int(input())

filter_1 = """
    SELECT * FROM Phonebook;
"""

filter_2 = """
    SELECT * FROM Phonebook WHERE city = %s;
"""

if num == 1:
    cursor.execute(filter_1)
    print('All usernames')
    print(*cursor.fetchall(), sep = '\n')
else:
    city_name = input('Enter the city: ')
    cursor.execute(filter_2, (city_name,))
    print(*cursor.fetchall(), sep = '\n')

cursor.close()
db.commit()
db.close()