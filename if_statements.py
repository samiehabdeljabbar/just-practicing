#working on if statements

#is_male = True 
is_male = False
is_tall = False
#you can use these two phrases (and, or)
if  is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short make")
elif not (is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("You are neither male or not tall or both")
