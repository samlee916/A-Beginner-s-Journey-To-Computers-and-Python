#Python Example 1

#a simple print statement
print("Hello World")

#a int variable
d = 35
print(d)

#a string variable
w = "hello"
print(w)

#combining two strings
p = "world"
print(w+p)

#combining two intergers
a = 60
print(d+a)

#length of a variable
len(p)

#changing a string to uppercase and lowercase
print(w.upper())
print(p.lower())

#finding a specific string
print(w[0])
print(w[3])

#print out a string from a specific length
print(w[:3])

#lists
shopping_list = ["apples", "potatoes", "bacon", "fish"]
print(shopping_list)
grocery_list = ["pie", "grapes", "oranges"]
print(shopping_list + grocery_list)

#adding something to an array
shopping_list.append("bread")
print(shopping_list)

#removing something from an array
shopping_list.remove("bread")
print(shopping_list)

#how long the shopping_list is
print(len(shopping_list))

#tuples
food_list = ("yam", "jackfruit", "catfish");
#tuples are immutable, meaning that one cannot remove or update things
print(food_list[1])

#dictionaries
dict = {"Name" : "Eric", "Height" : 23, "Weight" : 98}
print(dict["Name"])
#clearing the dictionary
#dict.clear();
print(dict.clear())
print(len(dict))






