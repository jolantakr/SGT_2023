# # 1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided.
# # 1.1) Based on the task 1, count the occurrences of each character in the text provided and display them in the output
# # 2)Write the program to sort the list (without using sort function). You can implement any algorithm
#
# #Task 1
# text = input("Enter the text: ")
# text = text.lower()
# letter = input("Enter the letter: ")
# letter = letter.lower()
#
# text_len = len(text)
# text_list = []
#
# for i in range(0, text_len):
#     text_list.append(text[i])
#
# count = text_list.count(letter)
# if count > 0 and count == 1:
#     print(f"Letter {letter} is used {count} time.\n")
# elif count > 0:
#     print(f"Letter {letter} is used {count} times.\n")
#
#
# #Task 1.1
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet_len = len(alphabet)
#
# for x in range(0, alphabet_len):
#     check_letter = alphabet[x]
#     count2 = text_list.count(check_letter)
#     if count2 > 0 and count2 == 1:
#         print(f"Letter {check_letter} is used {count2} time.")
#     elif count2 > 0:
#         print(f"Letter {check_letter} is used {count2} times.")
from typing import List

#Task 2

elements = ["pineapple", "banana", "apple", "lemon"]

for q in range(0, len(elements)):
    for z in range(0, len(elements)-1):
        if elements[z] > elements[z+1]:
            elements[z], elements[z+1] = elements[z+1], elements[z] #SWAPING ELEMENTS
print(elements)

