import math
from random import randint, choice, sample, shuffle


# math
r = 100
print(2 * r * math.pi)
print((r ** 2) * math.pi)
print(math.pow(r, 2) * math.pi)

x1 = 10
x2 = 20
y1 = 20
y2 = 50
l = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(l)

print(math.factorial(20))

# Random
print(randint(0, 100))

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
print(sample(players, 3))

cards = ['6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
print(cards)
shuffle(cards)
print(cards)

