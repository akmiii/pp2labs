#classic puzzle

heads = int(input())
legs = int(input())

def get_num(h, l):
    for i in range(h):
        for j in range(h):
            if i + j == h and 2*i + 4*j == l:
                return (i, j)

print(*get_num(heads, legs))