from tensorflow.examples.tutorials.mnist import input_data

class Classifier(object):
    def __init__(self, layers):
        self.layers = layers
        self.mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
