# # Task 1
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return "Make : " + self.make + ", Model : " + self.model + ", Year : " + str(self.year)
#
#
# car1 = Car("Audi", "A3", 2020)
#
# print(car1.get_info())


# Task 2

# class Rectangle:
#     def __init__(self, r_width, r_height):
#         self.r_width = r_width
#         self.r_height = r_height
#
#     def area(self):
#         r_area = int(self.r_width) * int(self.r_height)
#         return r_area
#
#     def perimeter(self):
#         r_perimeter = (int(self.r_width) * int(self.r_height)) * 2
#         return r_perimeter
#
#
# rec1 = Rectangle(6, 5)
#
# print("Area: " + str(rec1.area()))
# print("Perimeter: " + str(rec1.perimeter()))


# Task 3
#
# class BankAccount:
#     def __init__(self, account_number: str, balance: float, owner_name: str):
#         self.account_number = account_number
#         self.balance = balance
#         self.owner_name = owner_name
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not possible to withdraw, because the amount exceeds the balance")
#         else:
#             self.balance -= amount
#
#
# bank_account = BankAccount("LV834343", 20000, "Jack Peterson")
# print(bank_account)
# bank_account.deposit(100)
# print(bank_account)
# bank_account.withdraw(400)
# print(bank_account)
# bank_account.withdraw(40000)

# Task 4
#
# class Person:
#     def __init__(self, name: str, age: int, address: str):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def get_info(self):
#         return f"Name: {self.name}, age: {self.age}, address: {self.address}"
#
#
# p1 = Person("Ilze", 22, "Miera iela 1, Riga, LV-1011")
# print(p1.get_info())

# Task 5

# class Animal:
#     def __init__(self, name: str, species: str):
#         self.name = name
#         self.species = species
#
#     def speak(self):
#         return "Muuu"
#
# a1 = Animal("Gauja", "cow")
# print(a1.speak())

# # Task 6
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}"
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, number_of_doors):
#         super().__init__(make, model, year)
#         self.number_of_doors = number_of_doors
#
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year, width, max_width):
#         super().__init__(make, model, year)
#         self.width = width
#         self.max_width = max_width
#
#     def max_cargo_width(self):
#         return self.max_width - self.width
#
#
# car = Car("Audi", "A3", 2020, 4)
# print(car.get_info())
#
# truck = Truck("Volvo", "V4", 2020, 10000, 15000)
# print(truck.max_cargo_width())

# #Task 7
# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"
#
# class Student(Person):
#     def __init__(self, name, age, address, student_id):
#         super().__init__(name, age, address)
#         self.student_id = student_id
#
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Student ID: {self.student_id}"
#
#
# class Teacher(Person):
#     def __init__(self, name, age, address, subject):
#         super().__init__(name, age, address)
#         self.subject = subject
#
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Subject: {self.subject}"
#
#
# student1 = Student("Janis", 25, "Liela iela 10, Riga", 34567)
# teacher1 = Teacher("Ilze", 35, "Maza iela 10, Riga", "Math")
#
# print(student1.get_info())
# print(teacher1.get_info())

# Task 8
# import json

# key = "age"
# with open("Persons.json","r") as f:
#     persons = json.load(f)["persons"]

# persons.sort(key=lambda person:person[key])

# with open("Persons.json","w") as f:
#     json.dump({"persons":persons},f)

# Task 9
# with open("Students_Grades.csv","r") as f:
#     students_grades = f.readlines()

# averages = list()
# for student_line in students_grades[1:]:
#     columns = student_line.replace("\n","").split(";")
#     name = columns[0]
#     sum_grade = 0
#     for grade in columns[1:]:
#         sum_grade += int(grade)
#     averages.append([name,sum_grade/(len(columns)-1)])

# csv_output = students_grades[0].replace("\n","")
# for student in averages:
#     csv_output += "\n" + student[0] + ";" + str(student[1])

# with open("Student_average.csv","w") as f:
#     f.write(csv_output)

# Task 10

import csv

lines = list()
with open("Students_Grades.csv", "r") as csvfile:
    students_grades_csv = csv.reader(csvfile, delimiter=";")
    for student in students_grades_csv:
        lines.append(student)

student_grades = lines[1:]
student_grades.sort(key=lambda student: student[0])

with open("Students_Grades.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(lines[0])
    writer.writerows(student_grades)
