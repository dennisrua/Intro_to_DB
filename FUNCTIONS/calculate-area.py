#Function definitions

def calculate_area(length, width):
    """ calculates the area of a rectangle"""
    area = length * width
    return area

print(calculate_area(7,10))

# Local vs Global Scope
# count = 0
# def increment():
#     count+=1

# increment()
# print(count)

#Global and nonlocal keywords
counts = 1
def increment_global():
    global counts
    counts += 3

increment_global()
print(counts)

#KEYWORD ARGUMENTS 
def user_info(name, age=None):
    print(f"Name: {name}")
    if age:
        print(f"Age:{age}")

user_info(name="Albright", age=26)

#Write a function to greet the user by name.
def greet(name):
   print(f"Wassuuup {name} ?")

name= input("What is your name? ")
greet(name)

#Create a function to calculate the area of a rectangle. Is this the best implementation? IDK
def triangle_area(area):
     print(f"The area of your triangle is {area}")

base = int(input("enter triangle base: "))
height = int(input("Enter triangle height: "))
area = 1/2 * base * height

triangle_area(area)

#Develop a function to check if a number is even or odd.
def is_even_or_odd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

number = int(input("Enter any number:"))
is_even_or_odd(number)