read= open('Hello.txt','r')
print("File in read mode...")
print(read.read())
read.close()

write= open('Hello.txt','w')
write.write("File in write mode...")
write.write("Hello whats your name?")
write.close()

a=open('Hello.txt','a')
a.write("\n File in append mode...")
a.write("Whats you hobby??")
a.close()