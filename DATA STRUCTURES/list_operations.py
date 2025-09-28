import random

# LISTS
my_list=[10,20,30,40,50,60,70,80,90,100]

#indexing
print(my_list[0])
print(my_list[2])
#slicing 

#allows you to extract items from a list using list[start:stop:step] indices
# start → index where slicing begins (default is 0 if omitted).
# stop → index where slicing ends (but it is excluded).
# step → how many items to "skip" as you move through the list. Default is 1.
print(my_list[1:3]) #gives [20, 30] excluding the stop index
print(my_list[::2]) #step of two --> gives [10,30,50,70,90]

#reversing a list 
print(my_list[::-1]) #negative-no stop, no start, skip one index each (prints the whole array in reverse)
print(my_list[::-3]) # prints the whole array at intervals of 3
#Rule of thumb ==> positive step(move left-right), negative step(move right-left)

#appending - adding elements to the end of a list 
# my_list=[10,20,30,40,50,60,70,80,90,100]
append=my_list.append(130)
print(append) #-->returns none
print(my_list)

#removing - deleting items from a list
remove =my_list.remove(30)
print(my_list)     

#DICTIONARIES
 #METHODS --> get(key, default) keys() values() items()


#TUPLES
#Are like lists --> but once created the elements cannot be changed(immutable)


#SETS
#Are a collection of unique elements (do not allow duplicate values)
#OPERATIONS --> union() - combines two sets to create a new set cotaining all unique elements from both sides
# intersection() - finds the common elements between the two sets 
# difference() - finds the elements present in one set but not in another set



########PRACTICE EXERCISES######################

#Exercise 1: Create a list to store names of your favorite fruits. 
# Write code to access the second element and print it.

favorite_fruits=["apple", "bananas", "watermelon", "pineapples", "grapes"]
print(favorite_fruits[1]) #returns bananas

#Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. 
# Use the method to retrieve the genre.
favorite_book ={
    "title": "Finding Me",
    "Author" : "Viola Davis",
    "genre" : "Autobiography"
}
print(favorite_book.get("genre")) #returns autobiography
print(favorite_book.keys()) #returns [title, author, genre]
print(favorite_book.values()) #returns [finding me, viola davis, authobiography]
print(favorite_book.items()) #returns [(title, finding me),(author, viola davis), (genre, autobiography)]

#Exercise 3: Write a program to generate a random set of numbers between 1 and ten. 
#Use set operations to remove duplicates and display the unique numbers.

random_numbers = [random.randint(1,10) for _ in range(15)]
print(f"original list with possible duplicates : {random_numbers}")

unique_numbers = set(random_numbers)
print(f"set with unique numbers only: {unique_numbers}")   

