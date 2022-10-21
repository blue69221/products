import os # operating system

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
    print('Yeah! 找到檔案了!')
    # with open('products.csv', 'r', encoding='utf-8') as f:
    with open('products.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 條件符合就跳到下一回再繼續執行下面程式
            name, price = line.strip().split(',') # .strip():移除換行、split():分割
            products.append([name, price])
    print(products)

else:
    print('找不到檔案......')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

# 印出所有購買記錄
for product in products:
    # print(product[0])
    print(f'商品名稱：{product[0]} 的價格為 {product[1]}')

# 寫入檔案
# with open('products.csv', 'w', encoding='utf-8') as f:
with open('products.csv', 'w') as f:
    f.write(f'商品,價格 \n')
    for product in products:
        # f.write(product[0] + ',' + str(product[1]) + '\n')
        f.write(f'{product[0]}, {product[1]} \n')