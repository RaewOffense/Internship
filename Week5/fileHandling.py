# student = open("student.txt","w")

# student.write("We are student of Techspire College and we are doing internship in Code Himalaya.")
# student.close()


#Example of read mode
# def file_handling():
#     student = open("student.txt","r")
#     # print(student.read()) # read whole documents
#     # print(student.read(5)) # display only first five character
#     print(student.readline()) # return one line
#     print(student.readline()) 
#     print(student.readline())
#     student.close()
# file_handling()

# read using Loop 
# def read_file_using_loop():
#     f = open("student.txt",'r')
#     for x in f:
#         print(x)
# read_file_using_loop()

#example of write mode
# def write_mode():
#     studentList = input("Enter name:")
#     f = open("studentList.txt","a")
#     f.write(studentList)
#     f.close()
# write_mode()

import os
if os.path.exists ("studentList.txt"):
    os.remove("studentList.txt")
else:
    print("The file does not exit")