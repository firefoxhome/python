# Author:firefoxhome
# Time:2018-1-3
# Theme:python2.7 matplotlib numpy Module uses
# Need to install:
# sudo apt-get update
# sudo apt-get install python-dev
# sudo pip install numpy
# sudo apt-get install python-matplotlib
# sudo pip install xlrd
# sudo apt-get install python-sip
# sudo apt-get install libqt4-dev
# sudo apt-get install python-qt4 python-qt4-dev pyqt4-dev-tools qt4-dev-tools
#  
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                 label='Dashes set proactively')

ax.legend(loc='lower right')
plt.show()
