import MySQLdb, sys, os

dbAddr = 'localhost' #change with ip in case of remote db
dbUser = '' #fill with username that can access the db
dbPass = '' #fill with password of username
dbName = 'totdb'

############### INIT THE DB
db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()

# some code here, from json to db

#cursor.execute('''INSERT INTO domain (id, adder) VALUES (%s, %s)''', ('test1', 'test2'))
#db.commit()
#cursor.execute('''SELECT * FROM domain''')
#print cursor.fetchone()

db.close()
