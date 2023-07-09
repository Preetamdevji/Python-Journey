class Employee:
    def __init__(self,name,age,salary,gender):
            self.name = name
            self.age = age
            self.salary = salary
            self.gender = gender
        
    def employee_details(self):
          print("The name of Employee is:" + str(self.name))
          print("The age of Employee is:" + str(self.age))
          print("The salary of Employee is:" + str(self.salary))
          print("The gender of Employee is:" + str(self.gender))

e1 =Employee("Preetam",25,20000,"Male")
e1.employee_details()