import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('/Users/xuzhaoyang/Desktop/DanWood.dt')
print(data)

#6.1

a = data[:,0]
b = data[:,1]

print(a)

def regression_parameters(a,b):
    
    x_T = np.mat(a) #shape (1,6)
    y = np.mat(b) #shape (1,6)
#   x = np.transpose(x_T) #shape (6,1)
#   y_T = np.transpose(y) #shape (6,1)
    X = np.column_stack((x_T.T,[1,1,1,1,1,1])) #shape (6,2)
#   X_T = np.transpose(X) #shape (2,6)
    w1 = np.dot(X.T,X)
#   print (w1.I) #Inverse matrix
    wI = np.linalg.pinv(w1) #Pseudo inverse matrix
    w2 = np.dot(wI,X.T)
    w = np.dot(w2,y.T)
#    print (w)
    
    return w,X,y


#6.2

def MSE_model(w,X,y):
    
    print(y)
    j = np.array(y - np.dot(w.T,X.T))
    MSE = sum(sum([c**2 for c in j])) / len(a)
    print (MSE)
    
    return MSE


#6.3
    
def regression_plot(w,a,b):
    
    x_line=np.arange(1,2,0.0001)
    y_line=np.arange(2,6,0.0001)  
    
    y_line = int(w[0]) * x_line + int(w[1])
    
    plt.plot(x_line,y_line,'yellow')
    plt.scatter(a,b)

    plt.title('Figure 6 ',fontweight = 'heavy')
    plt.xlabel('absolute temperature(x)')
    plt.ylabel('radiated energy')
    plt.legend(labels = ['Regression','Datapoints'],loc = 'upper left')
    
    plt.savefig('6.png')
    plt.show()
    
    return ()


#6.4
    
print(np.var(b))
    
    
#6.5
    
def Phi(a):
    
    n = 3
    
    return (a**n)

x2 = Phi(a) #transformed x to x^3
print (x2)


def main(y,x2,b):
    
    w1 = regression_parameters(x2,b)[0] #parameters
    print(w1)
    
    MSE1 = MSE_model(w1,regression_parameters(x2,b)[1],regression_parameters(x2,b)[2])
    print (MSE1) #MSE

    x_line=np.arange(2,5,0.0001)
    y_line=np.arange(2,6,0.0001)  
    
    y_line = int(w1[0]) * x_line + int(w1[1])
    
    plt.plot(x_line,y_line,'yellow')
    plt.scatter(x2,b)

    plt.title('Figure 7 ',fontweight = 'heavy')
    plt.xlabel('absolute temperature(x^3)')
    plt.ylabel('radiated energy')
    plt.legend(labels = ['Regression','Datapoints'],loc = 'upper left')
    
    plt.savefig('7.png')
    plt.show()
    return ()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      