#learning functions 

#key work for functions is def

def say_hi():
    print("Hello User")
print("Top")
#calling the function by typing the function anme
say_hi()
print("Bottom")

def take_input():
    name = input("What is your name ")
    age = input("What is your age ")
    print("Hello " + name + "! You are " + age + ", Thats Awesome!")

take_input()