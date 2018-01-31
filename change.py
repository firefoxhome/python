
#coding=utf-8

import os
import shutil
import urllib2 
import requests  
import urllib 
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall 
import webbrowser

#sudo pip install requests 
#Need : python2.7
#sudo pip install beautifulsoup4

#2018-1-26 17:21  Achieve basic functions
#2018-1-30 10:53  Add Increase the download success of the firmware information response server
#2018-1-30 14:45  Solve the firmware movement is not covered
#2018-1-31 20:15  Modify the function check



#list1 = ['MM721','MM741','MM761','MM821']
#list2 = ['pmu721','pmu741','pmu821']


def mymovefile(srcfile, dstfile):
	if not os.path.isfile(srcfile):
		print "%s not exists!"%(srcfile)
	else:
		fpath,filename=os.path.split(dstfile)
		if not os.path.exists(fpath):
			os.makedirs(fpath)
		shutil.move(srcfile,dstfile)
		print "move %s -> %s"%(srcfile, dstfile)

def Schedule(a,b,c):

    '''

    a:已经下载的数据块

    b:数据块的大小

    c:远程文件的大小

   '''

    per = 100.0 * a * b / c

    if per > 100 :

        per = 100

    print '%.2f%%' % per,'已下载的大小:',a*b,'文件大小:',c

    #print '已经下载的数据块:',a#,'\n'

    #print '数据块的大小:',b#,'\n'

    #print '远程文件大小:',c,'\n'

    #print '已下载的大小:',a*b,'文件大小:',c

def check(fs,fd):
    if fs == fd:
        print "MD5 Right"
        print "Firmware download successed"

        output = os.popen('ifconfig | grep wlp2s0 | cut -c 39-65')
        mac =  output.read()
        #print mac
        str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
        print str

        url = str +'&b=8211712-16c14b0'  
        print url
        webbrowser.open(url, new=0, autoraise=True)

    else:
        print "MD5 Error,Please download it again"
        count = 0
        
        while (count < 4):
            print 'The count is:', count
            count = count + 1

            output = os.popen('ifconfig | grep wlp2s0 | cut -c 39-65')
            mac =  output.read()
            #print mac
            str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
            print str
            #Crawl the content
            page = urllib2.urlopen(str)   
            contents = page.read()  
            #print(contents)

            url = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/md5sums'
            md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

            local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs' )

            urllib.urlretrieve(contents,local,Schedule)
            print "****************************************************************************"
            print "Download the MD5 File"
            print "****************************************************************************"
            urllib.urlretrieve(url,md5,Schedule)


            #check MD5
            check1 = os.popen('cat md5sums | grep MM821.mcs | cut -c 1-32')
            check2 = os.popen('md5sum MM821.mcs | cut -c 1-32')
            ck1 =  check1.read()
            ck2 =  check2.read()
            #print ck1
            #print ck2
            check(ck1, ck2)

        initial = '/home/factory/canaan_factory/MM821.mcs'
        initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM821.mcs'


        print "Three downloads failed,Good bye!"
        mymovefile(initial,initial_bak)
'''
def downfirmware():
    #Get links
    output = os.popen('ifconfig | grep wlp2s0 | cut -c 39-65')
    mac =  output.read()
    #print mac
    str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
    print str
    #Crawl the content
    page = urllib2.urlopen(str)   
    contents = page.read()  
    print(contents)
'''

	
#step1 Back up the existing firmware
#while True:
os.chdir('/home/factory/Avalon-extras/scripts/factory')
print "当前工作目录 : %s" % os.getcwd()
os.system("ls")
#filename = r'/home/factory/Avalon-extras/scripts/factory/MM741.mcs'
srcfile = '/home/factory/Avalon-extras/scripts/factory/MM821.mcs'
dstfile = '/home/factory/canaan_factory/MM821.mcs'
#Add dstfile = /home/factory/canaan_factory/MM821.mcs, solve the firmware movement is not covered.

#Get links

output = os.popen('ifconfig | grep wlp2s0 | cut -c 39-65')
mac =  output.read()
#print mac
str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
print str
#Crawl the content
page = urllib2.urlopen(str)   
contents = page.read()  
print(contents)
print 'http header:/n', page.info() 
print 'http status:', page.getcode() 
#print 'url:', page.geturl() 

if page.getcode() != 200:
    os._exit()
else:
    print "Server links Right"





if os.path.exists(srcfile):
    message = 'OK, the "%s" file exists.'
    print message % srcfile
    #mv exists firmware to /home/factory/canaan_factory
    mymovefile(srcfile,dstfile)
    

    #downloads MM821.mcs


    url = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/md5sums'
    md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs' )

    urllib.urlretrieve(contents,local,Schedule)
    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)


    #check MD5
    check1 = os.popen('cat md5sums | grep MM821.mcs | cut -c 1-32')
    check2 = os.popen('md5sum MM821.mcs | cut -c 1-32')
    ck1 =  check1.read()
    ck2 =  check2.read()
    #print ck1
    #print ck2
    check(ck1, ck2)


else:
    message = 'Sorry, I cannot find the "%s" file.'
    print message % srcfile
    

    #downloads MM821.mcs
    url = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/md5sums'
    md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs')

    urllib.urlretrieve(contents,local,Schedule)
    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)

    #check MD5
    check1 = os.popen('cat md5sums | grep MM821.mcs | cut -c 1-32')
    check2 = os.popen('md5sum MM821.mcs | cut -c 1-32')
    ck1 =  check1.read()
    ck2 =  check2.read()
    #print ck1
    #print ck2
    check(ck1, ck2)




# Download new firmware
'''

image_url = "https://canaan.io/downloads/software/avalon741/mm/2017-06-03/MM741.mcs"  
  
r = requests.get(image_url) # create HTTP response object  
  
with open("python_logo.png",'wb') as f:  
    f.write(r.content)  




#print filename
#os.path.exists('MM741.mcs')

'''
'''
if os.path.exists(filename):
    message = 'OK, the "%s" file exists.'

else:
    message = 'Sorry, I cannot find the "%s" file.'
print message % filename
#os.getcwd()
	#Myfile="/home/factory/Avalon-extras/scripts/factory/MM741.mcs"
'''

