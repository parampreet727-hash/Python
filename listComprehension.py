# Statement 1
num = [1,2,3,4,5]
sqr = []

for n in num:
    sqr.append(n**2)
print(sqr)

# Statement 2
num = [1,2,3,4,5,6,7,8,9,10]
sqr = [n**2 for n in num]
print(sqr)

# Statement 3
num = [1,2,3,4,5,6,7,8,9,10]
sqr = [n**2 for n in num if n % 2 == 0]
print(sqr)

# Statement 4
chars = [char for char in "Parampreet"]
print(chars)

# Statement 5
nums = [n for n in range(10) if n % 2 == 0]
print(nums)

