import os
import subprocess
from modules.scanner.main import *
from modules.exploiter.exploits import *
from lib.command import sanitizeCom

def showModules():
    for file in os.listdir('./modules/'):
        if file!="__pycache__":
            print(file)

def useModule(command):

    passed = sanitizeCom(command)

    if not passed:
        match command:
            case command if "scanner" in command:
                return "scanner"
            case command if "exploits" in command:
                return "exploits"
            case "show modules":
                showModules()
                return ""
    else:
        return ""