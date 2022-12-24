def checkPrimeNumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
       return num
    for i in range(2,num):
        if num%i==0:
           return 0
    return num
lst=[]
start=int(input())
stop=int(input())
for i in range(start,stop+1):
    if checkPrimeNumber(i):
        lst.append(i)
print(*lst)
print(len(lst))
