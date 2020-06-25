lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Piyal", "Rifat", "Nabila", "Mahmud", "Tofazzal"]
'''friends.extend(lucky_numbers)
'''
print(friends)
# Adding another item in Friends List
# append function add item end of the list
friends.append("kipta")
print(friends)
# insert function add item with index position
friends.insert(1, "Keri")
print(friends)
# remove function
friends.remove("kipta")
print(friends)
# clear all items from list
'''friends.clear()'''
print(friends)
'''#pop function remove the last elements of the list
lucky_numbers.pop()'''
print(lucky_numbers)
print(lucky_numbers.index(15))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
# Copying friends elements into friends2 List
firends2 = friends.copy()
print(firends2)