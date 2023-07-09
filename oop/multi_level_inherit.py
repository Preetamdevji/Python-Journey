class Parent:
    def get_name(self,name):
        self.name = name

    def show_assign_str(self):
        return self.name

class Child(Parent):
    def get_age(self,age):
        self.age = age

    def show_assign_str_2(self):
        return self.age

class GrandChild(Child):
    def get_gender(self,gender):
        self.gender = gender

    def show_assign_str_3(self):
        return self.gender
    
my_grandchild = GrandChild()
my_grandchild.get_name("Preetam")
my_grandchild.get_age("25")
my_grandchild.get_gender("Male")

print(my_grandchild.show_assign_str())
print(my_grandchild.show_assign_str_2())
print(my_grandchild.show_assign_str_3())