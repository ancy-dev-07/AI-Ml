# print("hello")
# num =range(1,31,4)  #sequence of number 
# """
# print(1)
# print(2)
# print(3)"""
# print(list(num))

# number=2 #to variable is used to store a value


# sentence ="""

# it is used for ecccomerce website it has 
# 1.payment integration 
# 2. add to cart


# """
# print(sentence)


# class Addition:
#     def __init__(self,a,b):
#         self.a =a
#         self.b =b
#     def add_nums(self):
#         print(f"{self.a} + {self.b} = {self.a +self.b}")


# addition =Addition(2,3)

# addition.add_nums()


# class Employee:
#     def set_employee(self, emp_id, name,age):
#         self.emp_id = emp_id
#         self.name = name
#         self.age=age

#     def show_employee(self):
#         print("ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Manager(Employee):
#     def set_manager(self, department, salary,month):
#         self.department = department
#         self.salary = salary
#         self.month = month

#     def show_manager(self):
#         print("Department:", self.department)
#         print("Salary:", self.salary)
#         print("Month:", self.month)

# m = Manager()
# m.set_employee(1, "Rahul",21)
# m.set_manager("IT", 50000,"january")
# m.show_employee()
# m.show_manager()


# class Company:
#     def __init__(self,name,location):
#         self.name =name
#         self.location =location

#     def display_company(self):
#         print(f"Company name :{self.name} Company location : {self.location}")

# class Developer(Company):
#     def __init__(self, name, location,staff_name,role):
#         Company.__init__(self,name,location)
#         self.staff_name =staff_name
#         self.role =role

#     def display_developer(self):
#         print(f"Developer name :{self.staff_name} role : {self.role}")
        
# d =Developer("infosys","trivandrum","ancy","software developer")

# d.display_developer()
# d.display_company()

class Father:
    def skill_father(self):
        print("father is good at gardening")

class Mother:
    def skill_mother(self):
        print("mother is good at cooking")

class Child(Father,Mother):
    def skill_child(self):
        print("child is good at drawing")

c =Child()
c.skill_mother()
c.skill_father()
c.skill_child()


class Dancer:
    def dancing_skill(self):
        print("hema is good at dancing")


class Singer:
    def singing_skill(self):
        print("nilla is good at singing")


class Permformed_class(Dancer,Singer):
    def permformance(self):
        print("she is good at everything")