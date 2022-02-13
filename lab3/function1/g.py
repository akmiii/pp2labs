#3 next to a 3 

numbers = list(map(int, input().split()))

def has_33(n):
    for i in range(len(n)-1):
        if n[i] == 3 and n[i] == n[i+1]:
            return True
    return False

print(has_33(numbers))