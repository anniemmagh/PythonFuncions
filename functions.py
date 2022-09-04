#python functions
from tokenize import maybe


myList = [1,2,3,4,5]
def myLen(x):
    
    n =0
    for i in x:
        n = n+1

    return n

y = myLen(myList)
print(y)