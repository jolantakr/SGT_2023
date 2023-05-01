# # Task 1
# def add_numbers(a, b):
#     return a + b
#
#
# a = float(input("Write a number: "))
# b = float(input("Write a number: "))
# print(add_numbers(a, b))
#
#
# # Task 2
# def count_vowels(text):
#     vowels = "aeiou"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#
#
# text = input("Write your text here: ").lower()
#
# print(count_vowels(text))
#
#
# # Task 3
#
# def compare_txt(txt):
#     txt_reverse = txt[::-1]
#     if txt_reverse == txt:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")
#
#
# txt = input("Write your text here: ").lower()
# compare_txt(txt)

# # Task 4
# def get_even_numbers(numbers):
#     numbers = numbers.split(",")
#     even_numbers = []
#     for num in numbers:
#         if int(num) % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers
#
#
# number_input = input("Write numbers here: ")
# print(get_even_numbers(number_input))
#
# #Task 5
#
# def find_sum_numbers(numbers, target_sum):
#     numbers = numbers.split(",")
#     for num in numbers:
#         difference = target_sum - int(num)
#         if str(difference) in numbers and str(num) != str(difference):
#             return [int(num), difference]
#     return None
#
# numbers_input = input("Write numbers here: ")
# target_sum_input = int(input("Write target sum here: "))
# print(find_sum_numbers(numbers_input, target_sum_input))


# # Task 6
#
# def product_of_num(numbers_list):
#     result = 1
#     for num in numbers_list:
#         result *= int(num)
#     return result
#
#
# numbers_input = input("Write numbers here: ")
# numbers_input = numbers_input.split(",")
# print(product_of_num(numbers_input))

##Task 8

# def key_of_even(dict_input:dict):
#     keys = []
#     for key,value in dict_input.items():
#         if value % 2 == 0:
#             keys.append(key)
#     return keys

# input_dict = {"1":6,"2":10,"3":9,"4":8}
# print(key_of_even(input_dict))

#Task 9

# def get_sums(list_of_dict:list):
#     sums_dict = dict()
#     for values_dict in list_of_dict:
#         for key,value in values_dict.items():
#             if key in sums_dict:
#                 sum = sums_dict.get(key)
#                 sum += value
#                 sums_dict[key] = sum
#             else:
#                 sums_dict[key] = value
#     return sums_dict

# #Task 10
# def swap(my_t):
#     if len(my_t) < 2:
#         return my_t
#     my_list = list(my_t)
#     my_list[0], my_list[-1] = my_list[-1], my_list[0]
#     new_t = tuple(my_list)
#     return new_t
#
#
# # Test
# t1 = (1, 2, 3, 4, 5)
# t2 = ('a', 'b', 'c', 'd')
# t3 = (1,)
#
# print(swap(t1))
# print(swap(t2))
# print(swap(t3))


# # Task 11
#
# def get_set(input_set):
#     output_set = set()
#     for element in input_set:
#         if element % 3 != 0:
#             output_set.add(element)
#     return output_set
#
#
# # Test
#
# input_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(get_set(input_set))
