#Age Calculate----

import datetime

age_Year = input("What is your age Year? ")
current_year = datetime.datetime.now().year
calculate_Age = current_year - int(age_Year)
print(calculate_Age)

#Large_String-----

large_string = '''Hi Python Team
Here is our large string technique
Use the 6 single quotes
for avoiding confusion press the
single quotes button 2 times :)
'''

print(large_string)

#find the index value and the -ve index ----------

course_title = "Here is the python course"
print(course_title[0])
print(course_title[-1] + " <== -ve index means start from last char")

#Splice the index --------
course = 'Python for Beginners'
print(course[0:3])

#want to see all char another approach with array is ---------
course = 'Python for Beginners'
print(course[0:])

#Alternate approach of string concatenation ---------
first_name = "Python"
last_name = "Beginners"
string_concatenation = first_name + " for " + last_name + ' <= string concatenation'
print(string_concatenation)
placeholder_string = f'{first_name} for {last_name} <= placeholder string '
print(placeholder_string)

#string built-in methods ----------
course = 'Python for Beginners'
print(len(course))
print(course.count('Python'))

#if statement ------
age = 18
name_test = 'test string'
if name_test == 'test string' or age == 18:
    print("You are 18 years old")
elif age < 18:
    print("You are less than 18 years old")
else:
    print("You are not 18 years old")

#while loop-----
i = 7
j = 1
while j <= i:
    print((' ' * (i - j)+(j * '*')))
    j = j + 1
print()
print('Done')

#for loop -------
list_of_string = ["John", "Ali", "Adnan"]
for item in list_of_string:
    print(len(item))
print()
print(len(list_of_string))

#Dictionary------
phone = input("Enter your phone number: ")
number_in_word = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
}
output = " "
for letter in phone:
    output += number_in_word.get(letter, "😒") + " "
print(output)
