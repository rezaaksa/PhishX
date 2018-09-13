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



ID = 0
CALLID = 0

lastname = random.choice(['diana','jakal','boreson','sinan','zanyar','lkafe','kenny','parker','faye','spivey','simon','miller','wilson','ryan','jackson','fellows','tuckler','turner','counety','baker','griffin','reynolds','andrews','dunns','barker','reid'])
sex = random.choice(['1','2'])#Female,Male

#---------------------[for teh date]-----------------------#

month = random.choice(['2','3','4','5','6','7','8','9','11'])
day = random.choice(['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','24','25','26','32'])
year = random.choice(['16','17','18','19','20','21','22','23','24','25','26','27','28','29'])

#----------------------------------------------------------#


useragents = random.choice([
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55',
	'Mozilla/5.0 (X11; Heathrow/1.4; Linux i686; rv:30) Gecko/30 Firefox/30',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'
])#Selects a Random useragent... to bypass facebooks shitty security

password = random.choice(['75!x#+FmnfW3SK','vL&pM2zVtV6NsEH4','PKc-pK2XmfRG-7B','UmE*F4aKD!cV7','eLU_U2&#MsqT#@4+','xS?mVEy!d2khDsye','L2tb+A97P=#s*WD$','wv&+&sXhrWxw7cJ','S+rD?r=z7?KaS2U','Rj?HcnN7*-jw=CKw','SQ?3Vx!J8vueyf2','cunnsjs1736jn#','lmasdks128973#!!!@'])
info = open('sms_support/phone','r')
info = info.read()


phone = info.strip().split(":",1)[0]
name = info.strip().split(":",1)[1]




SMS_AMNT = int(input(Grey+"["+Blue+"SMS"+Grey+"]-["+Blue+"10"+Grey+"]"+Green+": "+Reset))
CALL_AMNT = int(input(Grey+"["+Blue+"CALL"+Grey+"]-["+Blue+"3"+Grey+"]"+Green+": "+Reset))	



profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragents)

display = Display(visible=0, size=(800, 600))
display.start()

br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver',firefox_profile=profile)

print(Grey+"USING:"+Reset+"  "+Blue+useragents+Reset)

br.get("https://mbasic.facebook.com/reg/")
time.sleep(3)

br.find_element_by_name("firstname").send_keys(str(name))
br.find_element_by_name("lastname").send_keys(str(lastname))
br.find_element_by_name("reg_email__").send_keys(str(phone))
br.find_elements_by_css_selector("input[type='radio'][value='"+sex+"']")[0].click()

br.find_element_by_css_selector('#month > option:nth-child('+month+')').click()
br.find_element_by_css_selector('#day > option:nth-child('+day+')').click()
br.find_element_by_css_selector('#year > option:nth-child('+year+')').click()

br.find_element_by_name('reg_passwd__').send_keys(str(password))
time.sleep(2)
br.find_element_by_name('submit').click()
time.sleep(16)


while True:

	try:
		br.get("https://www.facebook.com/")
		time.sleep(11)
		br.find_element_by_link_text("Did you not get the SMS?").click()
		time.sleep(2)
		ID = ID + 1

		if ID > SMS_AMNT:
			CALLID = CALLID + 1
			if CALLID > CALL_AMNT:
				break

			else:
				br.find_element_by_partial_link_text("Call").click()
				print(Grey+"["+Blue+str(CALLID)+Grey+"] "+Red+"Called")
				time.sleep(60)


		else:
			br.find_element_by_link_text("Send SMS Again").click()
			print(Grey+"["+Blue+str(ID)+Grey+"] "+Green+"SMS sent")
			time.sleep(60)

	except Exception:
		br.get("https://mbasic.facebook.com/")
		time.sleep(11)
		br.find_element_by_name("p_pn").send_keys(str(phone))
		br.find_element_by_id("checkpointSubmitButton-actual-button").click()
		time.sleep(20)

		while True:
			if ID > SMS_AMNT:
				break
			else:
				br.find_element_by_name("p_rl").click()
				ID = ID + 1
				print(Grey+"["+Blue+str(ID)+Grey+"] "+Green+"SMS sent")
				time.sleep(60)
		break

br.close()
display.stop()
sys.exit(0)