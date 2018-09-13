#!/usr/bin/python


import os
import codecs
import time
import subprocess
import sys
import random
from pyvirtualdisplay import Display
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('base/firefox/firefox')

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

TRIES=0
ID = 0

lastname = random.choice(['diana','jakal','boreson','sinan','zanyar','lkafe','kenny','parker','faye','spivey','simon','miller','wilson','ryan','jackson','fellows','tuckler','turner','counety','baker','griffin','reynolds','andrews','dunns','barker','reid'])
useragents = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'


info = open('./sms_support/phone','r')
info = info.read()


month = random.choice(['1','2','3','4','5','6','7','8','9'])
day = random.choice(['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','24','25','26'])
year = random.choice(['1990','1994','2000','1992','1984','1986','1983','1980','1997','1987','1966','1999','1988','1989'])


let = random.choice(['lk','sa','df','kg','jq','qw','3r','ks','gt','ws','gt','lo','yh','qw'])
let1 = random.choice(['3','9','2','6','4q','qw5','31','k4','6','8s','9t','1o','8h','4w'])
num = random.choice(['16','17','18','19','20','21','22','23','24','25','26','27','28','29'])

password = random.choice(['75!x#+FmnfW3SK','vL&pM2zVtV6NsEH4','PKc-pK2XmfRG-7B','UmE*F4aKD!cV7','eLU_U2&#MsqT#@4+','xS?mVEy!d2khDsye','L2tb+A97P=#s*WD$','wv&+&sXhrWxw7cJ','S+rD?r=z7?KaS2U','Rj?HcnN7*-jw=CKw','SQ?3Vx!J8vueyf2','cunnsjs1736jn#','lmasdks128973#!!!@'])


phone = info.strip().split(":",1)[0]
name = info.strip().split(":",1)[1]

SMS_AMNT = int(input(Grey+"["+Blue+"SMS"+Grey+"]-["+Blue+"10"+Grey+"]"+Green+": "+Reset))
CALL_AMNT = int(input(Grey+"["+Blue+"CALL"+Grey+"]-["+Blue+"3"+Grey+"]"+Green+": "+Reset))


profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragents)


display = Display(visible=0, size=(800, 600))
display.start()
 

br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver',firefox_profile=profile)


print(Grey+"("+Green+"Might not Work if Phone is Used too many times of Verification"+Grey+")")
print(Grey+"USING:"+Reset+"  "+Blue+useragents+Reset)

br.get("https://accounts.google.com/SignUp?hl=en-GB")

time.sleep(14)

br.find_element_by_name("FirstName").send_keys(str(name))
br.find_element_by_name("LastName").send_keys(str(lastname))

uname = str(lastname+name+num+let1+let)

br.find_element_by_name("GmailAddress").send_keys(str(uname))
br.find_element_by_name("Passwd").send_keys(str(password))
br.find_element_by_name("PasswdAgain").send_keys(str(password))
br.find_element_by_name("BirthDay").send_keys(str(day))
br.find_element_by_name("BirthYear").send_keys(str(year))


m = '#\\:'+month+' > div:nth-child(1)'

br.find_element_by_id("BirthMonth").click()
br.find_element_by_css_selector(m).click()
sex = ':'+random.choice(['f','e'])
br.find_element_by_id('Gender').click()
br.find_element_by_id(sex).click()

br.find_element_by_name('RecoveryPhoneNumber').clear()
br.find_element_by_name('RecoveryPhoneNumber').send_keys(str(phone))
time.sleep(10)

br.find_element_by_name('submitbutton').click()
time.sleep(7)
while True:
	try:
		br.find_element_by_id('tos-scroll-button').click()
		time.sleep(4)
	except Exception:
		br.find_element_by_id('iagreebutton').click()
		time.sleep(20)
		break

while True:
	try:
		if ID == SMS_AMNT:
			break

		else:
			br.find_element_by_name("SendCode").click()
			ID = ID + 1
			print(Grey+"["+Blue+str(ID)+Grey+"] "+Green+"SMS sent")
			time.sleep(55)
			br.find_element_by_id('try-again').click()
			time.sleep(15)

	except Exception:
		break


while True:
	try:
		if TRIES == CALL_AMNT:
			break

		else:
			TRIES = TRIES + 1
			br.find_element_by_id('signupidvmethod-voice').click()
			time.sleep(2)
			br.find_element_by_name("SendCode").click()
			print(Grey+"["+Blue+str(TRIES)+Grey+"] "+Red+"Called")
			time.sleep(55)
			br.find_element_by_id('try-again').click()
			time.sleep(15)

	except Exception:
		print(Green+"Finished")
		br.close()
		display.stop()
		time.sleep(10)
		break



sys.exit(0)