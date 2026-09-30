 # File Read

f = open("text.txt","r")
data = f.read()
print(data)
f.close()

# File Write

f = open("text.txt","w")
f.write("Hi")
f.write("\nMy name is Parampreet Singh.")
f.close()

# File Append
f = open("text.txt","a")
f.write("\nAppending a new line to the file.")
f.close()