import numpy as np
import random
import math

#generate random x,y
def genData():
    
    x = np.zeros(shape=(10,2))
    y = np.zeros(shape=10)
    
    for i in range(0,10):
        
        x[i][0] = 1
        x[i][1] = i
        
        y[i] = random.randint(0,1)

    d1 = np.ones((1,10))*1   
    x1 = np.hstack((x,d1.T))
   
    return x1,y

#gradient descent
def gradientDescent(x1,y):
    
    
    eta = 0.005
    t = 10
    w = np.array([0,0,0])
    
    for i in range(0,t):
        
        loss = np.zeros(shape=(10,3))
        
        for j in range(0,10):
             
            hypothesis = np.dot(w,x1[j].T)
            loss[j] = np.dot(y[j],x1[j])/(1 + math.exp(np.dot(y[j],hypothesis)))
        
        gradient = loss.sum(axis=0)/(-10)
        print(gradient)
            
        w = w - eta * gradient
        
        print(w)
    
    return w