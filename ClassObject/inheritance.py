class Person:
    def __init__(self, name):
        self.name = name

    def personName(self):
        return f"Person Name is {self.name}"

class Employee(Person):
    def __init__(self,name, id):
        super().__init__(name)
        self.id = id
    
    def employee_id(self):
        return f" Employee id no. is {self.id}"

class Employee1(Employee):
    def __init__(self,name,id,address):
        super().__init__(name,id)
        self.address =address
    def show(self):
        return f"Address is {self.address}"

employee = Employee1("Rajesh",9999,"Banke")

print(employee.personName())
print(employee.employee_id())
print(employee.show())