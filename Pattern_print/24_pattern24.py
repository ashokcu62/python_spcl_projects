"""
* * * 
* * * 
*
*
*
* * * * * * 
* * * * * * 
*
*
*
* * * * * * * * * 
* * * * * * * * * 
"""

n=3
for i in range(1,n+1,1):
    for j in range(1,n,1):
        for k in range(1,n*i+1,1):
            print("*",end="")
        print("")
    if i == n :
        break
    for l in range(1,n+1,1):
        print("*")