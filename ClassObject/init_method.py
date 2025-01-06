class Students:

    def __init__(self,name,address,age):
        self.name = name
        self.address =address
        self.age = age
    def __str__(self):
        return f"Name:{self.name}, age:{self.age}, address:{self.address}"

student =Students("Rajesh34",35,22)
print(student)
