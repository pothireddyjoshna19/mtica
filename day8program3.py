def Factorial(num):
    assert(num>=0),"Factorial of negative number is not defined !"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-10))
except Exception as obj:
    print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)
