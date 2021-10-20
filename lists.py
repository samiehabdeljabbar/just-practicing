#working with list's in python
#usually in python you will be working with large amounts of data

friends = ["Kevin", "Karen", "Jim"]
friends222 = ["Kevin", 2, False]

print(friends)
print(friends[0])
print(friends[2])
print(friends[1])
#can also index list backwards with negatives
print(friends[-1])
print(friends[-2])
#can also select more 
print(friends[1:])
#you can also pull from a range of people or list items as well
friend = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friend[1:3])
print(friend[1:4])
friend[1] = "Mike"
print(friend) 