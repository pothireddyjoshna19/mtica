class A:
    def first_Method(self):
        print("Method of class A...")
class B(A):
    def first_Method(self):
        print("Method of class B...")
        super().first_Method

         


ob=B()
ob.first_Method()
    
