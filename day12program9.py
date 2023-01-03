class Dog:
    price=4000
    def __init__(self,name,color):
          self.color=color
          self.name=name
    def bark(self):
        print("woof")
        print(self.name,"has",self.price,"price and its color is", self.color)

if __name__=="__main__":
    pet1=Dog("bunty","brown")
    pet2=Dog("johny","white")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
    Dog('abc','blue').bark()
