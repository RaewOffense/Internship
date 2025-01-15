from context_manager import ContextManager
import csv

class CSV_Saver:
    def createFile(self,row_data):
        with ContextManager("csv_saver.csv","a") as csv_saver:
            writer = csv.writer(csv_saver)
            writer.writerow(["Name","Address","Age"])
            writer.writerow(row_data)
    def read_csv_data(self):
        with ContextManager("csv_saver.csv","r") as csv_read:
            reader = csv.reader(csv_read)
            for row in reader:
                print(row)
    def delete_student(self):
        with ContextManager("csv_saver.csv","r") as file:
            reader = csv.reader(file)
            


class Students(CSV_Saver):
    def add_students(self):
        self.name = input("Enter Student Name:")
        self.address = input("Enter Student Address: ")
        self.age = int(input("Enter Student Age:"))
        self.createFile([self.name,self.address,self.age])

def main():
    student =Students()
    while True:
        print("""
        1. Add Student
        2. View all Student
        3. Exit
        """)
        choice = input("Which task Do You Want to Do?:")

        if choice == '1':
            student.add_students()
            print("Student added successfully!")
        elif choice == '2':
            print("Student Data")
            student.read_csv_data()
        elif choice == '3':
            print("Good Bye!")  
            break
        else:
            print("Invalid Choice, Please enter valid choice!")
if __name__ == "__main__":
    main()