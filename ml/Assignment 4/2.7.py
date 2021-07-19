import math

for n in range(15000000,10**11):
    
    d = 11 #define d_vc
    
    a = (10 ** (-4))/8 
    b = a * n #f(x)


    a1 = 2 ** (d+1) 
    b1 = n ** (d)  
    c1 = a1*b1+2
    e1 = c1*100 #g(x)
    
    if b>= math.log(e1):
        print (n,b,math.log(e1))
        
        break
