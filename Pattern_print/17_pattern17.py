"""
* * * * 
*
* * * * * * * * 
*
*
* * * * * * * * * * * * 
*
*
*
* * * * * * * * * * * * * * * * 


"""
n=4
for i in range(1,n+1,1):
    for j in range(1,i*4+1,1):
        print("*",end="")
    print("")

    if n == i:
        break
    
    for k in range(1,i+1,1):
        print("*")