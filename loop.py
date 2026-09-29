# While Loop

i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop End!")

j = 1
while j <= 5:
    print(j)
    j += 1


k = 50
while k <= 100:
    print(k)
    if k == 60:
        break
    k += 1
print("Break : 60")


x = 50
while x <= 55:
    if x == 53:
        x += 1
        continue
    print(x)
    x += 1
print("Continue skip : 53")