#coding=utf-8


import time

class Gun:
	
	color = 'black'

	def __init__(self,newName,allNum,evNUm):
		self.__name = newName
		self.__bulletnum = allNum
		self.__jianbulletnum = evNUm	

    #gun name
	def setName(self, newName):
		self.__name = newName
    #total bullet
	def setBulletNum(self,num):
		self.__bulletnum = num
    #consume buttle
	def sefJianBulletNum(self,num):
		self.__jianbulletnum = num
    #shoot 
	def buibui(self):
		if self.__bulletnum - self.__jianbulletnum > 0:
			self.__bulletnum = self.__bulletnum - self.__jianbulletnum
		print("%s Surplus Bullet number is: %d"%(self.__name, self.__bulletnum))


AK47 = Gun('AK47',50,4)
#AK47.setName('AK47')
#AK47.setBulletNum(50)
#AK47.sefJianBulletNum(4)

MP5 = Gun('MP5',30,2)
#MP5.setName('MP5')
#MP5.setBulletNum(30)
#MP5.sefJianBulletNum(2)


while True:

	AK47.buibui()
	MP5.buibui()

	time.sleep(1)

	AK47.buibui()
	MP5.buibui()


#have a bug  
