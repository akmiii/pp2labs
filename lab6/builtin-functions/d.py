import time

t = int(input())
s = int(input())
time.sleep(s//1000)
print(f"Квадратный корень из {t} после {s} миллисекунд равен {t ** 0.5}.")