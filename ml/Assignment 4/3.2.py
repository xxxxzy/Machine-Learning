import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def F_norm():
    
    data1 = np.loadtxt('/Users/xuzhaoyang/Desktop/parkinsonsTrainStatML.dt')
    data2 = np.loadtxt('/Users/xuzhaoyang/Desktop/parkinsonsTestStatML.dt')
    
    y_Train = data1[:,22]
    x_Train = np.delete(data1,22,axis=1)
    y_Test = data2[:,22]
    x_Test = np.delete(data2,22,axis=1)
    
    TrainMean=np.mean(x_Train,axis=0)
    TrainVar=np.var(x_Train,axis=0)
    TrainStd=np.std(x_Train,axis=0)
    
    F_norm1=(x_Train-TrainMean)/TrainStd
    
    return(y_Train,y_Test,x_Test,F_norm1)

  

def Grid_search():
    
    param_grid = {"gamma":[0.001,0.01,0.1,1,10,100],"C":[0.001,0.01,0.1,1,10,100]}
    
    grid_search = GridSearchCV(SVC(kernel='rbf'),param_grid,cv=5) 
    X_Train,X_Test,Y_Train,Y_Test = train_test_split(F_norm1,y_Train,random_state=0)
    grid_search.fit(X_Train,Y_Train) 
    
    print("Best parameters:{}".format(grid_search.best_params_))
    
    return

def error(y_Train,F_norm1):
    
    clf = SVC(C=1, kernel='rbf', gamma=0.01, decision_function_shape='ovo')
    clf.fit(F_norm1, y_Train)
    
    y_pre = clf.predict(F_norm1)
    
    num=0
    for i in range(97):
        
        if y_pre[i] == y_Train[i]:
            
            num=num
            
        else:
            
            num=num+1
            
            
    print(num)
    
    return
             
        
    
    
    
    
    
    
    
    
    
    
    