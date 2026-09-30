# Lambda Function
add = lambda x,y : x + y
print("Lambda Function :",add(10,20))


# Normal Function
def add_fun (a,b):
    return a + b
print("Normal Function :",add_fun(5,10))

# Map using Lambda Function
num = [1,2,3,4,5,6,7,8,9,10]
sq_num = list(map(lambda x: x**2, num))
print(sq_num) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Filter using Lambda Function
number = [1,2,3,4,5]
evens = list(filter(lambda x : x % 2 == 0, number))
print("Even Number :",evens) #Even Number : [2, 4]

#Reduce using Lambda Function
from functools import reduce
reduce_num = [1,2,3,4]
total_num = reduce(lambda x, y: x + y, reduce_num)
print(total_num)