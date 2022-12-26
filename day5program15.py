def extract_Consonent(s):
    n_Consonent=0
    for i in s:
        if i in '0123456789':
            n_Consonent+=1
    return n_Consonent

str1=input()
a=extract_Consonent(str1)
print(" N0 of Consonent in:'",str1,"'is",a)
