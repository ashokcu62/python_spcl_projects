"""
* * * * * 
*
* * * * * 
*
*
* * * * * 
*
*
*
* * * * * 
*
*
*
*
* * * * * 


"""
n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print("*",end="")
    print("")
    if i == n:
        break
    for k in range(1,i+1,1):
        print("*")
    