import numpy 
import tensorflow as tf
a = numpy.array = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
print(numpy.shape(a))
a = numpy.reshape(a,(18,1))
t1 = tf.ones(shape=(3,3))
t2 = tf.reshape(t1, shape=(1,9))
print(t2)
print(t1)
