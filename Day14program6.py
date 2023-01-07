class A:
    def first_Method(self):
        print("Method of class A...")
class B(A):
    def second_Method(self):
        print("Method of class B...")

class C(A,B):
    def third_Method(self):
        print("Method of class C...")
        
         

if __name__=='__main__':
    ob=C()
    ob.first_Method()
    ob.second_Method()
    ob.third_Method()

