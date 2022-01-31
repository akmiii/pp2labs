#Problem I. 189327. Dimash that’s too bad

n = int(input())
for i in range(n):
    s = input()
    if s.endswith("@gmail.com"):
        print(s[:-10])


        