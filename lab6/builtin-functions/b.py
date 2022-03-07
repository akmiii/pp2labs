#calculate the number of upper case letters and lower case letters

s = input()

lower = []
upper = []
for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
print(f'Number of lower case letters: {len(lower)}')
print(f'Number of upper case letters: {len(upper)}')