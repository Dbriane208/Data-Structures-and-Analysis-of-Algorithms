#WORKING WITH CLASSES 
class Cookie:
    #this is a constructor
    def __init__(self,color):
        self.color = color

    def set_color(self,color):
        self.color = color

    def get_color(self):
        return self.color        

#Creating instances
cookie_one = Cookie("blue")
cookie_two = Cookie("white")

#Accessing the cookies
#When we run this code we will get the memory address of the objects in our class
print(f"The color of cookie one is ",cookie_one)
print(f"The color of cookie two is ",cookie_two)

#In order to acess the colors we need to have two methods below the constructor
print(f"The color of cookie one is ",cookie_one.get_color())
print(f"The color of cookie two is ",cookie_two.get_color())

#We can also set the colors of the cookies using the set method
cookie_one.set_color("green")
cookie_two.set_color("brown")

print(f"The color of cookie one is now",cookie_one.get_color())
print(f"The color of cookie two is now",cookie_two.get_color())

#WORKING WITH POINTERS
#Pointers work differently with different data types

#Integers
num1 = 10
num2 = num1

#Checking the value of num 1 and 2
print("The value of num1 is ",num1)
print("The value of num2 is ",num2)

#Checking the id to where they both point
print("The value of num1 is ",id(num1))
print("The value of num2 is ",id(num2))

#When we change the value of num1 they will have different values and point at different memory locations
#This indicates that integers are immutable

num2 = 22

#Checking the value of num 1 and 2
print("The value of num1 is now",num1)
print("The value of num2 is now",num2)

#Checking the id to where they both point
print("The value of num1 is now",id(num1))
print("The value of num2 is now",id(num2))

#Dictionaries
dict1 = {"value":20}
dict2 = dict1

#Dict 1 and Dict 2 will both have the same value and point the same memory location
print("The value of dict1 is ",dict1)
print("The value of dict2 is ",dict2)

print("The value of dict1 is ",id(dict1))
print("The value of dict2 is ",id(dict2))

#If we change the value of dict2 then it will overwrite the value of dict1.
# This will make them to have the new value. This shows that Dictionaries are mutable
dict1["value"] = 40

print("The value of dict1 is now",dict1)
print("The value of dict2 is now",dict2)

print("The value of dict1 is now",id(dict1))
print("The value of dict2 is now",id(dict2))

#Dictionaries which are not pointed by any variables are removed through garbage collections
dict3 = {"value":22}
dict5 = {"value":33}

#dict 4 will point at dict3
dict4 = dict3

#Let's make dict3 and dict4 to point at dict5
dict4 = dict5
dict3 = dict4 

#In the exmaple above the value 22 will be removed through garbage collection when all the dictionaries point elsewhere.
print("The value of dict3 is now",dict3)
print("The value of dict4 is now",dict4)
print("The value of dict5 is now",dict5)

print("The value of dict3 is now",id(dict3))
print("The value of dict4 is now",id(dict4))
print("The value of dict5 is now",id(dict5))
        