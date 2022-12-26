def extract_Consonant(s):
    Consonant=''
    for i in s:
        if i in 'bcdfgtr':
            Consonant+=i
    return Consonant

str1=input()
a=extract_Consonant(str1)
print("Consonants in:'",str1,"'is",a)
