#working on list functions with freecode camp


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim","Jim","Jim", "Oscar", "Toby"]
#the extend function will allow you to append a list with another list as well!
friends.extend(lucky_numbers)
#the append function will allow you to add a new variable into the list
friends.append("Creed")
#the insert function will take two values, one being the position, two being the name of the new string or variable you are inserting
friends.insert(1, "Kelly")
#the remove funtion will remove a string from the list
friends.remove("Jim")

#.clear will remove everyone from the lists
#.pop will remove the last element from the list
print(friends.index("Kevin"))
print(friends.index("Toby"))
print(friends.count("Jim"))
#friends.sort()
print(friends)