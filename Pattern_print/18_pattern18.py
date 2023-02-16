"""
* * 
* * * * * 
* * 
* * 
* * * * * * * * * * 
* * 
* * 
* * 
* * * * * * * * * * * * * * * 
* * 
* * 
* * 
* * 

"""
n=4
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        for k in range(1,2+1,1):
            print("*",end="")
        print("")
    
    if i == n :
        break

    for l in range(1,i*5+1,1):
        print("*",end="")
    print("")
