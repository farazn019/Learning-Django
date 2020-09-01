import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

x_values = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype='float')
y_values = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0, 9.0], dtype='float')

model.fit(x_values, y_values, epochs=50000)

print(model.predict([10.0]))


#With an epochs of 500 we got a value of: 18.982449.
#With an epochs of 5000 we got a value of:18.999989
#With an epochs of 50000 we got a value of: 18.999989
