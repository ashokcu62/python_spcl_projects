"""
* * 
*
* * * * 
*
*
*
* * * * * * * * 
*
*
*
*
*
"""
n=3
p=2
c=1
for i in range(1,n+1,1):
    for j in range(1,i*p+1,1):
        print("*",end="")

    print("")
    p+=1

    for k in range(1,c+1,1):
        print("*")
    c+=2