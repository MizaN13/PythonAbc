monthConversions = {
    "Jan": "January",
    "Feb": "Februry",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Oct"])
print(monthConversions.get("Dec"))

# Loop Through a Dictionary
for item in monthConversions:
    print(monthConversions[item])

# from Mosh
phone = input("Phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for digit in phone:
    output += digit_mapping.get(digit, "!") + " "
print(output)