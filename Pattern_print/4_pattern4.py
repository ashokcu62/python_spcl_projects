"""
*
* * * * 
*
*
* * * * * * * * 
*
*
*
* * * * * * * * * * * * 

"""

n=3
for i in range(1,n+1,1):

    for j in range(1,i+1,1):
        print("*")
    

    for k in range(1,i*4+1,1):
        print("*",end="")
    print("")
   
#    end="" takes values prints showing togather  so it appends a last line in its own line 
#  thats why add a print("") after the the second loop
    
    