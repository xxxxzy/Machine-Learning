import numpy as np


data1 = np.loadtxt('/Users/xuzhaoyang/Desktop/parkinsonsTrainStatML.dt')
data2 = np.loadtxt('/Users/xuzhaoyang/Desktop/parkinsonsTestStatML.dt')

Data_TrainOutput = data1[:,22]
Data_TrainIutput = np.delete(data1,22,axis=1)
Data_TestOutput = data2[:,22]
Data_TestIutput = np.delete(data2,22,axis=1)

def F_norm(Data_TrainIutput,Data_TestIutput):
    
    TrainMean=np.mean(Data_TrainIutput,axis=0) #mean of the train data
    TrainVar=np.var(Data_TrainIutput,axis=0) #variance of the train data
    TrainStd=np.std(Data_TrainIutput,axis=0) #standard deviation of the train data

    
    F_norm=(Data_TestIutput-TrainMean)/TrainStd #f_norm

    
    Norm_mean=np.mean(F_norm,axis=0)
    Norm_var=np.var(F_norm,axis=0)
    print(Norm_mean,Norm_var)
    
    print(TrainMean,TrainVar)

    
    return Norm_mean,Norm_var

F_norm(Data_TestIutput)

    
    