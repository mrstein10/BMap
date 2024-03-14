#from src import *
import src.target as target
import src.help as help
import lib.command as commands
import lib.logic as logic
#import modules.scanner.main as scanMain
from modules import ModulesClass


if __name__ == "__main__":
	SYM=""
	targets=""
	_lhost=""
	while True:
		command = input(f"[{SYM}] -> ")
		if not commands.sanitizeCom(command):
			if "show lhost" in command:
				print(_lhost)

			if "exit" in command and SYM == "":
				break
			elif "back" in command or "exit" in command:
				SYM =""
			elif "help" in command and SYM == "":
				help.globalHelp()
			elif "target" in command or "lhost" in command:
				_lhost = target.main(command)
			elif "show modules" in command:
				logic.showModules()
			elif "use" in command or SYM:
				for p in ModulesClass.plugins:
					inst = p()
					SYM = inst.execModule(command, SYM)
			else:
				help.globalHelp()