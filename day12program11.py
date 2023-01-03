class student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
          self.name=name
          self.rollno=rollno
    def displaystudent(self):
        print('Name : '+self.name.title()+'\nRoll.no : '\
              +str(self.rollno))
        print('college : '+self.college+'\ncourse : '+self.course)

for i in range(4):
    n=input()
    r=int(input())
    temp='obj'+str(i)
    temp=student(n,r)
    lstobj.append(temp)
for i in lstobj
    
    
