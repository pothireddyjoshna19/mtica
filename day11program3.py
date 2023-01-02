def findfrequency(s):
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
            frequencyDict[i] +=1
        else:
            frequencyDict[i]=1
    return frequencyDict
def formatoutput(d):
    for i in sorted(d):
        print(i,d[i])

n=int(input())
for i in range(n):
    inpstr=input()
    formatoutput(findfrequency(inpstr))
    
