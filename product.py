product = []
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	item = [] #--
	item.append(name) #--
	item.append(price) #--
	product.append(item) #product,append([name, price])
print(product)