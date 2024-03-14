import os
import subprocess
#from modules.scanner.main import *
#from modules.exploiter.exploits import *
from lib.command import sanitizeCom

def main() -> None:
    return 0

def showModules():
    for file in os.listdir('./modules/'):
        if not "__pycache__" in file :
            if not "init" in file:
                print(file)

def useModule(command):

    passed = sanitizeCom(command)

    if not passed:
        if "scanner" in command:
            return "scanner"
        if "exploits" in command:
            return "exploits"
    else:
        return ""