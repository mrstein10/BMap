import nmap3
import src.db as database
import lib.command as com

#
# HIER NOCH DIE JSON VERARBEITUNG IMPLEMENTIEREN
#

nmap = nmap3.Nmap()

# Hier Schleife des Moduls die die optionen und einstellungen speichert und exploiten kann
def mainNMap(SYM) -> None:
    SYMModule = "NMAP"
    while True:
        command = input(f"[{SYM}][{SYMModule}] -> ")
        targets = database.getUsedTarget()
        if not com.sanitizeCom(command):
            if "exit" in command:
                break
            if "show options" in command:
                showOptions(targets)
    #results = nmap.scan_top_ports(ip)
    #print(results)

def scanTopPorts(ip) -> None:
    results = nmap.scan_top_ports(ip)
    return results

def versionDetection(ip) -> None:
    results = nmap.nmap_version_detection(ip)

def showOptions(targets) -> None:
    print("+----------------------------------------------------------------------+ \
    \n|                     |   Configuration   |                            | \
    \n|                     +-------------------+                            |")
    if len(targets) > 0:
        print(f"\n|     LHOST   {targets[0][0]}                                                     | \
        \n|     LPORTS  {targets[0][0]}                                                     |")
    else:
        print("\n|     LHOST   <none>                                                   | \
        \n|     LPORTS  <none>                                                   |")
    print("\n|                                                                      | \
    \n+----------------------------------------------------------------------+\n\n")
