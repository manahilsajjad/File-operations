f1=open('Hello.txt','r')
f2=open('Bye.txt','w')

for line in f1.readlines():

    if not (line.startswith('Hello')):
        print(line)

f2.close()
f1.close()