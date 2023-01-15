class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollNumber):
        self.__rollNumber=rollNumber
    def getRollNumber(self):
        return self.__rollNumber
obj=Student()
obj.setName("abhi")
obj.setRollNumber(2701)
print(obj.getName())
print(obj.getRollNumber())