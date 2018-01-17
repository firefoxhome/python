import numpy as np
import matplotlib.pyplot as plt
import xlrd

#open excel file and get sheet
myBook = xlrd.open_workbook('jiang.xls')
mySheet = myBook.sheet_by_index(0)

#get datas
time = mySheet.col(0)
time = [x.value for x in time]
tps = mySheet.col_values(1)

#drop the 1st line of the data, which is the name of the data.
time.pop(0)
tps.pop(0)

#declare a figure object to plot
fig = plt.figure(1)

#plot tps
plt.plot(tps)

#advance settings
plt.title('time-tps')
plt.xticks(range(len(time)),time)

#show the figure
plt.show()
