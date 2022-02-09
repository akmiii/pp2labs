#Problem M. 197032. Important dates

l = []
while (True):
    s = input().split()     #dd mm year
    date = [i for i in s]
    if date[0] == '0':      
        break
    else:
        d = date[2] + ' ' + date[1] + ' ' + date[0]
        l.append(d)         #year mm dd

#print(sorted(l))
for i in sorted(l):
    dd = i.split()
    print(dd[2], dd[1], dd[0])  #dd mm year
