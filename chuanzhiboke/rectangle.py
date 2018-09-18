#coding=utf-8

class JuxingArea():

	def getNums(self):
		self.__a = input("Please input frist number:")
		self.__b = input("Please input second number:")

	def cal(self):
		print("rectagle area is:%d"%(self.__a * self.__b))

class SanjiaoxingArea():

	def getNums(self):
		self.__a = input("Please input frist number:")
		self.__b = input("Please input second number:")

	def cal(self):
		print("Triangle area is:%f"%(self.__a * self.__b / 2.0))


#a = JuxingArea()
#a.getNums()
#a.cal()

b = SanjiaoxingArea()
b.getNums()
b.cal()