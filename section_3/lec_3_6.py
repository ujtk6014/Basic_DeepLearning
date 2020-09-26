import numpy as np
import sys, os
sys.path.append(os.pardir)

from common.mnist import load_mnist
from PIL import Image
import pickle
import time


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

#シグモイド関数（オーバーフロー対策）
@np.vectorize
def sigmoid(x):
    return np.exp(min(0,x)) / (1.0 + np.exp(-abs(x)))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
def get_data():
    (x_train, t_train), (x_test,t_test) = \
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
    a3 = np.dot(z2,W3) + b3
    y = softmax(a3)
    return y


x, t = get_data()
network = init_network()

val = input('Enter the number 1:Normal 2:Batch > ')
if val == '1':
    #"普通バージョン
    accuracy_cnt = 0
    t1_n = time.time()
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y) #最も確率の高い要素のインデックスを取得
        if p == t[i]: #ラベルと一致＝正解したらカウントを増やす
            accuracy_cnt += 1
    t2_n = time.time()
    print("Elapsed time: " + str(round(t2_n-t1_n,2)))
    print("ACCURACY:"+ str(float(accuracy_cnt)/len(x))) #正解率の表示

elif val == '2':
    #バッチ処理（高速化）
    batch_size = 100
    accuracy_cnt = 0
    t1_b = time.time()
    for i in range(0,len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network,x_batch)
        p = np.argmax(y_batch, axis=1) #最も確率の高い要素のインデックスを取得
        accuracy_cnt +=np.sum(p == t[i:i+batch_size])
    t2_b = time.time()
    print("Elapsed time: " + str(round(t2_b-t1_b,2)))
    print("ACCURACY:"+ str(float(accuracy_cnt)/len(x))) #正解率の表示



