class Employee:
    def __init__(self, salary , name , age ):
        self.__salary = salary
        self.name = name
        self.__age = age

    def PrintInfo(self):
        print(self.__salary)
        print(self.name)
        print(self.__age)

    def SetSalary(self, newSalary):
        self.__salary = newSalary

    def GetSalary(self):
        return self.__salary


Astrid = Employee(2500 , "Astrid" , "27")
Astrid.name = "Elsa"
Astrid.__age = 34
print(Astrid.GetSalary())
Astrid.SetSalary("4500")
print(Astrid.GetSalary())
