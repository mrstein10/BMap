import nmap3

#
# HIER NOCH DIE JSON VERARBEITUNG IMPLEMENTIEREN
#

nmap = nmap3.Nmap()

def mainNMap(ip) -> None:
    results = nmap.scan_top_ports(ip)
    print(results)

def scanTopPorts(ip) -> None:
    results = nmap.scan_top_ports(ip)
    return results

def versionDetection(ip) -> None:
    results = nmap.nmap_version_detection(ip)