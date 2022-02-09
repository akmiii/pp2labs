#Problem J. 195834. Boris and Passwords

def hasBig(name):
    for bukva in name:
        if 'A' <= bukva <= 'Z':
            return True
    return False

def hasSm(name):
    for bukva in name:
        if 'a' <= bukva <= 'z':
            return True
    return False

def hasNum(name):
    for bukva in name:
        if '0' <= bukva <= '9':
            return True
    return False

n = int(input())
l = []
for i in range(n):
    login = input()
    if hasBig(login):
        if hasSm(login):
            if hasNum(login):
                l.append(login)
res = sorted(list(set(l)))
print(len(res))
for i in range(len(res)):
    print(res[i])


    
'''
for keys, value in d.items():
    
        d[login] = True
    else:
        d[login] = False
print(d)

cnt = 0
for key, value in d.items():
    if value == True:
        
print(cnt)
for key, value in sorted(d.items()):
    if value == True:
        print(key)
        '''

