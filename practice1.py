# # Largest Number

# a = 15
# b = 27
# c = 9

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# #Method : List Sum

# numbers = [4, 7, 2, 9, 1, 6]

# total = 0

# for number in numbers:
#     total = total + number

# print(total)

# # Method : Loop 
# for i in range(1, 11):
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print(i)


# # Method: Even or Odd
# number = 7

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Method 1: Find the Missing Number

numbers = [1, 2, 3, 5, 6]

for i in range(1, 7):
    if i not in numbers:
        print("Missing number:", i)


# Method 2: Using the sum formula

numbers = [1, 2, 4, 5, 6]

n = 6

expected = n * (n + 1) // 2
actual = sum(numbers)

missing = expected - actual

print("Missing number:", missing)

# Method 1: Find the Missing Number

numbers1 = [1, 2, 3, 4, 6, 7, 8, 9]

for j in range(1, 7):
    if j not in numbers1:
        print("Missing number:", j)

# Python Program: Palindrome Number

n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# Find duplicates: Find duplicate elements in [1, 2, 3, 2, 4, 1].

numbers = [1, 2, 3, 2, 4, 1]

duplicates = []
seen = set()

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.add(num)

print("Duplicates:", duplicates)