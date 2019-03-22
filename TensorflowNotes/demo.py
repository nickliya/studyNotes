import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def add_layer(inputs, in_size, out_size, activation_function=None):
    """
    添加神经层
    :param inputs:  传入数据
    :param in_size: lian
    :param out_size:
    :param activation_function: 激励函数，默认None
    :return:
    """

    # 权重，in_size行，out_size列
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    # 最后返回是个列表
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    # 做运算
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
predition = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition), reduction_indices=[1]))

# 优化
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(100):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 25 == 0:
        print(sess.run(train_step, feed_dict={xs: x_data, ys: y_data}))
