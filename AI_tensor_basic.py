## 숫자 인식 모델
'''
import numpy as np
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim)  # 텐서 이미지의 차원수 확인
print(train_images.shape)
print(train_images.dtype)

digit = train_images[4]  # 4번째 이미지 확인
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

print(train_labels[4])  # Label 확인

x = np.random.random((32,)) 
w = np.random.random((32,)) 
y = np.dot(w, x)
print(w)
print(x)
print(y)

# np.dot 직접 만들기
def vector_dot(w, x):   
    z = 0.
    for i in range(x.shape[0]):
      z += x[i] * w[i]
    return z

a = np.array([[1,2,3],[3,4,5]])
b = np.array([[1,2,],[3,4,],[5,6]])
#Transpose
at = a.T
#matrix multiplication
c = np.matmul(a,b)
print(at)
print(c)

# np.random.rand vs np.random.random 차이
r1 = np.random.rand(2,3)
r2 = np.random.random((2,3))
'''

# CUDA cuDNN 설치 필요
# import tensorflow as tf
# from tensorflow.python.client import device_lib

# print(device_lib.list_local_devices([1]) )

'''
참고 사이트
https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=ko#0
https://colab.research.google.com/drive/1IqjyoGLFeEdDFuPQ1yMA018Zz9DWuCkA#scrollTo=WD4GqdT54rya
https://playground.tensorflow.org/
https://teachablemachine.withgoogle.com/train
(텐서보드) https://bit.ly/kmooc-tensorboard1
(텐서보드) https://bit.ly/hparameter-tuning
(차원 축소) https://bit.ly/kmooc-dreduction 

# 퍼셉트론 손글씨 인식
https://colab.research.google.com/drive/1Igay5IFSdV8aLk6V9sD7CU7vfmIR0rMD?utm_campaign=perceptron%20coding#scrollTo=Z_Dp1RQz9taT
<<< Code >>>
% tensorflow_version 2.x
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

# 패션 mnist
https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/classification.ipynb
'''
# keras.Sequential, dense 함수에 대해 알아보자

# 데이터 수집, 전처리, 모델 서치, 학습

'''
(배포) https://bit.ly/colab_bootstrap
(필터) https://bit.ly/convolution-filters
(Fashion-Mnist) https://bit.ly/mlp-fashion-mnist
'''