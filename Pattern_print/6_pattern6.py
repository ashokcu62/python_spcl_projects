"""
* * * * * * * * * * 
*
* * * * * * * * 
*
*
* * * * * * 
*
*
*
* * * * 
*
*
*
*
* * 
*
*
*
*
*

"""

n=5
u=10
for i in range(1,n+1,1):
    for k in range(1,u+1,1):
        print("*",end="")
    u-=2
    print("")
    for j in range(1,i+1,1):
        print("*")