import tensorflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None):
    """
    :param inputs:  传入数据
    :param in_size:
    :param out_size:
    :param activation_function: 激励函数，默认None
    :return:
    """

    Weights = tf.Variable(tf.random_normal([in_size, out_size]))