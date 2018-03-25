#python 3

from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderName,newFolderName,queue):
	fr = open(oldFolderName + "/"+ name)
	fw = open(newFolderName + "/"+ name,"w")

	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()

	queue.put(name)


def main():
	oldFolderName = input("Please input FolderName:")

	newFolderName = oldFolderName + "-bak"
	#print (newFolderName)
	os.mkdir(newFolderName)

	fileNames = os.listdir(oldFolderName)

	pool = Pool(5)
	queue = Manager().Queue()

	for name in fileNames:
		pool.apply_async(copyFileTask, args=(name,oldFolderName,newFolderName,queue))

	num = 0
	allNum = len(fileNames)
	while num<allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\r copy Speed of progress:%.2f%%"%(copyRate*100), end="")

	print("\n coping end")
if __name__ == "__main__":
	main()


