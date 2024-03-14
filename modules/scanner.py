import sys
sys.path.insert(0,"modules/scanner/")
import modules
import ScanInformation
import nmap
import target

class Scanner(modules.ModulesClass):
    closeCommand = ["back", "exit", "close"]

    def execModule(object, command, SYM=""):
        if "scanner" in command:
            SYM = "scanner"
        elif "scanner" in SYM:
            print("Command scanner main")
            main(command,SYM)
            SYM = "scanner"
        return SYM

def main(command,SYM):
    if "searchsploit" in command:
        return "searchsploit"
    elif "nmap" in command:
        nmap.mainNMap(SYM)

'''
def main(command,targets=""):
    match command:
        case command if "run" in command or "exploit" in command:
            nmap.mainNMap("127.0.0.1")
        case "exploit":
            nmap.mainNMap("127.0.0.1")
        case "results":
            ScanInformation.beautifyServices()
        case command if "help" in command:
            showHelp()
        case "show options":
            showOptions(targets)
'''
def searchExploit(service):
    search = f"searchsploit {service}"
    #exploit='searchsploit "upnp" | grep "Realtek" | cut -d"|" -f2 | cut -d"/" -f3'
    return search

def showOptions(targets=""):
    print(targets)
    print("+----------------------------------------------------------------------+ \
    \n|                     |   Configuration   |                            | \
    \n|                     +-------------------+                            |")
    if targets != "":
        for host,port in targets:
            print(f"\n|     LHOST   {host}                                                     | \
        \n|     LPORTS  {port}                                                     |")
    else:
        print("\n|     LHOST   <none>                                                   | \
        \n|     LPORTS  <none>                                                   |")
    print("\n|                                                                      | \
    \n+----------------------------------------------------------------------+\n\n")

def showHelp():
    print("\n+----------------------------------------------------------------------+ \
    \n|                         |    Help    |                               | \
    \n|                         +------------+                               | \
    \n|                                                                      | \
    \n|      results  Show the results from the scan in a table.             | \
    \n|                                                                      | \
    \n+----------------------------------------------------------------------+\n\n")