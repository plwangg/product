import os
product = []
if os.path.isfile('product.csv'):
	print('新增內容')
	with open('product.csv', 'r') as file:
		for line in file:
			name , price = line.strip().split(',')
			product.append([name, price])
else:
	print('新增第一筆資料')
	with open('product.csv', 'w') as file:
		file.write('商品,價格')
	with open('product.csv', 'r') as file:
		for line in file:
			name , price = line.strip().split(',')
			product.append([name, price])

#user input
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	item = [] 
	item.append(name)
	item.append(price)
	product.append(item)
print(product)

#write file	
with open('product.csv', 'w') as file:
	for i in product:
		file.write(i[0] + ',' + i[1] + '\n')