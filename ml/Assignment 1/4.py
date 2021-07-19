import numpy as np
import matplotlib.pyplot as plt
#import operator
#import os
#from datetime import datetime
#from numpy import *



data1 = np.loadtxt('/Users/xuzhaoyang/Desktop/MNIST-Train-cropped.txt').reshape(10000,784)
data2 = np.loadtxt('/Users/xuzhaoyang/Desktop/MNIST-Train-Labels-cropped.txt')
data3 = np.loadtxt('/Users/xuzhaoyang/Desktop/MNIST-Test-cropped.txt').reshape(2000,784)
data4 = np.loadtxt('/Users/xuzhaoyang/Desktop/MNIST-Test-Labels-cropped.txt')
data2 = np.transpose(data2)
data4 = np.transpose(data4)



#Preparation
def Pre_plot():
    
#    a = np.asmatrix(data1)  #change into matrix
    b = data1[0]  #choose column
    c = np.reshape(b,(28,28)) #reshape into 28*28
    d = np.transpose(c) #transpose matrix
    f = data2[0]
    print(f)
    plt.imshow(d)
    
    return plt.imshow(d)
    





def choosedigits():
    
    Train_pick = []
    Test_pick = []
    digits = [0,8]
    Num = 0
    for i in range (0,10000):
        
        if (data2[i] in digits):
            
            Train_pick.append(i)
    
    print(Train_pick)
            
    data5 = data1[Train_pick]
    data6 = data2[Train_pick]
    
    for j in range (0,2000):
        
        if (data4[j] in digits):
            
            Test_pick.append(j)
    
    Num = len(Test_pick)
    
    data7 = data3[Test_pick]
    data8 = data4[Test_pick]

    print(Num)
    
    return (data5,data6,data7,data8,Num)




def KNN(data5,data6,data7,data8,Num):
    
    for k in range (1,34,2):

        c = 0
        d = 0
        
        for i in range (0,Num):
#            h = data5.shape[0] #data5有几行
#            diff = np.tile(data7[i],(h,1)) - data5
#            i = 2
            distance_x = np.tile(data7[i],(data5.shape[0],1)) - data5 #Matrix subtraction
            square = distance_x ** 2
            disance = np.sum(square,axis=1) #Euclidean distance
            sequence = np.argsort(disance)
            
            num = []
            a = 0
            b = 0
            
            for j in range (k):
                
                num.append(sequence[j])
             
            for m in range (len(num)):

                if data6[num[m]] == data8[i]:
                    
                    a = a + 1
                    
                else:
                    
                    b = b + 1
                    
                    
            if a > b:
                
                c = c + 1 #times of right
                
            else:
                
                d = d + 1 #times of wrong
              
#            if data9 == data8[i]:
              
#                c = c + 1
            
#            else:
                
#                d = d + 1
                             
#            print(data9)
        print(c,d)
        
        return()
            
            
            
            
'''           
            
            
            print(sequence)
                      
            Count = {} #change into dic
            
            for m in range(1):
                
                guesslabel = data6[sequence[m]]
                Count[guesslabel] = Count.get(guesslabel,0)+1
                
#               break
            print (Count)
        
            
        maxcount = 0
        maxindex = 0
        loss = 0
        
    
        for key,value in Count.items():
            
            if value > maxcount:
                    
                maxcount = value
                maxindex = key
#        print(maxindex,maxcount)
                
        for j in range (0,Num):
                    
            if maxindex == data8[j]:
                
                loss = 0
            else:
                loss = loss + 1
            
        print(loss)
            
        
        return 
'''               
                
