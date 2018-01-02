#coding=utf-8

class Cat:
	color = 'black'
	legs = 4
	weight = 6

	def miaomaio(self):
		print("cat is call")

	def catch(self):
		print("catch a mouse")


class Bosi(Cat):
	pass

	def scratch(self):
		print("bo si mao is scratching")
	#color = 'black'
	#legs = 4
	#weight = 6

	#def miaomaio(self):
	#	print("cat is call")

	#def catch(self):
	#	print("catch a mouse")

class TomCat(Bosi):
	pass




#xiaohua = Cat()
#xiaohua.miaomaio()
#xiaohua.catch()

#bosi = Bosi()
#bosi.miaomaio()
#bosi.catch()
#bosi.scratch()

tom = TomCat()
tom.scratch()

