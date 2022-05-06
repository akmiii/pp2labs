import psycopg2
from config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

data = input()
cursor.execute("call delete(%s);", [data])

cursor.close()
db.commit()
db.close()