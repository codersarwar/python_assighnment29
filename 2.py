#2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

#This programm is wroking succesfully if i run this program then have seen None

def cretfile(filename,text):
  f=open(filename,"w")
  f.write(text)
  f.close()
if(print(cretfile("myfile.txt","WORLD"))):
    print("successfully created")

