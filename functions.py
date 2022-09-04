# #python functions

# from cmath import sqrt
# from re import X


# myList = [1,2,3,4,5]
# def myLen(x):
    
#     n =0
#     for i in x:
#         n = n+1

#     return n

# y = myLen(myList)
# print(y)

# ####
# myList = [1,2,3,4,5]
# mytuple = (1,2,3,4,5)
# def myLen(x):
    
#     n =0
#     for i in x:
#         n = n+1

#     return n

# y = myLen(mytuple)
# print(y)
#########
from math import sqrt

def q_e_solver(a,b,c):
    d = b**2 - 4*a*c
    if d<0:
        return None
    elif d==0:
        x = -b /(2*a)
        return x
    else:
        
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
    return x1, x2

print(q_e_solver(2,3,-3)) 

