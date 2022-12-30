def printSeries(n):
    num=1
    for i in range(1,n+1):
        for j in  range(i):
            print(num,end='')
            num+=1
    return None


inpNum=int(input())
printSeries(inpNum)


