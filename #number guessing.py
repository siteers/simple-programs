#number guessing
import random

print('Guess number!')

y = random.randint(0,10)

while True:
    x = input("type number 1-10")
    x = int(x)
    if x == y:
        print('Congratulations!')
        break
    if x != y:
        print('Try again!')