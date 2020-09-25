from layer_naive import *

#test
apple = 100
orenge = 150
apple_num = 2
orenge_num = 3
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_orenge_layer = MulLayer()
add_apple_orenge_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orenge_price = mul_orenge_layer.forward(orenge, orenge_num)
apple_orenge_price = add_apple_orenge_layer.forward(apple_price,orenge_price)
price = mul_tax_layer.forward(apple_orenge_price,tax)
print(price)

#backward
dprice = 1
dapple_orenge_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorenge_price = add_apple_orenge_layer.backward(dapple_orenge_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorenge, dorenge_num = mul_orenge_layer.backward(dorenge_price)

print(dapple, dapple_num, dorenge, dorenge_num, dtax)
