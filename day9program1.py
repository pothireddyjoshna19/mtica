def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),"First argument should be string"
    assert isinstance(n,str),'Second argument should be int'
    for i in range(n,0,-1):
        print(ch*i)
    return None



inpch=input("Enter a character:")
inpNum=int(input("Enter a no:"))

print('-'*40)
try:
    printSeriesDecreasing(inpch,inpNum)
except AssertionError as ob:
    print(ob)
