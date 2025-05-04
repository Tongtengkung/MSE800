import tensorflow as tf
import matplotlib.pyplot as plt

class image_file:
    def __init__(self):
        self.image_path = r'C:\Users\norra\OneDrive\Documents\GitHub\MSE800\Week4\Cat03.jpg'
    
    def fetch_and_show_image(self):
        print('Fetching and showing image...')
        image = tf.io.read_file(self.image_path)
        image = tf.image.decode_image(image)
        image = tf.image.convert_image_dtype(image, tf.float32)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    