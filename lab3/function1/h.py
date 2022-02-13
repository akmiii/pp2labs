#007 in order

numbers = list(map(int, input().split())) # 1 2 4 0 0 7 5

def spy_game(nums):
    l = []
    for i in nums:
        if i == 0 or i == 7:
            l.append(i)
    if l[0] == 0 and l[1] == 0 and l[2] == 7:
        return True
    return False
    

print(spy_game(numbers))

