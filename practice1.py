# Largest Number

a = 15
b = 27
c = 9

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# List Sum

numbers = [4, 7, 2, 9, 1, 6]

total = 0

for number in numbers:
    total = total + number

print(total)

# Loop 
for i in range(1, 11):
    if i % 2 == 0:
        print("Even")
    else:
        print(i)


# Even or Odd
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
