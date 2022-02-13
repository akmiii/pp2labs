#game "Guess the number"

from random import randint
num = randint(1, 20)

def game():
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

print("Hello! What is your name?")
name = input()
print()
print("Well,", name+',', "I am thinking of a number between 1 and 20")
print("Take a guess.")
game()