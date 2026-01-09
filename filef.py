f = open ("test.txt","w")

f.write("Hello, This is Python.\n")
f.write("I can write Python code. \n")

f.close()

f = open("test.txt","r")

content = f.read()
print(content)

f.close()
