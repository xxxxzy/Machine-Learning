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
    Train_pick1 = []
    Test_pick = []
    Val_pick = []
    
    digits = [5,6]
    Num_Test = 0
    Num_Val = 0
    
#Train set1
    for i in range (0,8000):
        
        if (data2[i] in digits):
            
            Train_pick.append(i)
    

            
    data5 = data1[Train_pick]
    data6 = data2[Train_pick]
    
#Train set2
    for m in range (0,10000):
        
        if (data2[m] in digits):
            
            Train_pick1.append(m)
    

            
    data11 = data1[Train_pick1]
    data12 = data2[Train_pick1]
#    print(data11)
#Validation set    
    for n in range (8000,10000):
        
        if (data2[n] in digits):
            
            Val_pick.append(n)
            
    Num_Val = len(Val_pick)
            
    data9 = data1[Val_pick]
    data10 = data2[Val_pick]
            
#Test set    
    for j in range (0,2000):
        
        if (data4[j] in digits):
            
            Test_pick.append(j)
    
    Num_Test = len(Test_pick)
  
    data7 = data3[Test_pick]
    data8 = data4[Test_pick]
    
    return (data5,data6,data7,data8,data9,data10,data11,data12,Num_Test,Num_Val)




def KNN_Test(data11,data12,data7,data8,Num_Test):
    
    x = []
    y = []
    for k in range (1,34,2):

        c = 0
        d = 0
        
        for i in range (0,Num_Test):
            
#            h = data5.shape[0] #data5有几行
#            diff = np.tile(data7[i],(h,1)) - data5
#            i = 2
            distance_x = np.tile(data7[i],(data11.shape[0],1)) - data11 #Matrix subtraction
#            print(distance_x)
            square = distance_x ** 2
            disance = np.sum(square,axis=1) #Euclidean distance
            sequence = np.argsort(disance)
#            print(sequence)
            
            num = []
            a = 0
            b = 0
            
            for j in range (k):
                
                num.append(sequence[j])
             
            for m in range (len(num)):

                if data12[num[m]] == data8[i]:
                    
                    a = a + 1
                    
                else:
                    
                    b = b + 1
                    
            if a > b:
                
                c = c + 1 #times of right
                
            else:
                
                d = d + 1 #times of wrong
              
        l = d/(c+d)
        print (l)
        x.append(k)
        y.append(l)
        
    plt.plot(x,y)
    plt.show()        

        
    return (x,y)
        
        
def KNN_Val(data5,data6,data9,data10,Num_Val):

    x1 = []
    y1 = []
        
    for k in range (1,34,2):

        c = 0
        d = 0
        
        for i in range (0,Num_Val):
            
#            h = data5.shape[0] #data5有几行
#            diff = np.tile(data7[i],(h,1)) - data5
#            i = 2
            distance_x = np.tile(data9[i],(data5.shape[0],1)) - data5 #Matrix subtraction
            square = distance_x ** 2
            disance = np.sum(square,axis=1) #Euclidean distance
            sequence = np.argsort(disance)
            
            num = []
            a = 0
            b = 0
            
            for j in range (k):
                
                num.append(sequence[j])
             
            for m in range (len(num)):

                if data6[num[m]] == data10[i]:
                    
                    a = a + 1
                    
                else:
                    
                    b = b + 1
                    
            if a > b:
                
                c = c + 1 #times of right
                
            else:
                
                d = d + 1 #times of wrong
              
        l = d/(c+d)
        print (l)
        
        x1.append(k)
        y1.append(l)
        
      
    plt.plot(x1,y1)
    plt.show()

    print(x1)
    return (x1,y1)

def plot(x,y,x1,y1):
    
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.title('Figure 5:digitals in [5,6]',fontweight = 'heavy')
    plt.xlabel('K')
    plt.ylabel('Empirical loss')
    plt.legend(labels = ['test error','validation error'],loc = 'lower right')
    plt.savefig('5.1.png')
    plt.show()

    
    return ()
