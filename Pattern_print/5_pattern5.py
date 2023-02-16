"""

* * * 
*
*
*
* * * * * * 
*
*
*
*
*
*
* * * * * * * * *

"""
n=3
for i in range(1,n+1,1):

    for k in range(1,i*3+1,1):
        print("*",end="")
    print("")

    if n==i:
        break
    for j in range(1,i*3+1,1):
        print("*")
