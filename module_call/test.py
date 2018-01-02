#coding=utf-8

def printHello():
	print("-"*30)
	print("****** hello world **********")
	print("-"*30)

def main():
	print("This is a main")
	printHello()

if __name__ == '__main__':
    #The call in this file will be executed,Other module calls do not run the following functions
    #The test code can be placed here

	#print('---- in test.py ----')
	#printHello()
	#print('---- out test.py ----')

	main()
