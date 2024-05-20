class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getAvg(self):
        avg=(self.marks)
        sum=0
        for val in avg:
            sum+=val
        return sum//3
s1=Student("Mask",[10,20,30])
print(s1.getAvg())
