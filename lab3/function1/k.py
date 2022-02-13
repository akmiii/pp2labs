#palindrome

s = input()

def isPal(s):
    if s == s[::-1]:
        return True
    return False

print(isPal(s))