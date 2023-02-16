"""
* * * 
* * * 
*
* * * * * * 
* * * * * * 
*
*
* * * * * * * * * 
* * * * * * * * * 
*
*
*
* * * * * * * * * * * * 
* * * * * * * * * * * * 
*
*
*
*
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 

"""

n=5
for i in range(1,n+1,1):
    for g in range(1,2+1,1):
        for k in range(1,i*3+1,1):
            print("*",end="")
        print("*")
    if i==n:
        break
    for l in range(1,i+1,1):
        print("*")
