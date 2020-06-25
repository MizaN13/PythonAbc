employee_file = open("employees.txt", "r")
print(employee_file.readable())
'''print(employee_file.read())'''
# Reading single line from txt file
'''print(employee_file.readline())'''
# Take entire lines in an array
'''print(employee_file.readlines())'''
'''print(employee_file.readlines()[1])'''

# Using for loop to read the file
for employee in employee_file.readlines():
    print(employee)

employee_file.close()