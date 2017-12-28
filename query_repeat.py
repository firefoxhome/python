#
#
#
#
#--------------------------------------------

#coding=utf-8

str1 = 'dfafsfdsfgdtfadfsssfff'

num = len(str1)

numList = []

for s in str1:
	freq = str1.count(s)

	numStr = s + ":" + str(freq)

	if numStr not in numList:
		numList.append(numStr)

for i in numList:
	print(i)

