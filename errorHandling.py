# try:
#     a = int(input("Enter a number :"))
#     b = 10/a
#     print("Result :",b)

# # except ValueError:
# #     print("Please enter a valid number")
# # except ZeroDivisionError:
# #     print("You can't divided by zero")

# except (ValueError,ZeroDivisionError):
#     print("Invaild Input")

try:
    num = int(input("Enter your age :"))
except ValueError:
    print("Invalid Input")
else:
    print("Your age is :", num)