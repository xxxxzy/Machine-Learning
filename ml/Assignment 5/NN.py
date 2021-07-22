import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'   #only show warning and error

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()   #tensorflow2.0 transfer to 1.0

import numpy as np
import matplotlib.pyplot as plt


#使用numpy生成200个随机点（样本点）
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]      #使用numpy生成200个随机点，[:, np.newaxis]增加维度（x_data 是一个200行1列的数据）
noise = np.random.normal(0, 0.02, x_data.shape)         #生成随机噪声干扰项（形状同x_data）  
y_data = np.square(x_data) + noise               #构造类似于二次函数的点图形


#定义两个placeholder #有点像x[],先占两个位置
x = tf.placeholder(tf.float32, [None, 1])    #x、y的维度为任意行，1列（根据样本来定义的维度）
y = tf.placeholder(tf.float32, [None, 1])


#定义神经网络隐藏层L1（该神经网络的神经元数量为（1-10-1））
Weights_L1 = tf.Variable(tf.random_normal([1, 10]))    #随机产生10个权重
Biases_L1 = tf.Variable(tf.zeros([1, 10]))    #0初始化偏向
Wx_plus_B_L1 = tf.matmul(x, Weights_L1) + Biases_L1    #L1层进行加权求和  #matmul矩阵相乘
L1 = tf.nn.tanh(Wx_plus_B_L1)   #根据非线性方程（双曲正切函数）转化输出  #Activation function


#定义神经网络输出层
Weights_L2 = tf.Variable(tf.random_normal([10, 1]))  
Biases_L2 = tf.Variable(tf.zeros([1, 1]))   
Wx_plus_B_L2 = tf.matmul(L1, Weights_L2) + Biases_L2    #将L1的输出作为输出层的输入
prediction = tf.nn.tanh(Wx_plus_B_L2)         #预测值
print(prediction)

#定义二次代价函数
loss = tf.reduce_mean(tf.square(y - prediction))
#使用随机梯度下降法进行训练，使得二次代价函数最小
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
#初始化参数
init = tf.global_variables_initializer()
#定义会话
with tf.Session() as sess:
    sess.run(init)
    for _ in range(2000):     #进行2000次训练学习
        sess.run(train_step, feed_dict = {x:x_data, y:y_data}) 
    #获得预测值
    prediction_value = sess.run(prediction, feed_dict = {x:x_data})
#    print(prediction_value)
    #画图
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.plot(x_data, prediction_value, 'red', lw = 5)    
    plt.show()