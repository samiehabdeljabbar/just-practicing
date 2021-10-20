#working on list functions with freecode camp


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#the extend function will allow you to append a list with another list as well!
friends.extend(lucky_numbers)
#the append function will allow you to add a new variable into the list
friends.append("Creed")
#the insert function will take two values, one being the position, two being the name of the new string or variable you are inserting
friends.insert(1, "Kelly")

print(friends)