import matplotlib.pyplot as plt
import MySQLdb
import pylab

# def plotGraph(x,y,my_yticks):
# 	plt.plot(x,y, ':Dr')
# 	plt.yticks(y, my_yticks)
# 	plt.gcf().autofmt_xdate()
# 	# pylab.ion()
# 	plt.show()

def connectDatabase2(date, interface):
	x = []
	y = []
	my_yticks = []
	db = MySQLdb.connect("localhost","root","1234","log")
	cursor = db.cursor()
	sql = "SELECT * FROM packets WHERE `Date`='%s' AND `interface`='%s'" % (date, interface)
	cursor.execute(sql)
	uniqueIp = [0]
	i = 0

	for item in cursor:
		sourceIp = item[1]
		destIP = item[2]

		if sourceIp == "172.25.12.127":
			if destIP not in uniqueIp:
				uniqueIp.insert(i,str(destIP))
				y.append(i)
				my_yticks.append(str(destIP))
				i += 1

	uniqueIp.pop()
	i = 0
	for i in range(0,24):
		x.append(i)

	time = [0]
	b = [0]
	db.commit()
	db.close()
	j = 0
	for item in cursor:
		sourceIp = item[1]
		if sourceIp == "172.25.12.127":
			a = str(item[6]).split(":")
			hr = int(a[0])
			mi = int(a[1])
			sec = int(a[2])
			time.insert(j,hr + mi/60.0 + sec/3600.0)
			b.insert(j,uniqueIp.index(str(item[2])))
			j += 1

	time.pop()
	b.pop()
	plt.plot(time,b,':Dr',)
	plt.yticks(y, my_yticks)
	pylab.ion()
	plt.show()

# This window is not closing unless we close all the windows
# connectDatabase2("2016-03-09")