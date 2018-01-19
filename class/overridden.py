#coding=utf-8

class Cat:

	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge
		print("my is Cat class Construction method")

class Bosi(Cat):
	def __init__(self,a,b,c):

		Cat.__init__(self,a,b)

		self.weight = c
		
		print("My is Bosi class Construction method")


bosi = Bosi('aaaaa',100,6)

print(bosi.name)
print(bosi.age)
print(bosi.weight)