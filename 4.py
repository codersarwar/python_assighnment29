#4. Write a Python script to store a list of city names in a file ‘cities.txt’
def fil(fname,mode,a):
    f=open(fname,mode)
    f.write(a)
   
    
    print(f)
a=input("enter a city name")
if(fil("cities.txt","a",a)):
    print("successfully created and inserted data")
