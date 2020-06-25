is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a Tall Male")
else:
    print("You are neither Male nor Tall")

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a Tall Male")
else:
    print("You are neither Male nor Tall")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a Tall Male")
else:
    print("You are neither Male nor Tall")

#If else condition
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a Tall Male")
elif is_male and not(is_tall):
    print("You are short Male")
else:
    print("You are either not Male or not Tall")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a Tall Male")
elif not(is_male) and is_tall:
    print("You are not Male but Tall")
else:
    print("You are either not Male or not Tall")