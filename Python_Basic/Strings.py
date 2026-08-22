###1) To check wether the string is polindrome or now
# str1='amaama'
# str2=str1[::-1]
# if(str1==str2):
#     print('Polindrom')
# else:
#     print('Not a polindrome')

##2) Symmetric or not
# s1='amaama'
# half=int(len(s1)/2)
# print(half)
# if len(s1)%2==0:
#     firstHalf=s1[:half]
#     secondHalf=s1[half:]
# else:
#     firstHalf=s1[:half]
#     secondHalf=s1[half+1:]
# if firstHalf==secondHalf:
#     print('symmetric')
# else:
#     print('not symmetric')

#3)Reverse word in a string
# str1='My name is khan'
# words=str1.split()
# reversed_words=words[::-1]
# result=' '.join(reversed_words)
# print(result)

#4) Count the number of vowels in a string
# str1='My name is khan'
# vowels='aeiouAEIOU'
# count=0
# for char in str1:
#     if char in vowels:
#         count+=1
# print(count)

#5) Count the number of words in a string
# str1='My name is khan'
# words=str1.split()
# print(len(words))

#6) Count the number of characters in a string
# str1='My name is khan'
# print(len(str1))

#7) Count the number of uppercase and lowercase characters in a string
# str1='My name is khan'
# uppercase=0
# lowercase=0
# for char in str1:
#     if char.isupper():
#         uppercase+=1
#     elif char.islower():
#         lowercase+=1
# print('Uppercase:', uppercase)
# print('Lowercase:', lowercase)

#8) Remove all the punctuations from a string
# import string
# str1='My name is khan!'
# str1=str1.translate(str.maketrans('', '', string.punctuation))
# print(str1)
# print(string.punctuation)

#9) Remove all the whitespaces from a string
# str1='My name is khan'
# str1=str1.strip()
# print(str1)

#10) Replace all the spaces with hyphens in a string
# str1='My name is khan'
# str1=str1.replace(' ', '-')
# print(str1)

#11) Count the number of occurrences of a substring in a string
# str1='My name is khan'
# substring='khan'
# count=str1.count(substring)
# print(count)

#12) Check if a string starts with a specific substring
# str1='My name is khan'
# substring='My'
# if str1.startswith(substring):
#     print('The string starts with the substring')
# else:
#     print('The string does not start with the substring')

#13) Check if a string ends with a specific substring
# str1='My name is khan'
# substring='khan'
# if str1.endswith(substring):
#     print('The string ends with the substring')
# else:
#     print('The string does not end with the substring')

#14) Convert a string to uppercase
# str1='My name is khan'
# str1=str1.upper()
# print(str1)

#15) Convert a string to lowercase
# str1='My name is khan'
# str1=str1.lower()
# print(str1)

#16) Capitalize the first letter of each word in a string
# str1='my name is khan'
# str1=str1.title()
# print(str1)

#17) Count the number of digits in a string
# str1='My name is khan 123'
# count=0
# for char in str1:
#     if char.isdigit():
#         count+=1
# print(count)

#18) Check if a string is alphanumeric
# str1='Mynameiskhan123'
# if str1.isalnum():
#     print('The string is alphanumeric')
# else:
#     print('The string is not alphanumeric')

#20) Check if a string is alphabetic
# str1='Mynameiskhan'
# if str1.isalpha():
#     print('The string is alphabetic')
# else:
#     print('The string is not alphabetic')

