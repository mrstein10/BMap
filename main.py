#from src import *
import src.target as target
import src.help as help
import lib.command as commands
import lib.logic as logic
import modules.scanner.main as scanMain


if __name__ == "__main__":
	SYM=""
	targets=""
	while True:
		command = input(f"[{SYM}] -> ")
		if not commands.sanitizeCom(command):
			if "exit" in command and SYM == "":
				break
			elif "back" in command or "exit" in command:
				SYM =""
			elif "help" in command and SYM == "":
				help.globalHelp()
			elif "target" in command:
				target.main(command)
			elif "show" in command:
				logic.showModules()
			else:
				if "use" in command:
					SYM = logic.useModule(command)
				else:
					if "scanner" in SYM:
						scanMain.execModule(command,targets)
					else:
						print("command not found")
						help.globalHelp()