my_set = {1,3,2,4,5,7,6,9,8,10,10}

print(my_set)
# Output - {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

my_set.add(20)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20}

my_set.remove(9)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8, 10, 20} (9 Remove)

print(type(my_set)) # <class 'set'>

# Union 

num1 = {2,1,3,4}
num2 = {1,2,3,4,5}

print("Union :", num1.union(num2))
# Union : {1, 2, 3, 4, 5} (Merge)

# Intersection

print("Intersection :",num1.intersection(num2))
# Intersection : {1, 2, 3, 4} (Common Value)
