#1.29
from tensorflow import keras
from keras.models import Sequential #sequential is we feeding it forward  顺序是我们将它向前传递
from keras.layers import Dense


# nn.py is Neural Network 神经网络

#Dense：这是一个普通的全连接神经网络层。
#Dense 实现以下运算：output = activation(dot(input, kernel) + bias)，其中 activation 是作为 activation 参数传递的逐元素激活函数，kernel 是该层创建的权重矩阵，bias 是该层创建的偏置向量（仅当 use_bias 为 True 时适用）。当此层后接 BatchNormalization 层时，建议将 use_bias 设置为 False，因为 BatchNormalization 层本身就有偏置项。
#注意：如果该层的输入秩大于 2，Dense 会计算输入和核沿输入的最后一个轴和核的第 0 轴的点积（使用 tf.tensordot）。例如，如果输入维度为 (batch_size, d0, d1)，则我们创建一个形状为 (d1, units) 的核，该核沿输入的第二个轴对每个形状为 (1, 1, d1) 的子张量进行运算（共有 batch_size * d0 个这样的子张量）。在这种情况下，输出的形状为 (batch_size, d0, units)


# we want to got the Random numbers
# so in order to predicts these random numbers
# we have two things to competing:

# 1. generator 会一直不断的生成数字 generate numbers 
# 2. Discriminator  <- This  这个discriminator会筛选出不要的数字 告诉generator说这不是我要的数字 this is to stop these numbers if they are not real 




#look at the 'IBM deep neural network picture' and to match the input layer, hidden layers and output layers

def build_discriminator(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']):
    model = Sequential() #we create the model and call it Sequential because we import it,is a back forward 
    
#optimizer is a function whether the neural should be activated or not,
#adam is used as a default optimizer优化器

#loss is a function, how we measure, how good it is, how well is doing
#so we choose the default one 'binary_crossentropy'

#metrics is what we want to measure, it should be a list
#accuracy is what we want to measure by default 


    # Input layer
    model.add(Dense(128, activation = 'relu', input_shape=(1,))) 
    #1 means one blue circle from the 'IBM deep neural network picture'
    #128 neural means we will have 128 circles for next layer, our first hidden layer, usually start with 128 this number 
    #relu is suitable for 1 put in 1 out, 
    #relu is check what it has received, and if it is 负数 negative number it will change into 0, if is positive 正数 it will leave the number and activate
#########if we want to improve the accuracy, we can look at the generator, or we can change from discriminator like change '128' this number, maybe another optimizer, or maybe other loss, 


    # Hidden layers
    model.add(Dense(64, activation = 'relu'))
    #this time we choose 64 neural
    model.add(Dense(32, activation = 'relu'))
    #next one we choose 32 neural


    # Output layer
    model.add(Dense(1, activation = 'sigmoid'))
    #because we input 1 value, so we want to output 1 value, or less than the input value
    #sigmoid work like pushing the rock up to hill and reach the peak it slopes down instead
    model.compile(optimizer=optimizer, loss=loss, metrics = metrics)

    return model