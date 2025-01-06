class A:
    def showA(self):
        print("Developer A")
#single inheritance (classs B(A):)
class B:
    def showB(self):
        print("Developer B")

#multiple inheritance (class C(A,B):)
class C(A,B):
    def showC(slef):
        print("Developer C")

obj = C()
obj.showA()
obj.showB()
obj.showC()

