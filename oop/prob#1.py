class Programmer:
    company = "Microsoft"
    def __init__(self,name,age,designation):
        self.name = name
        self.age = age 
        self.designation = designation

    def microsoft_emp_details(self):
        print(f"The name of the {self.company} Programmer is: {self.name}")
        print(f"The age of Programmer which works on {self.company}: {self.age}")
        print(f"The designation of Programmer which works on {self.company}: {self.designation}")

emp_details_1 = Programmer("Preetam",25,"Junior-Developer")
emp_details_2 = Programmer("Aslam",28,"SR.Developer")
emp_details_3 = Programmer("John Wick",18,"Fresher")
emp_details_1.microsoft_emp_details()
emp_details_2.microsoft_emp_details()
emp_details_3.microsoft_emp_details()