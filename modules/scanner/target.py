# Settarget
#function settarget(){
#	export ip_target=$1
#        if [ $# -eq 1 ]; then
#        	echo "$1" > "${HOME}/.config/polybar/shapes/scripts/target"
#        elif [ $# -gt 2 ]; then
#        	echo "settarget [IP] [NAME] | settarget [IP]"
#        else
#        	echo "$1" "$2" > "${HOME}/.config/polybar/shapes/scripts/target"
#        fi
#}
from lib.command import sanitizeCom

#Scan Target
def targetScan(ip):
	print("\n[*] SCANNING TARGET")
	#settarget "$1"
	sanitizeCom(f"nmap -T4 -sV {ip} -oG nmapscan > /dev/null")
	#nmap -T4 -sV "$ip_target" -oG nmapscan > /dev/null
	print("\n[*] SCAN COMPLETED")