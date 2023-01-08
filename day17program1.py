from random  import *
print (random())
print (randint(1,100))
print (uniform(1, 10))
items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)
items = [1,2,3,4,5,6,7,8,9,10]
x = sample(items, 3)
print("x=",x)
print(x[0])
y = sample(items, 4)
print(y)
