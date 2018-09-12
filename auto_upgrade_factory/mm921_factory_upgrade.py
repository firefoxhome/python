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
import wget
import os.path
import subprocess

#sudo pip install requests 
#Need : python2.7
#sudo pip install beautifulsoup4
#sudo pip install wget

#2018-9-12 13:20  The MM921 first version of the factory upgrade.




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
        count = 0
        
        while (count < 4):
            print 'The count is:', count
            count = count + 1
            print count

            output = os.popen('ifconfig | grep eth | cut -c 39-65')

            mac =  output.read()
            str = 'http://p.canaan-creative.com/mac/?a=%s' %mac
            

            print str
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



            md5sum_initial = '/home/factory/canaan_factory/md5sums'
            md5sum_initial_bak = '/home/factory/Avalon-extras/scripts/factory/md5sums'

            mymovefile(md5sum_initial_bak,md5sum_initial)

            md5sum_address = address + 'md5sums'
            print md5sum_address
            md5sum_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

            out_fname = 'md5sums'
            wget.download(md5sum_address, out=out_fname)




            MM921_initial = '/home/factory/canaan_factory/MM921.mcs'
            MM921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'

            mymovefile(MM921_initial_bak,MM921_initial)

            MM921_address = address + 'MM921.mcs'
            print MM921_address
            MM921_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM921.mcs' )

            out_fname = 'MM921.mcs'
            wget.download(MM921_address, out=out_fname)


            os.chdir('/home/factory/Avalon-extras/scripts/factory')
            check3 = os.popen('cat md5sums | grep MM921.mcs | cut -c 1-32')
            check4 = os.popen('md5sum MM921.mcs | cut -c 1-32')
            ck3 =  check3.read()
            ck4 =  check4.read()
            print ck3
            print ck4
                        
            if ck3 == ck4:
                print "MD5 Right"
                print "Firmware download successed"

            if count == 2:
                break

        initial = '/home/factory/canaan_factory/MM921.mcs'
        initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'


        print "Three downloads failed,Good bye!"
        mymovefile(initial,initial_bak)
        os._exit()



if __name__ == '__main__':
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


    path = "/home/factory/canaan_changelog"
    os.makedirs( path, 0755 );
    print  "New changelog placed directory successfully"

    os.chdir('/home/factory/canaan_changelog')
    changelogaddress = address + 'changelog'
    print changelogaddress
    
    
    changeloglocal = os.path.join('/home/factory/canaan_changelog','changelog' )
    
    out_fname = 'changelog'
    wget.download(changelogaddress, out=out_fname)

    print "当前工作目录 : %s" % os.getcwd()
    os.system("ls")


    check1 = os.popen('cat changelog | grep Version | cut -c 9-23').read()
    print "---------------"
    print check1
    print "---------------"

    os.chdir('/home/factory/Avalon-extras/scripts/factory')
    print "当前工作目录 : %s" % os.getcwd()
    os.system("ls")

    #check2 = os.popen('cat changelog | grep Version | cut -c 9-21').read()
    check2 = os.popen('cat changelog | grep Version | cut -c 9-23').read()

    print "--------------"
    print check2
    print "--------------"

    if check1 == check2:
        print "Firmware version is up to date."
        exit(0)
        print "-------------Error------------------"
    else:
        print "Firmware version is not up to date. Please download again"



    os.chdir('/home/factory/Avalon-extras')
    fd = os.open("version",os.O_RDWR)
    ver = os.read(fd,4)
    print "Local script version",ver

    result = re.search( r'("script_version": ")(.*?)(")', contents, re.M|re.I)
    net_ver = result.group(2)
    print "The latest script version of the server",net_ver

    if ver == net_ver:
        print "The version is already the latest"

    else:
        print "The version is not the latest"


    os.chdir('/home/factory/Avalon-extras/scripts/factory')
    print "当前工作目录 : %s" % os.getcwd()
    os.system("ls")

    srcfile = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'
    dstfile = '/home/factory/canaan_factory/MM921.mcs'


    if os.path.exists(srcfile):
        message = 'OK, the "%s" file exists.'
        print message % srcfile
        mymovefile(srcfile,dstfile)

        global address

        changelog_initial = '/home/factory/canaan_factory/changelog'
        changelog_initial_bak = '/home/factory/Avalon-extras/scripts/factory/changelog'

        mymovefile(changelog_initial_bak,changelog_initial)

        changelog_address = address + 'changelog'
        print changelog_address
        changelog_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

        out_fname = 'changelog'
        wget.download(changelog_address, out=out_fname)




        md5sum_initial = '/home/factory/canaan_factory/md5sums'
        md5sum_initial_bak = '/home/factory/Avalon-extras/scripts/factory/md5sums'

        mymovefile(md5sum_initial_bak,md5sum_initial)

        md5sum_address = address + 'md5sums'
        print md5sum_address
        md5sum_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

        out_fname = 'md5sums'
        wget.download(md5sum_address, out=out_fname)




        MM921_initial = '/home/factory/canaan_factory/MM921.mcs'
        MM921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'

        mymovefile(MM921_initial_bak,MM921_initial)

        MM921_address = address + 'MM921.mcs'
        print MM921_address
        MM921_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM921.mcs' )

        out_fname = 'MM921.mcs'
        wget.download(MM921_address, out=out_fname)

        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        check3 = os.popen('cat md5sums | grep MM921.mcs | cut -c 1-32')
        check4 = os.popen('md5sum MM921.mcs | cut -c 1-32')
        ck3 =  check3.read()
        ck4 =  check4.read()
        print ck3
        print ck4
        check(ck3,ck4)

    else:
        message = 'Sorry, I cannot find the "%s" file.'
        print message % srcfile     

        global address

        changelog_initial = '/home/factory/canaan_factory/changelog'
        changelog_initial_bak = '/home/factory/Avalon-extras/scripts/factory/changelog'

        mymovefile(changelog_initial_bak,changelog_initial)

        changelog_address = address + 'changelog'
        print changelog_address
        changelog_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','changelog' )

        out_fname = 'changelog'
        wget.download(changelog_address, out=out_fname)




        md5sum_initial = '/home/factory/canaan_factory/md5sums'
        md5sum_initial_bak = '/home/factory/Avalon-extras/scripts/factory/md5sums'

        mymovefile(md5sum_initial_bak,md5sum_initial)

        md5sum_address = address + 'md5sums'
        print md5sum_address
        md5sum_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','md5sums' )

        out_fname = 'md5sums'
        wget.download(md5sum_address, out=out_fname)




        MM921_initial = '/home/factory/canaan_factory/MM921.mcs'
        MM921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'

        mymovefile(MM921_initial_bak,MM921_initial)

        MM921_address = address + 'MM921.mcs'
        print MM921_address
        MM921_local = os.path.join('/home/factory/Avalon-extras/scripts/factory','MM921.mcs' )

        out_fname = 'MM921.mcs'
        wget.download(MM921_address, out=out_fname)

        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        check3 = os.popen('cat md5sums | grep MM921.mcs | cut -c 1-32')
        check4 = os.popen('md5sum MM921.mcs | cut -c 1-32')
        ck3 =  check3.read()
        ck4 =  check4.read()
        print ck3
        print ck4   
        check(ck3,ck4)


      
mychangelog = os.popen('cat changelog | grep Version | cut -c 9-23').read()
print mychangelog


url = str +'&b=%s'%mychangelog + '&c=%s'%ver 
print url
webbrowser.open(url, new=0, autoraise=True)


