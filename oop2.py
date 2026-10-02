# # Public Attributes & Methods
# class Account:
#     def __init__(self, acc_num, acc_pass):
#         self.account_number = acc_num
#         self.account_password = acc_pass

# acc1 = Account("123456789","Password@123")
# print(acc1.account_number)
# print(acc1.account_password)


# Private Attributes & Methods
class Account:
    def __init__(self, acc_num, acc_pass):
        self.account_number = acc_num # Public
        self.__account_password = acc_pass # Private

acc1 = Account("123456789","Password@123")
print(acc1.account_number)
print(acc1.__account_password)