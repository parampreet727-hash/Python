# Creating Class
class Student:
    name = "Parampreet Dhatt"

# Creating Object 
s1 = Student()
print(s1.name)

# Creating Class
class Car:
    color = "Blue"
    brand = "BMW"

# Creating Object 
carDetails = Car()
print(carDetails.color)
print(carDetails.brand)

# Constructor => 
# Creating Class
class Student:
    def __init__(self, name):
        self.name = name
        print("Adding new Student Details in Database...")

# Creating Object 
s1 = Student("Parampreet Dhatt")
print(s1.name)

s2 = Student("Harpreet Dhatt")
print(s2.name)