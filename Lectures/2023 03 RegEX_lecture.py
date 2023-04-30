# Examples from lecture

# re.search(pattern, string): Searches for the first occurrence of the pattern in the string and returns a match object if found.
    # import re
    # text = "The quick brown fox jumps over the lazy dog."
    # match = re.search('fox', text)
    # if match:
    # print("Found a match:", match.group())
# This will output: Found a match: fox

# re.findall(pattern, string): Returns a list of all non-overlapping occurrences of the pattern in the string.
    # import re
    # text = "The quick brown fox jumps over the lazy dog."
    # matches = re.findall('[aeiou]', text)
    # print(matches)
#This will output: ['e', 'u', 'i', 'o', 'u', 'o', 'e', 'a', 'o']

# re.sub(pattern, repl, string): Replaces all occurrences of the pattern in the string with the replacement string.
    # import re
    # text = "The quick brown fox jumps over the lazy dog."
    #new_text = re.sub('fox', 'cat', text)
    # print(new_text)
# This will output: The quick brown cat jumps over the lazy dog.

# emailPattern= "^[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]+@([a-z0-9]+\.)+[a-z]{2,}+$"
# text = input("Enter the text\n")
# match = re.search(emailPattern, text)
# if match:
#     print("Pattern is correct")
# else:
#     print("Pattern is not correct")

# phoneInput = input("Enter the phone:\n")
# phonePattern = r'^((\+371|8)( ){0,1}){0,1}2[0-9]{7}$'
# match = re.search(phonePattern, phoneInput)
# # if match:
# #     print("Pattern is correct")
# # else:
# #     print("Pattern is not correct")

