#UNDER CONSTRUCTION, DON'T USE IT!!!
import MySQLdb, sys, os, json

dbAddr = 'localhost' #change with ip in case of remote db
dbUser = '' #fill with username that can access the db
dbPass = '' #fill with password of username
dbName = 'totdb'
currdir = sys.argv[1]

'''data = json.load(open('localhost.port'))
print data[1]'''
############### INIT THE DB
db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()

domain_name = currdir.split('/')[len(currdir.split('/'))-1]
# some code here, from json to db

#cursor.execute('''INSERT INTO domain (id, adder) VALUES (%s, %s)''', ('test1', 'test2'))
#db.commit()
#cursor.execute('''SELECT * FROM domain''')
#print cursor.fetchone()

db.close()
