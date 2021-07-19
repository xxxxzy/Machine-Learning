import matplotlib.pyplot as plt
#import random
import numpy as np

#2.1
def main():

    T_all = 1000 # times of repetitions of experiment
    T_exp = []
    P_up = []
    N_up = 0 #times of show up

    for i in range(1,T_all):
        
        N_1 = np.random.binomial(20,0.05,1) #Bernoulli
        N_up = N_up + N_1  
        N_all = 20*i
        
        P_up.append(N_up/N_all)
        T_exp.append(i)
        
    plt.plot(T_exp,P_up,'blue')
    plt.title('Figure 1', fontweight = 'heavy')
    plt.xlabel('times of experiment')
    plt.ylabel('frequency of show up')
    plt.savefig('1.png')
    plt.show()

if __name__ == '__main__':
    main()



def main():
 
#2.2
    
    T_all = 1000000
    N_2 = np.random.binomial(20,0.5,T_all)
    L_2 = N_2.tolist() #change into list
    
    alpha = []
    P_up1 = []
    
    for i in range (10,20):
        
        a = [x for x in L_2 if x >= i]
        N_want = len(a)
       
        P_up1.append(N_want/T_all)
        alpha.append(i/20)
    
    plt.plot(alpha,P_up1,'green')
    plt.show()
        
#2.3
    
    P_up2 = []

    for i in range (10,20):
        
        alpha1 = i/20
        P_up2.append(10/(20*alpha1))
        
    plt.plot(alpha,P_up2,'red')
    plt.show()
        
#2.4
    
    P_up3 = []
    
    for i in range (10,20):
        
        alpha2 = i/20
             
        if 20*(alpha2 - 0.5)**2 <= 0.25:
            
            P_up3.append(1)
            
        else:
                
            P_up3.append(1/(20*4*(alpha2-0.5)**2)) 
        
    
    plt.plot(alpha,P_up1,'green',alpha,P_up2,'red',alpha,P_up3,'yellow')
    plt.title('Figure 2',fontweight = 'heavy')
    plt.xlabel('alpha')
    plt.ylabel('probability')
    plt.legend(labels = ['frequency of observing','Markov bound','Chebyshev bound'],loc = 'upper right')
    plt.savefig('2.png')
    plt.show()
        
if __name__ == '__main__':
    main()






    