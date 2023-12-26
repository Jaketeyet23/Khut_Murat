import random


A = random.randrange(50,100)
B = random.randrange(1,A)
print('A = ', A)
print('B = ', B)

r = A - B
while r >= B:
    r -= B
print("Остаток: ", r)