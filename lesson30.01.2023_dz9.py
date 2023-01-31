from random import randint
lst = [randint(0,10) for lst in range(randint(3,10))]
print(lst)
print ([lst[0]] + [lst[2]] + [lst[-2]])

