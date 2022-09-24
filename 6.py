#5. Write a Python script to append list of city names in a file ‘cities.txt’
from asyncore import read

#The program is not working there is no error but not coming output


def search(fname, word):
    
    try:
        
     f=open(fname,"r")
     line_count=0
     for line in f.readlines():
        line_count +=1
        print(line_count)
     strlist=line.split(' ')
     word_count=0
     for w in strlist:
         
         word_count+=1
         print(word_count)
     if(word==w):
        return(line_count,word_count)
     else:
      print("none") 
    except:
      print("o ho erroe")  
search("cities.txt","m")