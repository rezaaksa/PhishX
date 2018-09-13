reset
echo ""
echo "                     #################################"
echo "                                 -PHISHX- "
echo "                     #################################"
echo "                         [+]: MADE BY WEEBSEC :[+]"
echo "                     #################################"
echo ""
echo "                           ONLY run this as ROOT"
echo "               press ENTER to continue with the Installation"

read varos

rm -r firefox &> /dev/null
rm -r base &> /dev/null
rm ngrok* &> /dev/null

mkdir base

echo ""



ARCH="$(arch)"
echo "Detecting Arch: ${ARCH}"
echo " "
chmod -R 777 ./
apt-get update -y  &> /dev/null | echo "UPDATING"
apt-get install python3 python3-setuptools python3-pip xvfb sendemail php xterm -y &> /dev/null | echo "RESOLVING DEPENDENCIES"

pip3 install pyvirtualdisplay &> /dev/null | echo "INSTALLING PYTHON REQUIREMENTS"
pip3 install selenium &> /dev/null
pip3 install procname &> /dev/null
pip3 install requests &> /dev/null

if [[ ${ARCH} == "i686" || ${ARCH} == "i686" ]]; then
	wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
else
	if [[ ${ARCH} == "i386" || ${ARCH} == "i386" ]]; then
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
	else
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
	fi
fi


tar xvzf GECKO.tar.gz &> /dev/null | echo "EXTRACTING GECKODRIVER"
chmod +x geckodriver
mv geckodriver base/ | echo "MOVING GECKODRIVER TO THE RIGHT DIR"

if [[ ${ARCH} == "i686" || ${ARCH} == "i686" ]]; then
        wget -O firefox.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-i686/en-US/firefox-52.9.0esr.tar.bz2 &> /dev/null | echo "DOWNLOADING FIREFOX"
else
	wget https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-x86_64/en-US/firefox-52.9.0esr.tar.bz2 -O firefox.tar.bz2 &> /dev/null | echo "DOWNLOADING FIREFOX"
fi


tar xvjf firefox.tar.bz2 &> /dev/null | echo "EXTRACTING FIREFOX"
chmod -R 777 firefox/
mv firefox base/ &> /dev/null | echo "MOVING FIREFOX TO THE RIGHT DIR"

if [[ ${ARCH} == "i686" || ${ARCH} == "i686" ]]; then
	wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip &> /dev/null | echo "INSTALLING NGROK"
else

	if [[ ${ARCH} == "i386" || ${ARCH} == "i386" ]]; then
	        wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-i386.zip &> /dev/null | echo "INSTALLING NGROK"
	else
	        wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip &> /dev/null | echo "INSTALLING NGROK"
	fi
fi


unzip NGROK.zip &> /dev/null | echo "UNZIPPING NGROK"

rm -r ngrok-* &> /dev/null | echo "CLEANING UP"
rm *.zip
rm *.tar.gz
rm *.tar.bz2

echo " "
echo "[DONE]"
