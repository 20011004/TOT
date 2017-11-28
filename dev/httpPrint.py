import MySQLdb, os

dbAddr = '' #change with ip in case of remote db
dbUser = '' #fill with username that has access to db
dbPass = '' #fill with password related to username
dbName = 'totdb' #needs to exist (read README.txt file)!

reports = "/home/scanner/"

db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()
cursor.execute('''SELECT domain FROM have WHERE port=80 and state=%s''', ('open',))
result = cursor.fetchall()
db.close()

os.chdir(reports)
f = open("http.txt", "w")
for elem in result:
    f.write("%s\n" %elem[0])
f.close()
