from src import *
import src.target as target

if __name__ == "__main__":
	SYM=""
	targets=""
	while True:
		command = input(f"[{SYM}] -> ")
		if not sanitizeCom(command):
			if "exit" in command and SYM == "":
				break
			elif "back" in command or "exit" in command:
				SYM =""
			elif "help" in command and SYM == "":
				globalHelp()
			elif "target" in command:
				target.main()
			else:
				if "use" in command:
					SYM = useModule(command)
				else:
					if "scanner" in SYM:
						execModule(command,targets)
					else:
						print("command not found")