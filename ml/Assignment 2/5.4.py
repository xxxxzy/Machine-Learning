import numpy as np
import math


data1 = np.loadtxt('/Users/xuzhaoyang/Desktop/IrisTrainML.dt.txt')
data2 = np.loadtxt('/Users/xuzhaoyang/Desktop/IrisTestML.dt.txt')


def remove(data1,data2):
    Train_pick = []
    Test_pick = []
    a = data1[:,2]
    b = data2[:,2]
    ran = [0,1]
#train set  
    for i in range(0,100):
        
        if (a[i] in ran):
            
            Train_pick.append(i)
            
            print(Train_pick)
            
    data3 = data1[Train_pick]

    data_y = data3[:,2]
    d1 = np.ones((1,62))*1
    data_x = np.hstack((np.delete(data3, 2, axis=1),d1.T))

#test set    
    for j in range(0,38):
        
        if (b[j] in ran):
            
            Test_pick.append(j)
        
    data4 = data2[Test_pick]
    
    data_ty = data3[:,2]
    d2 = np.ones((1,26))*1
    data_tx = np.hstack((np.delete(data4, 2, axis=1),d2.T))
    

    return (data_x,data_y,data_ty,data_tx)

def linerregression(data_x,data_y):
    
    w1 = np.dot(data_x.T,data_x)
    wI = np.linalg.pinv(w1) 
    w2 = np.dot(wI,data_x.T)
    w = np.dot(w2,data_y.T)
    print(w)
    
    return (w)




def gradient(data_x,data_y):
    
    w = np.array([0.53779839,-6.06028193,-0.54198853])
    eta = 0.01
        
        
    for i in range(0,10):
        
        loss = np.zeros(shape=(62,3))
        
        for j in range(0,62):
             
            hypothesis = np.dot(w,data_x[j].T)
            loss[j] = np.dot(data_y[j],data_x[j])/(1 + math.exp(np.dot(data_y[j],hypothesis)))
        
        gradient = loss.sum(axis=0)/(-62)
        print(gradient)
            
        w = w - eta * gradient
        
    print (w)
    
    return (w)
    
def testerror(w,data_ty,data_tx):
    
    d=0
    p=np.dot(w,data_tx.T)
    print(w)
    print(p)
    
    for i in range(0,26):
        
        if p[i] >= 0.5:
            
            p[i] = 1
            
        else:
            
            p[i] = 0
            
            
    for j in range(0,26):
        
        if p[j] == data_ty[j]:
            
            d = d+1
            
    print (d)
    return (d)
    
def trainerror(w,data_y,data_x):
    
    d=0
    p=np.dot(w,data_x.T)
    print(w)
    print(p)
    
    for i in range(0,62):
        
        if p[i] >= 0.5:
            
            p[i] = 1
            
        else:
            
            p[i] = 0
            
            
    for j in range(0,62):
        
        if p[j] == data_y[j]:
            
            d = d+1
            
    print (d)
    return (d)
    

            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      