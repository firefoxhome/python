# Author:firefoxhome 
# Time:2017-12-30
# Theme: class 
#
#coding=utf-8

class Dog:

	color = 'white'
	sex = 'male'



	def setName(self,newName):
		self.name = newName
		self.__money = 1000000
# Note private property reference in class

	#def setjinmao(self):
	#	self.name = 'jingmao'

	#def sethashiqi(self):
	#	self.name = 'hashiqi'

	#def setzangao(self):
	#	self.name = 'zangao'

	def showMoney(self):
		print("money = %d"%self.__money)

	def eat(self):
		print("%s dog is eating bone"%self.name)

	def run(self):
		print("%s dog is runing"%self.name)


jinMao = Dog()
#jinMao.setjinmao()
jinMao.setName('dog123')
jinMao.eat()
print(jinMao.color)
print(jinMao.sex)
#print(jinMao.money)
jinMao.showMoney()


#hashiqi = Dog()
#hashiqi.sethashiqi()
#hashiqi.eat()

#zangao = Dog()
#zangao.setzangao()
#zangao.run()