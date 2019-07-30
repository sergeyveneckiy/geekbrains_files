import tensorflow as tf
from tensorflow  import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ancle boot']
#print(train_images[10][0])

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
     keras.layers.Flatten(input_shape=(28, 28)),
     keras.layers.Dense(128, activation=tf.nn.relu),
     keras.layers.Dense(10, activation=tf.nn.softmax)
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

img = test_images[150]

plt.figure()
plt.imshow(test_images[150])
plt.colorbar()
plt.grid(False)
plt.show()

img = (np.expand_dims(img, 0))
predictions_single = model.predict(img)
#print(predictions_single)
print(np.argmax(predictions_single))
print(class_names[np.argmax(predictions_single)])



