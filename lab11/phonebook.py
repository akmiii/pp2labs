import psycopg2
from config import params

db = psycopg2.connect(**params)

cursor = db.cursor()

def check(name):
    select = '''
            SELECT phone FROM phonebook WHERE name = %s;
    '''
    cursor.execute(select, [name])
    arr = cursor.fetchone()
    if arr == None: 
        return True
    return False

def check_phone(num):
    if(number.find('8707') == 0 and len(number) == 11):
        return number
    elif(number.find('8747') == 0 and len(number) == 11):
        return number
    elif(number.find('8775') == 0 and len(number) == 11):
        return number
    elif(number.find('8708') == 0 and len(number) == 11):
        return number
    elif(number.find('8777') == 0 and len(number) == 11):
        return number
    elif(number.find('8778') == 0 and len(number) == 11):
        return number

    print("Sorry, it seems you made a mistake in your phone number, can you write it again?")
    num = input()
    return check_phone(num)
    
command = input("Your query: ")

if command == 'return':
    cursor.callproc('filter')

    result = cursor.fetchall()
    for row in result:
        print("name = ", row[0])
        print("number = ", row[1])
        print("city = ", row[2])
        print('\n')
if command == 'insert new user':
    print("How many people you want to add?")
    n = int(input())
    for _ in range(0, n):
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        number = check_phone(number)
        city = input("Enter the city: ")
        if(check(name)): 
            cursor.execute("call inserting(%s, %s, %s);", (name, number, city))
        else:
            cursor.execute("call updating(%s, %s, %s);", (name, number, city))

if command == 'pagination':
    offset = int(input("Enter the offset: "))
    limit = int(input("Enter the limit: "))
    print('\n')
    
    cursor.callproc('pagination', (offset, limit))

    result = cursor.fetchall()
    for row in result:
        print("name = ", row[0])
        print("number = ", row[1])
        print("city = ", row[2])
        print('\n')
if command == 'delete':
    data = input("Enter the deleting data: ")
    cursor.execute("call delete(%s);", [data])

print("Connection with PostgreSQL is closed")