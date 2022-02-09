#Problem L. 194034. Open Closed

s = input()
l  = []
for i in s:
    if i == '(' or i == '{' or i == '[':
        l.append(i)
    else:
        if len(l) == 0:
            print('No')
            exit()
        elif i == ')' and l[-1] == '(':
            l.pop(-1)
        elif i == ']' and l[-1] == '[':
            l.pop(-1) 
        elif i == '}' and l[-1] == '{':
            l.pop(-1)
if len(l) == 0:
    print('Yes')
else:
    print('No')