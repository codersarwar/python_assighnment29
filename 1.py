#1. Write a Python script to print the following status of a file:
#a. Whether a file is read only
#b. Whether a file is closed or not
#c. Which file opening mode is used
#d. Name of the file
w=open("ts.txt","w")
a=open("ts.txt","a")
b=open("ts.txt","r")
print(w)
w.close()


