# Task 1

age = int(input("What is your age? "))
licence = (input("Do you have a drivers licence? "))

result = age >= 18 and licence == "yes"

print(f"You are able to drive : {result}")

# Task 2
password = input("What is your password? ")
password_l = len(password)

result = password_l >= 8

print(f"Password accepted: {result}")

# Task 3
number_1 = int(input("Enter first integer: "))
number_2 = int(input("Enter second integer: "))

a = number_1 % 2 == 0
b = number_2 % 2 == 0

result_1 = a and b
print(f"Both numbers are even : {result_1}")

result_2 = a or b
print(f"At least one number is even : {result_2}")


# Task 4

year = int(input("Enter a year to check if it is a leap year: "))
a = year % 4 == 0
b = year % 100 == 0
c = year % 400 == 0

result = a and not b or c

print(f"Leap year : {result}")


# Task 5

check_date = input("Enter the date (day, month, year): ")
a, b, c = check_date.split(",")
a = int(a)
b = int(b)
c = int(c)

year = c > 0

date_30 = 0 < a <= 30
month_30 = b == 4 or b == 6 or b == 9 or b == 11

date_31 = 0 < a <= 31
month_31 = b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12

date_f_28 = 0 < a <= 28
date_f_29 = a == 29
mont_f = b == 2

a_1 = c % 4 == 0
b_2 = c % 100 == 0
c_3 = c % 400 == 0

leap_year = a_1 and not b_2 or c_3


result = (date_30 and month_30 and year) or (date_31 and month_31 and year) or (date_f_28 and mont_f and not leap_year) or (date_f_29 and mont_f and leap_year)

print(f"Date valid : {result}")
