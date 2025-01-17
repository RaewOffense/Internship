from context_manager import ContextManager
import csv
import random

class CSV_Saver:
    def createFile(self, row_data):
        with ContextManager("csv_saver.csv", "a") as csv_saver:
            writer = csv.writer(csv_saver)
            if csv_saver.tell() == 0:  # Check if file is empty (first entry)
                writer.writerow(["StudentID", "Name", "Address", "Age"])
            writer.writerow(row_data)

    def read_csv_data(self):
        with ContextManager("csv_saver.csv", "r") as csv_read:
            reader = csv.DictReader(csv_read)
            for row in reader:
                print(row)

    def updateDetail(self, student_id, updated_data):
        """Update student details based on the given student_id."""
        updated_rows = []
        found = False

        with ContextManager("csv_saver.csv", "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames  # Get headers

            for row in reader:
                if row["StudentID"] == student_id:
                    # Update the student's details with the new data
                    row.update(updated_data)
                    found = True
                updated_rows.append(row)

        if found:
            with ContextManager("csv_saver.csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_rows)
            print(f"Student with ID {student_id} updated successfully!")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        """Delete a student based on the student_id."""
        updated_rows = []
        found = False
        with ContextManager("csv_saver.csv", "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            for row in reader:
                if row["StudentID"] == student_id:
                    found = True
                    continue
                updated_rows.append(row)

        with ContextManager("csv_saver.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        if found:
            print(f"Student with ID '{student_id}' deleted successfully!")
        else:
            print(f"Student with ID '{student_id}' not found.")

class Students(CSV_Saver):
    def generate_student_id(self):
        """Generate a random student ID."""
        return str(random.randint(10000, 99999))  # Ensure ID is a string

    def add_students(self):
        """Add a new student."""
        student_id = self.generate_student_id()
        name = input("Enter Student Name: ")
        address = input("Enter Student Address: ")
        age = int(input("Enter Student Age: "))
        self.createFile([student_id, name, address, age])

def main():
    student = Students()
    while True:
        print("""
        1. Add Student
        2. View all Student
        3. Update Student Details
        4. Delete Student
        5. Exit
        """)
        choice = input("Which task Do You Want to Do? ")

        if choice == '1':
            student.add_students()
            print("Student added successfully!")
        elif choice == '2':
            print("Student Data:")
            student.read_csv_data()
        elif choice == '3':
            student_id = input("Enter the Student ID to update: ")
            print("""
            1. Address
            2. Age
            """)
            update_choice = input("What do you want to update? ")

            if update_choice == '1':
                updated_address = input("Enter new Address: ")
                update_data = {"Address": updated_address}
                student.updateDetail(student_id, update_data)
            elif update_choice == '2':
                updated_age = input("Enter new Age: ")
                updated_data = {"Age": updated_age}
                student.updateDetail(student_id, updated_data)
            else:
                print("Invalid Choice!")
            
        elif choice == '4':
            student_id = input("Enter the Student ID to delete: ")
            student.delete_student(student_id)
        elif choice == '5':
            print("Good Bye!")  
            break
        else:
            print("Invalid Choice, Please enter valid choice!")

if __name__ == "__main__":
    main()
