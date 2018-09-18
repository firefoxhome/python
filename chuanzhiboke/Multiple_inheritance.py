#coding=utf-8

class A:
	def test1(self):
		print("------test1--------")

	def test(self):
		print("------test in A----")

class B:
	def test2(self):
		print("------test2--------")

	def test(self):
		print("-------test in B----")

class C(B,A):
	def test(self):
		print("--------test in C----")
	
	#Note Multiple inheritance B,A Order



c = C()
c.test1()
c.test2()
c.test()