string=input()

ans=[]
for i in string:
     if i in 'AEIOUaeiou':
          ans.append(i)
print(ans)


ans=[]
print(*len(ans))
