#coding=utf-8

tree = input('Please input directory  nesting number:')
i = 0
path = []
mystr = '/'

while i < tree:

	pathTemp = raw_input('Please input No. %d layer route:' %(i + 1))

	path.append(pathTemp)

	i += 1

finalPath = '/' + mystr.join(path)

print finalPath	