import psycopg2
from config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

create_table = '''
CREATE TABLE snake(
    username VARCHAR(30),
    highscore INT NOT NULL,
    level INT NOT NULL
);
'''
cursor.execute(create_table)

# drop_table = '''DROP TABLE snake'''
# cursor.execute(drop_table)

cursor.close()
db.commit()
db.close()