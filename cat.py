#coding=utf-8

class Cat:
	color = 'black'
	legs = 4
	weight = 6

	def miaomaio(self):
		print("cat maio miao")

	def catch(self):
		print("catch a mouse")


class Bosi(Cat):
	pass

	def naoyangyang(self):
		print("bo si mao naoyangyang")
	#color = 'black'
	#legs = 4
	#weight = 6

	#def miaomaio(self):
	#	print("cat maio miao")

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
#bosi.naoyangyang()

tom = TomCat()
tom.naoyangyang()

