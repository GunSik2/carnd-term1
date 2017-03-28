import tensorflow as tf
import numpy as np

## Base
# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)


## Tensor
# A is a 0-dimensional int32 tensor
A = tf.constant(1234)
# B is a 1-dimensional int32 tensor
B = tf.constant([123,456,789])
 # C is a 2-dimensional int32 tensor
C = tf.constant([ [123,456,789], [222,333,444] ])

with tf.Session() as sess:
    output = sess.run(fetches=[A, B, C])
    print(output)


##  Input
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)
with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
    print(output)

    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)

## Math
x = tf.add(5, 2)  # 7
y = tf.subtract(10, 4) # 6
z = tf.multiply(2, 5)  # 10
with tf.Session() as sess:
    output = sess.run(fetches=[x, y, z])
    print(output)

## Converting types
x = tf.subtract(2.0, 1) # tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1
with tf.Session() as sess:
    output = sess.run(x)
    print(output)


## Variable: Tensor that can be modified.
## This tensor stores its state in the session, so you must initialize the state of the tensor manually.
x = tf.Variable(5)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)


## Softmax
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    print("sum = ", np.sum(np.exp(x)), ", type = ", type(np.sum(np.exp(x))))
    print("sum (axis=0) = ", np.sum(np.exp(x), axis=0), ", type = ", type(np.sum(np.exp(x), axis=0)))

    return np.exp(x) / np.sum(np.exp(x), axis=0)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))
