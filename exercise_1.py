import math
import random

#függvényt létrehozni 99 és 49*-re és először a maint megírni!
for i in range(10):
    a = random.randint(1, 99)
    g = 100
    while a != g:
        g = int(input("Enter an integer from 1 to 99: "))
        if g < a:
            print("guess is low")
        elif g > a:
            print("guess is high")
        else:
            break
    print("you guessed it!")
 
b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")


def main():
    pass

if __name__ == '__main__':
    main()