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
import sys

#sudo pip install requests 
#Need : python2.7
#sudo pip install beautifulsoup4

#2018-1-26 17:21  Achieve basic functions
#2018-1-30 10:53  Add Increase the download success of the firmware information response server
#2018-1-30 14:45  Solve the firmware movement is not covered
#2018-1-31 20:15  Modify the function check
#2018-2-1  13:28  The client can read the version number of its own and the server
#2018-2-1  16:25  Added to the version judgment, the latest exit
#2018-2-5  21:00  The name of the modified network card is eth0
#2018-2-6  14:32  
#2018-2-25 18:17  Make some changes,delete Note
#2018-2-26 10:20  Change the server download link
#2018-2-26 15:54  The verification of changlog has been added
#2018-2-26 20:37  Modify the check functions


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

    print '%d%%' % per,'已下载的大小:',a*b,'文件大小:',c

    #print '已经下载的数据块:',a#,'\n'

    #print '数据块的大小:',b#,'\n'

    #print '远程文件大小:',c,'\n'

    #print '已下载的大小:',a*b,'文件大小:',c

def check(fs,fd):
    if fs == fd:
        print "MD5 Right"
        print "Firmware download successed"

       
    else:
        print "MD5 Error,Please download it again"
        count = 1
        
        while (count < 4):
            print 'The count is:', count
            count = count + 1

            output = os.popen('ifconfig | grep eth | cut -c 39-65')
            mac =  output.read()
            #print mac
            #str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
            str = 'http://ams.b-bug.org/mac/address.py?a=%s' %mac

            print str
            #Crawl the content
            page = urllib2.urlopen(str)   
            contents = page.read()  
            #print(contents)

            url = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/md5sums'
            md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

            local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs' )
            urllib.urlretrieve(address,local,Schedule)
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




#Get links
output = os.popen('ifconfig | grep eth | cut -c 39-65')
mac =  output.read()
#print mac
#str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
str = 'http://ams.b-bug.org/mac/address.py?a=%s' %mac
print "The URL is being accessed",str

#Crawl the content
page = urllib2.urlopen(str)   
contents = page.read()  

if page.getcode() != 200:
    os._exit()
else:
    print "Server links Right"

print "The content of the obtained web page is",contents

print 'http header:/n', page.info() 
print 'http status:', page.getcode() 


result = re.search( r'("Download_link": ")(.*?)(")', contents, re.M|re.I)
address = result.group(2)
print  "The firmware download address is",address

os.chdir('/home/factory/Avalon-extras')
print "当前工作目录 : %s" % os.getcwd()
os.system("ls")


fd = os.open("version",os.O_RDWR)
#version = os.popen('cat version | cut -c 1-4').read(fd,1)
ver = os.read(fd,4)
print "Local script version",ver

result = re.search( r'("script_version": ")(.*?)(")', contents, re.M|re.I)
net_ver = result.group(2)
print "The latest script version of the server",net_ver



if ver == net_ver:
    print "The version is already the latest"
    #exit(0)
    #print "The firmware is not required to be downloaded"
else:
    print "The version is not the latest"


#step1 Back up the existing firmware
#while True:
os.chdir('/home/factory/Avalon-extras/scripts/factory')
print "当前工作目录 : %s" % os.getcwd()
os.system("ls")


#filename = r'/home/factory/Avalon-extras/scripts/factory/MM741.mcs'
srcfile = '/home/factory/Avalon-extras/scripts/factory/MM821.mcs'
dstfile = '/home/factory/canaan_factory/MM821.mcs'
#Add dstfile = /home/factory/canaan_factory/MM821.mcs, solve the firmware movement is not covered.




if os.path.exists(srcfile):
    message = 'OK, the "%s" file exists.'
    print message % srcfile
    #mv exists firmware to /home/factory/canaan_factory
    mymovefile(srcfile,dstfile)
    

    #downloads MM821.mcs

    url = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/md5sums'
    md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

    changelog = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/changelog'
    changeloglocal = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs' )
    urllib.urlretrieve(address,local,Schedule)

    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)

    print "****************************************************************************"
    print "Download the changelog"
    print "****************************************************************************"
    urllib.urlretrieve(changelog,changeloglocal,Schedule)


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
    
    changelog = 'https://canaan.io/downloads/software/avalon821/mm/2017-12-27/changelog'
    changeloglocal = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM821.mcs')
    urllib.urlretrieve(address,local,Schedule)

    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)

    print "****************************************************************************"
    print "Download the changelog"
    print "****************************************************************************"
    urllib.urlretrieve(changelog,changeloglocal,Schedule)

    #check MD5
    check1 = os.popen('cat md5sums | grep MM821.mcs | cut -c 1-32')
    check2 = os.popen('md5sum MM821.mcs | cut -c 1-32')
    ck1 =  check1.read()
    ck2 =  check2.read()
    #print ck1
    #print ck2
    check(ck1, ck2)


mychangelog = os.popen('cat changelog | grep Version | cut -c 9-23').read()
print mychangelog


#output = os.popen('ifconfig | grep eth | cut -c 39-65')
#mac =  output.read()
        
#str = 'http://192.168.1.179/mac/address.py?a=%s' %mac
#print str

#url = str +'&b=8211712-16c14b0' + '&c=%s'%ver  
url = str + '&b=%s'%mychangelog + '&c=%s'%ver 
print url
webbrowser.open(url, new=0, autoraise=True)












