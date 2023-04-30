# Task 1

# number = int(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


# Task 2

# numbers = range(1, 101)
#
# for i in numbers:
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# Task 3

# number = int(input("Enter a number: "))
#
# for i in range(1, number +1):
#     if number % i == 0:
#         print(i)


# Task 4
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Choose operation *,/, +,- or %: ")
#
# while operation != "*" and operation != "/" and operation != "+" and operation != "-" and operation != "%":
#     print("Operation provided isn't valid, please, try again!")
#     operation = input("Choose operation *,/, +,- or %: ")
#
# if operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     if num2 == 0:
#         print("You cannot divide by zero.")
#     else:
#         print(num1 / num2)
# elif operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "%":
#     print(num1 % num2)

# Task 5
# number = int(input("Enter a number: "))
#
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print("This number is not a prime number.")
#             break
#     else:
#         print("This number is a prime number.")
# else:
#     print("This number is not a prime number.")
