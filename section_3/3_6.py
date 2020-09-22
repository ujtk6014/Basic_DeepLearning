import numpy as np
from mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

#以下動作チェック用
# #データの呼び出し
# (x_train, t_train),(x_test,t_test) = \
#     load_mnist(flatten = True, normalize = False)
# #それぞれのデータ形状を出力
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)
# #画像を表示してチェック
# img = x_train[0]
# label = t_train[0]
# print(label)
# print(img.shape)
# img = img.reshape(28,28)
# print(img.shape)
# img_show(img)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
def get_data():
    (x_train, t_train),(x_test,t_test) = \
        load_mnist(flatten = True, normalize = False, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']
    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)