#3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

def file(fname,mode):
    f=open(fname,mode)
    print(f.read())
file("myfile.txt","r")

