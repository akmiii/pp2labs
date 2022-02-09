#Problem O. 147221. String calculator

d = {'ONE': '1', 'TWO': '2', 'THR': '3', 'FOU': '4', 'FIV': '5', 'SIX': '6', 'SEV': '7', 'EIG': '8', 'NIN': '9', 'ZER': '0'} 
dic1 = dict()
for k, v in d.items():
    dic1[v] = k 

s = input().split('+')
a = ''
l = []
for c in s:                       #пробегаемся по списку
    t = ""
    for i in range(0, len(c), 3): #пробегаемся по каждому слову в списку с шагом 3
        t += d[c[i:i+3]]          #переводим слова по дикш
        a = t
    l.append(int(a))              #"ONE" -> "1"
#print(l)
ans = sum(l)
ans = str(ans)
res = ""
for i in ans:
    res += dic1[i]
print(res)


        