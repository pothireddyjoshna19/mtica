import time
inpNo =int(input("Enter a no: "))
start=time.time()
for i in range(inpNo):
    print("i=",i,"i^2=",i*i)
print("Time taken by Loop:",(time.time()-start)*100000)
