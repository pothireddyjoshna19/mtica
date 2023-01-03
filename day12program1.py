def printSeries(s,n):
     sp='.'
     for i in range(0,n):
        print(sp*(n-i-1)+s*(2*i+1)+sp*(n-i-1))
     return None
inps=input()
inpNum=int(input())
printSeries(inps,inpNum)
