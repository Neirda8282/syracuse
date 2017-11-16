def syracuse(x):
    L=[x]
    C=1
    while x>1:
        if x%2==0:
            x=x/2
        else : 
            x=3*x+1
        C+=1
        L.append(x)
    return (L,C)

#print(syracuse(7))
#print(syracuse(137))
r=3
max=syracuse(3)[1]
for i in range (3,301):
   
    
    if syracuse(i)[1]>max:
        max=syracuse(i)[1]
      
        r=i
        
print(max,r)

print(syracuse(129)[1],syracuse(231)[1])



