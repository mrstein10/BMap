from .db import *

def main(command):
    if "set" in command:
        ip = command.split(" ")[2]
        setLHost(ip)
        print(f"LHOST -> {ip}")
    elif "get" in command:
        getHosts()

def setLHost(ip) -> None:
	target = getTarget(ip)
	if not target:
		setTarget(ip)

def getHosts() -> None:
    hosts = getAllTargets()
    number = 1
    for host in hosts:
        print(f"{number} {host[0]}")
        number+=1