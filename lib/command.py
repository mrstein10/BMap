import subprocess
import os

commands = ["clear", "ls"]
ret = False

def sanitizeCom(command) -> bool:
	try:
		for com in commands:
			if com in command:
				systemCommand(command)
				ret = True
				break
			else:
				ret = False
	except Exception as e:
		print(e)
		ret = False	
	return ret

def systemCommand(command):
	print(command)
	os.system(command)
	#subprocess.run([command], check = True)