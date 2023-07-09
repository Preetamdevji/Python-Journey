class School:
    def __init__(self,school_name,school_address,school_principle_name):
        self.school_name = school_name
        self.school_address = school_address
        self.school_principle_name = school_principle_name

    def school_details(self):
        print("The Name of School is:", self.school_name)
        print("The Address of School is:", self.school_address)
        print("The Deen of School is:", self.school_principle_name)

class Parents:
    def __init__(self,father_name,mother_name,home_address):
        self.father_name = father_name
        self.mother_name = mother_name
        self.home_address = home_address

    def parent_details(self):
        print("The Name of Father is:", self.father_name)
        print("The Name of Mother is:", self.mother_name)
        print("The Home Address is:", self.home_address)

class Student(School,Parents):

    def __init__(self,student_name,student_grade,school_name,school_address,school_principle_name,father_name,mother_name,home_address):
        School.__init__(self,school_name,school_address,school_principle_name)
        Parents.__init__(self,father_name,mother_name,home_address)
        self.student_name = student_name
        self.student_grade = student_grade

    def student_details(self):
        print("Student Name is:", self.student_name)
        print("Student Grade is:", self.student_grade)
        super().school_details()
        super().parent_details()
s1 = Student("Preetam","A+","The Wendy School","Block-9","Tushna Patel","Devji Kesu","Venu kanji","Zamzama Park")
s1.student_details()