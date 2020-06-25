print("Hello World!!!!!!!!!!!!!!!!!!!!!!!")

Person_Name = "John"
Person_Age = "35"
is_Male = True

print("There was a man named " + Person_Name + ",")
print(Person_Name + " is " + Person_Age + " Years old.")

# working with string
print("Covid19\nBD\nQuatentines Day\nStarted Date:26-03-2020")

Phrase = "Hello Expertlab BD Ltd"
print(Phrase)
print(Phrase + " is Cool")
print(Phrase.upper())
print(Phrase.upper().isupper())
print(Phrase.lower().islower())

print(len(Phrase))

print(Phrase[6])
print(Phrase.index("E"))

print(Phrase.replace("Expertlab", "Skilledlab"))
print(Phrase)

# working with Number
print(2)
print(2.5)
print(-3.5)
print(3 * (2 + 5))
print(10%3)

my_num = 5
print(my_num)

# getting error without string casting
'''print(my_num + " is my favourite number.")
'''

print(str(my_num) + " my favourite number.")
print(pow(3,2))
print(pow(4,6))
print(min(4,6))
print(max(4,6))

my_num2 = -2.5
print(abs(my_num2))
print(round(2.4))
print(round(2.7))

from math import *

print(floor(5.5))
print(ceil(5.5))
print(sqrt(36))