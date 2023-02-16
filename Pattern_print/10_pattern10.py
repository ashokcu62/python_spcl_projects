"""
*
* * 
*
*
*
* * * * 
*
* * * * * * 
*
*
*
* * * * * * * * 


"""
n=4
u=1
for i in range(1,n+1,1):
    for j in range(1,1*u+1,1):
        print("*")
    

    u+=2
    if u>4:
        u=1
    for k in range(1,2*i+1,1):
        print("*",end="")
    print("")
    