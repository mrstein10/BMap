import sqlite3

connection = sqlite3.connect("src/database/bmap.db")

def getAllTargets() -> list:
	cur = connection.cursor()
	cur.execute("SELECT ip FROM targets")

	rows = cur.fetchall()
	cur.close()

	return rows
 
def getUsedTarget() -> list:
	cur = connection.cursor()
	cur.execute(f"SELECT ip FROM targets WHERE inUse=1")

	rows = cur.fetchall()
	cur.close
	return rows

def getTarget(ip) -> list:
	cur = connection.cursor()
	cur.execute(f"SELECT ip FROM targets WHERE ip=\"{ip}\"")

	rows = cur.fetchall()
	if len(rows) > 0:
		cur.execute(f"UPDATE targets SET inUse=0 WHERE inUse=1")
		cur.execute(f"UPDATE targets SET inUse=1 WHERE ip=\"{ip}\"")
		connection.commit()
	cur.close

	return rows

def setTarget(ip):
	cur = connection.cursor()
	
	cur.execute(f"UPDATE targets SET inUse=0 WHERE inUse=1")
	cur.execute(f"INSERT INTO targets (ip,inUse) VALUES (\"{ip}\",1)")
	connection.commit()
	
	cur.close()

def setPort(ip,port):
	cur = connection.cursor
	if port is list:
		for item in port:
			cur.execute(f"INSERT INTO ports (ip,port) VALUES ({item},\"{ip}\")")
	else:
		cur.execute(f"INSERT INTO ports (ip,port) VALUES ({port},\"{ip}\")")
	connection.commit()
	
	cur.close()