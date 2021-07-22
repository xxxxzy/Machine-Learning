# Machine-Learning
Course: Machine Learning
## Assignment 1
### K-NN
The program implements K-NN classification algorithm with data MNIST.

It compare K-NN algorithms for K = 1, 3, 5, 7, . . . , 33 in their ability to distinguish between digits “0” and “1”.

And then repeat the same for “0” and “8”. Repeat the same for “5” and “6”.
### Linear regression
The program also implements linear regression with data DanWood.

It builds an affine linear model h : R → R of the data described above using linear regression. Report the two parameters of the model as well as the mean-squared-error of the model computed over the complete data set. It also computes the variance of the labels in the training data set.

Then the program fit a non-linear model:

![](http://latex.codecogs.com/svg.latex?h(x)=ax^3+b)
### Theoretical part
Markov’s and Chebyshev’s Inequalities.

## Assignment 2
### Logistic regression
The program implements logistic regression model(page 95 in Abu-Mostafa et al. (2012)). Then apply logistic regression to the Iris flower data. It solves a binary classification task. The program can output the training and test error as measured by the 0-1 loss and three parameters of the (affine) linear model.
### Theoretical part
Hoeffding’s Inequality
## Assignment 3
### Theoretical part
Occam’s Razor:

Report derives high-probability bounds for different hypothesis sets.

Kernel:

First, Report proves the distance of two kernels in Reproduce Kernel Hilbert Space, which can be used to implement a kernel nearest-neighbor algorithm directly.

Second, it proves the sum of kernels is a positive-definite, if both of them are positive-definite kernels. It can help to familiar with the basic definition of the important concept of positive definiteness.

Third, it proves an upper bound on the rank of the Gram matrix. It is important to understand the real dimensionality of learning problems using a linear kernel that why linear kernels are often treated differently in efficient implementations.

## Assignment 4
### Support Vector Machines
The program implements SVM by using LIBSVM. In this excercise, Gaussian kernels are used by the form,

![](http://latex.codecogs.com/svg.latex?k(x,z)=\exp(-\gamma||x-z||^2))
Then the program applied on the data Diagnosing Parkinson’s disease voice signals(Little et al. (2009)). It mainly consists of three parts,

Data normalization: Data normalization is an important preprocessing step. A basic normalization is to generate mean free, unit variance input data.

Model selection using grid-search: The performance of your SVM classifier depends on the choice of the regularization parameter C and the kernel parameters (here gamma). Adapting these hyperpa- rameters is referred to as SVM model selection.Use grid-search to determine appropriate SVM hyperparameters gamma and C.

Inspecting the kernel expansion: A support vector x_i is bounded if the corresponding coefficient in the kernel expansion (usually denoted by alpha_i) has an absolute value of C. If 0 < alpha_i < C then the support vector is free. 
### Theoretical part
Growth function and VC-dimension.

## Assignment 5
### Random Forest
The random forest is a classification algorithm consisting of many decisions trees. It uses bagging and feature randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.（from wiki）

### Neural Networks
The program also implements a basis Neural Networks by tensorflow.




