def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None


inpch=input("Enter a character:")
inpNum=int(input("Enter a no:"))
printSeriesIncreasing(inpch,inpNum)
print('-'*40)
printSeriesDecreasing(inpch,inpNum)
