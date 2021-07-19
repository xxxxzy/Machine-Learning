import matplotlib.pyplot as plt
import numpy as np
import math

def main():
 
#Assignment 1
    
    T_all = 1000000
    N_2 = np.random.binomial(20,0.5,T_all)
    L_2 = N_2.tolist() #change into list
    
    alpha = []
    P_up1 = []
    
    for i in range (10,21):
        
        a = [x for x in L_2 if x >= i]
        N_want = len(a)
       
        P_up1.append(N_want/T_all)
        alpha.append(i/20)
        
    
    P_up2 = []

    for i in range (10,21):
        
        alpha1 = i/20
        P_up2.append(10/(20*alpha1))
        
    
    P_up3 = []
    
    for i in range (10,21):
        
        alpha2 = i/20
             
        if 20*(alpha2 - 0.5)**2 <= 0.25:
            
            P_up3.append(1)
            
        else:
                
            P_up3.append(1/(20*4*(alpha2-0.5)**2)) 
            
            
    P_up4 = []
    
    for i in range (10,21):
        
        alpha3 = i/20
        up = -(20*alpha3-10)**2
        
        P_up4.append(math.exp(up/10))
        P = math.exp(up/10)
        print(alpha3,P)
        
    #plt.plot(alpha,P_up4)
    #plt.show()
    
    plt.plot(alpha,P_up1,'green',alpha,P_up2,'red',alpha,P_up3,'yellow',alpha,P_up4,'blue')
    plt.xlabel('alpha')
    plt.ylabel('probability')
    plt.legend(labels = ['frequency of observing','Markov bound','Chebyshev bound','Hoeffding bound'],loc = 'upper right')
    plt.savefig('1.png')
    plt.show()
        
if __name__ == '__main__':
    main()


a=(1/2**20)*21
print(a)



    