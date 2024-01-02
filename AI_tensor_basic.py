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
import tensorflow as tf
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices([1]) )

'''
참고 사이트
https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=ko#0
https://colab.research.google.com/drive/1IqjyoGLFeEdDFuPQ1yMA018Zz9DWuCkA#scrollTo=WD4GqdT54rya
https://playground.tensorflow.org/
https://teachablemachine.withgoogle.com/train

# 퍼셉트론 손글씨 인식
https://colab.research.google.com/drive/1Igay5IFSdV8aLk6V9sD7CU7vfmIR0rMD?utm_campaign=perceptron%20coding#scrollTo=Z_Dp1RQz9taT
'''
