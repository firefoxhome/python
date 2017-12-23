#
# Author:firefoxhome(2683299672@qq.com)
# theme :card_management
#
#------------------------------------------------------------------------------------------------

#coding=utf-8

add=["zhangsan", "lisi", "wangwu"]

def mu():
	i=0

	for temp in add:
		print("%d     %s "%(i, temp))
		i+=1

print "welcome to python world!"
print "*"*45

while True:
	mu()

	print "add user please choice : 1 "
	print "delete user please choice : 2"
	print "update user please choice : 3"
	print "lookup user please choice : 4"
	print "quit user please choice : 5"

	print "*"*45

	a=input("please input your choice:")

	if a==5:
		break
	elif a==1:
		c=raw_input("please input need add user name:")
		add.append(c)
		print("%s add successed"%c)
	elif a==2:
		mu()
		i=input("please input you need delete user number:")

		nameLan=len(add)
		if i<=nameLan-1:
			del add[i]

		print("%s delete successed"%i)

	elif a==3:
		mu()

		i=input("please input you need update number:")

		e=raw_input("please input you new user:")

		if i<len(add):
			add[int(i)] = "%s"%e
			print("your update number %s"%i)
			print("update user is : %s"%e)
		else:
			print("Error!")
	elif a==4:
		i=raw_input("please input your lookup user:")

		if i in add:
			print("you lookup user exist")
		else:
			print("you lookup user no exist")
	else:
		print("your input Error")

