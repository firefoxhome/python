#!/usr/bin/env python2.7
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

#2018-5-6 10:00  851 first version+1
#2018-6-5 14:15  change code 
#2018-9-2 09:11  Modify duplicate download function
#2018-9-2 14:00  Official first edition code 

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

    per = 100.0 * a * b / c

    if per > 100 :

        per = 100

    print '%d%%' % per,'已下载的大小:',a*b,'文件大小:',c


def check(fs,fd):
    if fs == fd:
        print "MD5 Right"
        print "Firmware download successed"

       
    else:
        print "MD5 Error,Please download it again"
        count = 1
        
        
        while (count < 3):
            print 'The count is:', count            
            count = count + 1

            output = os.popen('ifconfig | grep eth | cut -c 39-65')
            mac =  output.read()
            #print mac
            str = 'http://p.canaan-creative.com/mac/?a=%s' %mac
    

            print str
            #Crawl the content
            page = urllib2.urlopen(str)   
            contents = page.read()  
            #print(contents)
            

            url = 'https://canaan.io/downloads/software/avalon851/mm/latest/md5sums'
            
            md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

            local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM851.mcs' )
            urllib.urlretrieve(address,local,Schedule)
            print "****************************************************************************"
            print "Download the MD5 File"
            print "****************************************************************************"
            urllib.urlretrieve(url,md5,Schedule)


            #check MD5
            check1 = os.popen('cat md5sums | grep MM851.mcs | cut -c 1-32')
            check2 = os.popen('md5sum MM851.mcs | cut -c 1-32')
            ck1 =  check1.read()
            ck2 =  check2.read()
            print "-------------------------------"
            print ck1
            print ck2
            print "-------------------------------"
            if ck1 == ck2:
                print "MD5 Right"
                print "Firmware download successed"
                exit(0)

        initial = '/home/factory/canaan_factory/MM851.mcs'
        initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM851.mcs'


        print "Three downloads failed,Good bye!"
        mymovefile(initial_bak,initial)
        exit(0)




output = os.popen('ifconfig | grep eth | cut -c 39-65')
mac =  output.read()

str = 'http://p.canaan-creative.com/mac/?a=%s' %mac
print "The URL is being accessed",str

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


srcfile = '/home/factory/Avalon-extras/scripts/factory/MM851.mcs'
dstfile = '/home/factory/canaan_factory/MM851.mcs'
#Add dstfile = /home/factory/canaan_factory/MM821.mcs, solve the firmware movement is not covered.


if os.path.exists(srcfile):
    message = 'OK, the "%s" file exists.'
    print message % srcfile
    #mv exists firmware to /home/factory/canaan_factory
    mymovefile(srcfile,dstfile)
    

    url = 'https://canaan.io/downloads/software/avalon851/mm/latest/md5sums'
    
    md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

       
    changelog = 'https://canaan.io/downloads/software/avalon851/mm/latest/changelog'
    changeloglocal = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM851.mcs' )
    urllib.urlretrieve(address,local,Schedule)

    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)

    print "****************************************************************************"
    print "Download the changelog"
    print "****************************************************************************"
    urllib.urlretrieve(changelog,changeloglocal,Schedule)


    check1 = os.popen('cat md5sums | grep MM851.mcs | cut -c 1-32')
    
    check2 = os.popen('md5sum MM851.mcs | cut -c 1-32')
    ck1 =  check1.read()
    ck2 =  check2.read()
    #print ck1
    #print ck2
    check(ck1, ck2)


else:
    message = 'Sorry, I cannot find the "%s" file.'
    print message % srcfile
    

    url = 'https://canaan.io/downloads/software/avalon851/mm/latest/md5sums' 
    
    md5 = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )
    
       
    changelog = 'https://canaan.io/downloads/software/avalon851/mm/latest/changelog'
    changeloglocal = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

    local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM851.mcs')
    urllib.urlretrieve(address,local,Schedule)

    print "****************************************************************************"
    print "Download the MD5 File"
    print "****************************************************************************"
    urllib.urlretrieve(url,md5,Schedule)

    print "****************************************************************************"
    print "Download the changelog"
    print "****************************************************************************"
    urllib.urlretrieve(changelog,changeloglocal,Schedule)


    check1 = os.popen('cat md5sums | grep MM851.mcs | cut -c 1-32')
    
    check2 = os.popen('md5sum MM851.mcs | cut -c 1-32')
    ck1 =  check1.read()
    ck2 =  check2.read()
    #print ck1
    #print ck2
    check(ck1, ck2)


mychangelog = os.popen('cat changelog | grep Version | cut -c 9-23').read()
print mychangelog


url = str +'&b=%s'%mychangelog + '&c=%s'%ver 
print url
webbrowser.open(url, new=0, autoraise=True)















