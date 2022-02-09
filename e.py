#Problem E. 187639. XOR in an array

arr = [int(i) for i in input().split()] #введеные числа входят в лист арр
#print(arr)
if len(arr) == 1:       #для 5 теста: если длина листа арр = 1, то вводим значение в этот же лист
    x = int(input())
    arr.append(x)
    
l = []
res = []
for i in range(arr[0]): #num[0] === len(arr), так как певрое число мы занесли в лист арр[0]
    l.append(arr[1]+2*i)
#print(l)

if len(l) == 1:
    print(l[0])
    exit()

for i in range(len(l)-1):
    res.append(l[i]^l[i+1])
    l[i+1] = res[i]
print(res[len(res)-1])