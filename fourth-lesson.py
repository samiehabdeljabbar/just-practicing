#working with strings

#in order to use a string I need to use quotation marks

# \n makes things print virtically 
print("Giraffe\nAcademy")

# \# basically means stop python, add this quotation than continue printing this statement
print("Giraffe\"Academy\"")

phrase = "Giraffe Academy"
print(phrase)

#concantination

print(phrase + " is cool")

#printing the string all in lower case

print(phrase.lower())

#printing in all uppercase

print(phrase.upper())

#printing a boolean statement
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())

#printing the number of characters that is in a string using len()
print(len(phrase))