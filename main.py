#inhertince
class Person:
    # method
    def __init__(self, name, age, phone, email):
        # create an attribute called name
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

class Student(Person):

    no_of_student=0
    def __init__(self, name, age, phone, email, course, year, deparment):
        super().__init__(name, age, phone, email)
        self.graduationyear = year
        self.addcourse = course
        self.deparment = deparment
        Student.no_of_student+=1
    def printstudent(self):

        print(self.name, self.age, self.phone, self.email, self.addcourse, self.graduationyear, self.deparment)

p1 = Student("aldsouqy", 20, '01066564601', "aldsouqy@gamil.com",  "algorthim", 2024,'cs')
p2 = Student("dana", 23, '010678944601', "dana@gamil.com",  "math", 2027,'is')
p3 = Student("hassan", 21, '019089764601', "hassan@gamil.com",  "math", 2025,'se')
p4 = Student("aml", 22, '015675453', "aml@gamil.com",  "math", 2026,'it')
print("student")
print("")
p1.printstudent()
print("")
p2.printstudent()
print("")
p3.printstudent()
print("")
p4.printstudent()
print("")

class Doctor(Person):

    def __init__(self, name , age , phone, email, addcourse, department):
        super(Doctor, self).__init__(name,age,phone,email)
        self.course = addcourse
        self.department= department

    def printdoctor(self):

        print(self.name, self.age, self.phone, self.email, self.course, self.department)
p1 = Doctor("ahmed", 37, '015444499900', "ahmed@gmail.com", "python", 'se')
p2 = Doctor("ibrahim", 44, '010454499900', "ibrahim@gmail.com", "operating search", 'it')
p3 = Doctor("osman", 46, '01556444499900', "oaman@gmail.com", "opreting system", 'is')
p4 = Doctor("elsaidy", 40, '0106478328', "elsaidy@gmail.com", "numercial analysis", 'cs')
print("doctor:")
print("")
p1.printdoctor()
print("")
p2.printdoctor()
print("")
p3.printdoctor()
print("")
p4.printdoctor()
print("")


class employee(Person):
    def __init__(self, name, age, phone, email):
        super(employee, self).__init__(name, age,phone,email)
    def printemployee(self):

        print(self.name, self.age, self.phone, self.email)

p1 = employee("mohamed", 45, '1234564779', "mohamed@gmail.com")

p2 = employee("rslan", 43, '1230984770', "rslan@gmail.com")

p3 = employee("frahat", 40, '01567564779', "frahat@gmail.com")

p4 = employee("hazem", 42, '0109876649', "hazem@gmail.com")

print("employee:")
print("")
p1.printemployee()
print("")
p2.printemployee()
print("")
p3.printemployee()
print("")
p4.printemployee()

























