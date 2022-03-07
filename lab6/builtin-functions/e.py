#returns True if all elements of the tuple are true

l = input().split()
print(bool(all((int(i) for i in l))))