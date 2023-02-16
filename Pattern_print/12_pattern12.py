"""
* 
* 
* * * 
* * 
* * 
* * * * * * 
* * * 
* * * 
* * * * * * * * *


"""
n=3
for i in range(1,n+1,1):
    for m in range(1,3,1):
        for j in range(1,i+1,1):
            print("*",end="")
        print("")

    for k in range(1,i*3+1,1):
        print("*",end="")
    print("")