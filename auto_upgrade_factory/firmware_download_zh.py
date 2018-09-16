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


def foldercheck(srcfile):
    if not os.path.exists(srcfile):
        print "%s 不存在!"%(srcfile)
        path = "/home/factory/canaan_changelog"
        os.makedirs( path,0755)
        print  "canaan_changelog目录创建成功"
    else:
        print  "进入canaan_changelog目录"


def changelogcheck(check1,check2):
    if check1 == check2:
        print "固件版本已经是最新的"
        os.system('rm -rf /home/factory/canaan_changelog')
        exit(0)
        print "-------------Error------------------"
    else:
        print "固件版本不是最新的，现在下载最新的版本"
        os.system('rm -rf /home/factory/canaan_changelog')


def versioncheck():
    os.chdir('/home/factory/Avalon-extras')
    fd = os.open("version",os.O_RDWR)
    ver = os.read(fd,4)
    print "当前仓库脚本版本是",ver

    result = re.search( r'("script_version": ")(.*?)(")', contents, re.M|re.I)
    net_ver = result.group(2)
    print "服务器端当前仓库版本是",net_ver

    if ver == net_ver:
        print "本地仓库版本已经是最新的"
    else:
        print "本地仓库版本不是最新的"

    return ver


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print "%s 不存在!"%(srcfile)
    else:
        fpath,filename=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile,dstfile)
        print "move %s -> %s"%(srcfile, dstfile)


def md5sums_download(address):
    md5sum_address = address + 'md5sums'
    print md5sum_address

    out_fname = 'md5sums'
    wget.download(md5sum_address, out=out_fname)


def changelog_download(address):
    changelog_address = address + 'changelog'
    print changelog_address

    out_fname = 'changelog'
    wget.download(changelog_address, out=out_fname)


def minermodel(address):
    output = os.popen("echo %s | awk -F '/' '{ print $6 }' " % address)
    minermodel = output.read()
    print "矿机型号是 ",minermodel
    return minermodel


def burnmodel(address):
    output = os.popen("echo %s | awk -F '/' '{print $7}' " % address)
    burnmodel = output.read()
    print "安装的固件名字是 ",burnmodel
    return burnmodel


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

            md5sums_download(address)

            MM921_initial = '/home/factory/canaan_factory/MM921.mcs'
            MM921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'

            mymovefile(MM921_initial_bak,MM921_initial)

            MM921_address = address + 'MM921.mcs'
            print MM921_address

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


output = os.popen('ifconfig | grep eth | cut -c 39-65')
mac =  output.read()

str = 'http://p.canaan-creative.com/mac/?a=%s' %mac
print "服务器端的访问链接是",str

page = urllib2.urlopen(str)
contents = page.read()

if page.getcode() != 200:
    os._exit()
else:
    print "可以获取服务器链接"

print "服务器端获取的内容是",contents

print 'http header:/n', page.info() 
print 'http status:', page.getcode() 

result = re.search( r'("Download_link": ")(.*?)(")', contents, re.M|re.I)
address = result.group(2)
print  "固件下载目录是",address


srcfile = '/home/factory/canaan_changelog'
foldercheck(srcfile)


os.chdir('/home/factory/canaan_changelog')
changelogaddress = address + 'changelog'
print changelogaddress

out_fname = 'changelog.log'
wget.download(changelogaddress, out=out_fname)
print "**************************-----------------------------------**********************"

print "当前工作目录 : %s" % os.getcwd()
os.system("ls")

check1 = os.popen('cat changelog.log | grep Version | cut -c 9-23').read()
print "---------------"
print check1
print "---------------"

os.chdir('/home/factory/Avalon-extras/scripts/factory')
print "当前工作目录 : %s" % os.getcwd()
os.system("ls")

check2 = os.popen('cat changelog | grep Version | cut -c 9-21').read()
#check2 = os.popen('cat changelog | grep Version | cut -c 9-23').read()

print "--------------"
print check2
print "--------------"

changelogcheck(check1,check2)


miner = minermodel(address).strip()
model = burnmodel(address).strip()


if miner == 'avalon921':
    print "This is avalon921 miner"
    if model == 'mm':
        print "This is avalon921 MM firmware"
        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        global address
        md5sum_initial = '/home/factory/canaan_factory/md5sums'
        md5sum_initial_bak = '/home/factory/Avalon-extras/scripts/factory/md5sums'

        mymovefile(md5sum_initial_bak,md5sum_initial)
        md5sums_download(address)

        changelog_initial = '/home/factory/canaan_factory/changelog'
        changelog_initial_bak = '/home/factory/Avalon-extras/scripts/factory/changelog'

        mymovefile(changelog_initial_bak,changelog_initial)
        changelog_download(address)

        MM921_initial = '/home/factory/canaan_factory/MM921.mcs'
        MM921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/MM921.mcs'

        mymovefile(MM921_initial_bak,MM921_initial)

        MM921_address = address + 'MM921.mcs'
        print MM921_address

        out_fname = 'MM921.mcs'
        wget.download(MM921_address, out=out_fname)

        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        check3 = os.popen('cat md5sums | grep MM921.mcs | cut -c 1-32')
        check4 = os.popen('md5sum MM921.mcs | cut -c 1-32')
        ck3 =  check3.read()
        ck4 =  check4.read()
        print ck3
        print ck4
        #check(ck3,ck4)
    elif model == 'pmu':
        print "This is avalon921 pmu firmware"
        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        global address
        md5sum_initial = '/home/factory/canaan_factory/md5sums'
        md5sum_initial_bak = '/home/factory/Avalon-extras/scripts/factory/md5sums'

        mymovefile(md5sum_initial_bak,md5sum_initial)
        md5sums_download(address)

        changelog_initial = '/home/factory/canaan_factory/changelog'
        changelog_initial_bak = '/home/factory/Avalon-extras/scripts/factory/changelog'

        mymovefile(changelog_initial_bak,changelog_initial)
        changelog_download(address)

        pmu921_initial = '/home/factory/canaan_factory/pmu921.axf'
        pmu921_initial_bak = '/home/factory/Avalon-extras/scripts/factory/pmu921.axf'

        mymovefile(pmu921_initial_bak,pmu921_initial)

        pmu921_address = address + 'pmu921.axf'
        print pmu921_address

        out_fname = 'pmu921.axf'
        wget.download(pmu921_address, out=out_fname)
        os.chdir('/home/factory/Avalon-extras/scripts/factory')
        check3 = os.popen('cat md5sums | grep pmu921.axf | cut -c 1-32')
        check4 = os.popen('md5sum pmu921.axf | cut -c 1-32')
        ck3 =  check3.read()
        ck4 =  check4.read()
        print ck3
        print ck4
        #check(ck3,ck4)
    else:
        print "--------------Error----------------------------------------"


os.chdir('/home/factory/Avalon-extras/scripts/factory')
mychangelog = os.popen('cat changelog | grep Version | cut -c 9-23').read()
print mychangelog

ver = versioncheck()


url = str +'&b=%s'%mychangelog + '&c=%s'%ver 
print url
webbrowser.open(url, new=0, autoraise=True)
