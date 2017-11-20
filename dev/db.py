#UNDER CONSTRUCTION, DON'T USE IT!!!

import MySQLdb, sys, os, json, glob

dbAddr = 'localhost' #change with ip in case of remote db
dbUser = '' #fill with username that has access to db
dbPass = '' #fill with password related to username
dbName = 'totdb' #needs to exist (read README.txt file)!
adderName = '' #fill with your name to record who added info inside db

report_dir = sys.argv[1]
dir_list = glob.glob(report_dir + '/*/')

db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()

for i in range(len(dir_list)):
    domain = dir_list[i].split('/')[len(dir_list[i].split('/')) - 2]
    cursor.execute('''SELECT id FROM domain WHERE id=%s''', (domain,))
    if str(type(cursor.fetchone()))=="<type 'NoneType'>":
        cursor.execute('''INSERT INTO domain (id, adder) VALUES (%s, %s)''', (domain, adderName))
        db.commit()

'''data = json.load(open('localhost.port'))
print data[1]'''
############### INIT THE DB

# some code here, from json to db

#cursor.execute('''INSERT INTO domain (id, adder) VALUES (%s, %s)''', ('test1', 'test2'))
#db.commit()
#cursor.execute('''SELECT * FROM domain''')
#print cursor.fetchone()

db.close()
