class Library:
    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks

    def showAvailableBooks(self):
        print("The books we have in our library are as follows:")
        print("=================================================")

        for book in self.availableBooks:
            print(book)
    
    def lendBook(self,requestedBook):
            if requestedBook in self.availableBooks:
                print("The book you requested has now been borrowed")
                self.availableBooks.remove(requestedBook)
            else:
                print("Sorry the book you have requested is currently not in the library")
                
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("Thanks for returning your borrowed book")

class Students:
    def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

    def returnBook(self):
        print("Enter the name of the book you'd like to return>>")
        self.book=input()
        return self.book
    

def main():
    library =Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
    student =Students()
    while True:
            print("""==================== Library Menu =====================
                1. Display All Available Books
                2.Request a Book
                3. Return a Book
                4. Exit
                """)
            choice = int(input("Enter your choice:"))

            if choice == 1:
                library.showAvailableBooks()
            elif choice == 2:
                library.lendBook(student.requestBook())
            elif choice == 3:
                library.addBook(student.returnBook())
            elif choice == 4:
                print("Thank You, Visit Again!!!")
                break
            else:
                print("Invalid Choice")
main()
                
