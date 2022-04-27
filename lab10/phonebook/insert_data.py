import psycopg2, csv
from lab10.config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

ins = """
    INSERT INTO Phonebook VALUES(%s, %s, %s);
"""

with open("phone.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            pass
            #cursor.execute(ins, row)
try:
    name = input("Enter the name: ")
    phoneNumber = input("Enter the number: ")
    city = input("Enter the city: ")
    cursor.execute(ins, (name,phoneNumber,city))
    print('Successfully added')
except:
    print('The username is already existed')

cursor.close()
db.commit()
db.close()