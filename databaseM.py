import MySQLdb	

def addToTable(l):
	db = MySQLdb.connect("localhost","root","1234","log")
	cursor = db.cursor()
	sql = "INSERT INTO `packets` VALUES(null,'%s','%s','%s','%s',CURDATE(),CURTIME(), '%s')" % (l[0],l[1],l[2],l[3], l[4])
	cursor.execute(sql)
	db.commit()
	db.close()