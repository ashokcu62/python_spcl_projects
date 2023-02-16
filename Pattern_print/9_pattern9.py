"""
* * * * * 
*
*
* * * * * * * * * * 
*
*
*
*
* * * * * * * * * * * * * * * 
*
*
*
*
*
*

"""
n = 3
for i in range(1, n+1, 1):
    for j in range(1, i*4+1, 1):
        print("*", end="")
    print("")

    for k in range(1, i*2+1, 1):
        print("*")
