#9. Write a Python script to store book data in a file. Book data is in the form of a
#dictionary in which book name is the key and price is its value. Use pickle to store
#data into a file (say bookfile)

import pickle
student={'1':'sarwar','2':'hoain'}
f=open("kk.txt","ab")
pickle.dump("student",f)
f.close()

