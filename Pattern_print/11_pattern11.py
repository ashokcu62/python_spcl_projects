"""
*******
**   **
* * * *
*  *  *
* * * *
**   **
*******


"""

n=7
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i==1 or i==7 or j==1 or j==7 or j+i==n+1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")