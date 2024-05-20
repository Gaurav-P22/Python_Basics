class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("This is Init")
        
    def Welcome(self):
        print("This is Welcome")

    def get_Marks(self):
        print(self.marks)
s1=Student("Ashish",45)
s1.get_Marks()