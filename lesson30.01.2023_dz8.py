from random import randint
lst = [randint(0,10) for _ in range(randint(0,10))]
print(lst)
print((sum(lst[::2])) * lst[-1])