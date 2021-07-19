#!/bin/python

import os,sys,time

def clear():
    os.system("clear")

clear()
print "\033[1;33m XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
time.sleep(1)
print "\033[1;33mXXXXX     XXXXXXXXXXXXXXX     XXXXX"
time.sleep(1)
print "\033[1;33mXXXX       XXXXXXXXXXXXX       XXXX"
time.sleep(1)
print "\033[1;33mXXXXX     XXXXXXXXXXXXXXX     XXXXX"
time.sleep(1)
print "\033[1;33mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
time.sleep(1)
print "\033[1;35m  Selamat Datang Di L-U-X Project"
print " "
print "[~] 1. \033[1;33mAndroid Information"
print " "
print "[~] 2. \033[1;33mKeluar..."
enter = raw_input "\033[1;36mInput \033[1;35m1(1-2) \033[1;37 $ "
if enter == '1':
    os.system("pkg install neofetch")
    clear()
    os.system("neofetch")
    print("\033[1;32Succes!")
    os.system("python2 script.py")
    time.sleep(15)
elif enter == '2'
    clear()
    print("Keluar Dari Program!")

