try:
    #answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid input")

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
# put error massage as
except ZeroDivisionError as error:
    #print("Divide by zero")
    print(error)
except ValueError:
    print("Invalid input")