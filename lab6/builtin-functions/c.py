#checks whether a passed string is palindrome or not

s = input()
a = ""
l = reversed(s)
for i in l:
    a += i
    
if s == a:
    print("Yes, it's a palindrome")
else:
    print("No, it's not")
