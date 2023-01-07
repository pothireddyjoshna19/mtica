class Wolf:
    price=500  #Class attribute created by variables within
           #the body of the class
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("Grr...")
class Dog(Wolf):

    def bark1(self):
        print("Wolf")


if __name__=="__main__":
    pet1=Dog("Tommy","Brown")
    pet1.bark()
    pet1.bark1()
    print(pet1.name,"is of color",pet1.color)




