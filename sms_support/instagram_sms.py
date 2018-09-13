#!/usr/bin/python

import os
import codecs
import time
import subprocess
import sys
import random
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('base/firefox/firefox')

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"


SMS_AMNT = int(input(Grey+"["+Blue+"SMS"+Grey+"]-["+Blue+"10"+Grey+"]"+Green+": "+Reset))

#
timeout = 60
iD = 0

lastname = random.choice(['diana','jakal','boreson','sinan','zanyar','lkafe','kenny','parker','faye','spivey','simon','miller','wilson','ryan','jackson','fellows','tuckler','turner','counety','baker','griffin','reynolds','andrews','dunns','barker','reid'])
rnd_char = random.choice(['2932','__837','9_82','29394','4_2_4','72','09','123','_0_','_9_'])
rnd_char2 = random.choice(['0','98','lade','sk','ks','de','le','qe','sz','mb','lo','pen','ku','iq'])

useragents = random.choice([
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55',
	'Mozilla/5.0 (X11; Heathrow/1.4; Linux i686; rv:30) Gecko/30 Firefox/30',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'
])

password = random.choice(['75!x#+FmnfW3SK','vL&pM2zVtV6NsEH4','PKc-pK2XmfRG-7B','UmE*F4aKD!cV7','eLU_U2&#MsqT#@4+','xS?mVEy!d2khDsye','L2tb+A97P=#s*WD$','wv&+&sXhrWxw7cJ','S+rD?r=z7?KaS2U','Rj?HcnN7*-jw=CKw','SQ?3Vx!J8vueyf2','cunnsjs1736jn#','lmasdks128973#!!!@'])
info = open('sms_support/phone','r')
info = info.read()

phone = info.strip().split(":",1)[0]
name = info.strip().split(":",1)[1]
fullname = str(name+lastname)
uname = str(lastname+rnd_char+rnd_char2)

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragents)

print(Grey+"USING:"+Reset+"  "+Blue+useragents+Reset)

display = Display(visible=0, size=(800, 600))
display.start()

br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver',firefox_profile=profile)

time.sleep(2)

br.get("https://www.instagram.com/")

time.sleep(7)

br.find_element_by_name("emailOrPhone").send_keys(str(phone))
br.find_element_by_name("fullName").send_keys(fullname)

br.find_element_by_name("username").send_keys(uname)
br.find_element_by_name("password").send_keys(password)

time.sleep(2)

br.find_element_by_css_selector("span.Um91Z:nth-child(1) > button:nth-child(1)").click()

time.sleep(7)

while True:
	if iD == SMS_AMNT:
		break
	else:
		br.find_element_by_link_text("Request New Code").click()
		iD = iD + 1
		print(Grey+"["+Blue+str(iD)+Grey+"] "+Green+"SMS sent")
		time.sleep(timeout)


br.close()
display.stop()
print(Blue+"finished")
sys.exit(0)