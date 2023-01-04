inp=input()
temp=inp.split()
ans=[]
for i in temp:
    ans.append(len(i))
print(ans)
int=input()

ans=[len(i) for i in temp]
print(*ans)
