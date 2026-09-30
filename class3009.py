#1
a = int(input())

if a <= 59:
    print("плохо :(")
elif a >= 60 and a <= 74:
    print ("удовлетворительно :)")
elif a >= 75 and a < 90:
    print ("хорошо :P")
elif a >= 90 and a < 100:
    print ("отлично :D")
elif a < 0 or a > 100:
    print("Некорректно :^")

#2

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print(" II четверть")
elif x < 0 and y < 0:
    print("III четверть")
elif x > 0 and y < 0:
    print("IV четверть")

#3

import random

s = random.randint(0, 1000)
while True:
    n = int(input())
    if n == s:
        print("ураа!!!!!  :D")

        break
    elif n < s:
        print("Больше")

    else:
        print("Меньше")


