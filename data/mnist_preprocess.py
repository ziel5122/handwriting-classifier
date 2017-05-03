import idx2numpy
from numpy import vstack
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('./MNIST', one_hot=True)

mnist_images = vstack((mnist.train.images, mnist.test.images,
    mnist.validation.images))
mnist_labels = vstack((mnist.train.labels, mnist.test.labels,
    mnist.validation.labels))

print(mnist_images[0])

'''
idx2numpy.convert_to_file('./MNIST/mnist-images.idx', mnist_images)
idx2numpy.convert_to_file('./MNIST/mnist-labels.idx', mnist_labels)

print('images:', len(mnist_images), '/ labels:', len(mnist_labels))
'''
