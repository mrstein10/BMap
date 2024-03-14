from modules.scanner.ScanInformation import * 
from modules.scanner.options import *
from lib.command import sanitizeCom
from src.db import *
from src.target import *
from modules.scanner.nmap import *

closeCommand = ["back", "exit", "close"]

def execModule(command,targets=""):
	main(command, targets)

def main(command,targets=""):
	match command:
		#case command if "set lhost" in command:
		#	ip = command.split(" ")[2]
		#	setLHost(ip)
		#	print(f"LHOST -> {ip}")
		case "run":
			mainNMap("127.0.0.1")
		case "exploit":
			mainNMap("127.0.0.1")
		case "results":
			#IPServices
			beautifyServices()
		case command if "help" in command:
			showHelp()
		case "show options":
			showOptions(targets)
		case "clear":
			sanitizeCom("clear")
		case command if command in closeCommand:
			print("Close command")
			SYM=""