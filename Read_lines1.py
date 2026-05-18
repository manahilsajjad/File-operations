file = open('Hello.txt','r')
print(file.read())
file.close()

file = open('Hello.txt','r')
print("\n Read in parts \n")
print(file.read(10))
file.close()

file=open('Hello.txt','a')
file.write(" Hi! I am learning file handeling in python.")
file.close()