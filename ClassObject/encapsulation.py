#Example of encapsulation

class Student:
    def __init__(self,name,address,email):
        self.name = name
        self.address = address
        self.email = email
    def show(self):
        print(f"{self.name} {self.email} {self.address}")

    
    def _student_detail(self):
        print(self.name)
        print(self.address)
        print(self.email)

class Student1 (Student):
    def display(self):
        self.show()
        self._student_detail()
        
stud =Student1("Rajesh","banke","rajesh@gmail.com")

stud.display()