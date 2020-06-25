name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " ! Your are " + age + " Years old now.")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)
# We need int casting number num1 and num2
result = int(num1) + int(num2)
print(result)

# Adding two Float number
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)