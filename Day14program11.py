#Magic Methods "dunders"
#are special method which have leading and training double underscore
#used for operator overloading
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        temp=self.real+ob.real,self.imag+ob.imag
        return temp
    def __str__(self):
        return (self.real,self.imag)
ob1=Complex(3,5)
ob2=Complex(2,1)
ob3=ob1+ob2
print(ob3)
