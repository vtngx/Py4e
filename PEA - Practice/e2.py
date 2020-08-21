f = open('data.txt')

products = dict()

for line in f:
    name = line.split(' ')[0] + ' ' + line.split(' ')[1]
    total = int(line.split(' ')[2]) * int(line.split(' ')[3])
    products[name] = products.get(name, 0) + total

sort = sorted(products.items(), key=lambda x: x[1], reverse=True)[:5]

for k, v in sort:
    print(k, v)
