from math import sqrt, pi
from random import randint


def gram_to_ounces(n):
    return(n * 28.3495231)

def getTem(n):
    return (5/9 * (n-32))

def get_num(h, l):
    for i in range(h):
        for j in range(h):
            if i + j == h and 2*i + 4*j == l:
                return (i, j)
def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
def filter(num):
    arr = []
    for i in num:
        if isPrime(i):
            arr.append(i)
    return(arr)
def getPerm(a, start, end):
    if start == end:
        print(''.join(a))
    else:
        for i in range(start, end+1):
            a[start], a[i] = a[i], a[start]
            getPerm(a, start+1, end)
            a[start], a[i] = a[i], a[start]     

def getRev(s):
    l = []
    for i in s:
        if i == len(s):
            return
        else:
            l.append(i)
    return(l[::-1])

def has_33(n):
    for i in range(len(n)-1):
        if n[i] == 3 and n[i] == n[i+1]:
            return True
    return False

def spy_game(nums):
    l = []
    for i in nums:
        if i == 0 or i == 7:
            l.append(i)
    if l[0] == 0 and l[1] == 0 and l[2] == 7:
        return True
    return False

def getVol(r):
    return (4*pi*(r**3) / 3)

def uniq(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

def isPal(s):
    if s == s[::-1]:
        return True
    return False

def hist(l):
    res = []
    for i in range(len(l)):
        res.append('*'*l[i])
    return res

def game():
    num = randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print()
    print("Well,", name+',', "I am thinking of a number between 1 and 20")
    print("Take a guess.")
    cnt = 0
    a = int(input())
    while a != num:
        if a > num:
            cnt += 1
            print()
            print("Your guess is too high.", "Take a guess.", sep = '\n')
            a = int(input())
            continue
        elif a < num:
            cnt +=1
            print()
            print("Your guess is too low.", "Take a guess.", sep = '\n')
            
            a = int(input())
            continue
    else:
        print("Good job,", name,"! You guessed my number in", cnt+1, "guesses!")  