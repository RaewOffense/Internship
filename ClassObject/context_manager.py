# Custom Simple Context Management
class ContextManager:
    def __init__(self,fileName,mode):
        self.fileName = fileName
        self.mode = mode 
        self.file = None
    
    def __enter__(self):
        self.file = open(self.fileName,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
    

with ContextManager("demo.csv","w") as file:
    file.write("Hello developer")


with ContextManager("demo.txt","r") as file:
    result = file.read()
    print(result)