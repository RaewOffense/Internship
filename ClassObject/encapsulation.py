#Example of encapsulation

class Student:
    def __init__(self,name,address,email):
        self.name = name
        self.address = address
        self.__email = email
    
    def student_detail(self):
        print(self.name)
        print(self.address)
        print(self.__email)
student =Student("Rajesh","banke","rajesh@gmail.com")
