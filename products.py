products = []

while True:
    name = input('請輸入商品名稱：')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

for product in products:
    # print(product[0])
    print(f'商品名稱：{product[0]} 的價格為 {product[1]}')

with open('products.csv', 'w') as f:
    for product in products:
        # f.write(product[0] + ',' + str(product[1]) + '\n')
        f.write(f'{product[0]}, {product[1]} \n')