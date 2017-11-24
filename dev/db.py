import MySQLdb, sys, os, json, glob

dbAddr = '' #change with ip in case of remote db
dbUser = '' #fill with username that has access to db
dbPass = '' #fill with password related to username
dbName = 'totdb' #needs to exist (read README.txt file)!
adderName = '' #fill with your name to record who added info inside db

#Pass path with last slash, e.g. '/path/to/directory/report/'
report_dir = sys.argv[1]
dir_list = glob.glob(report_dir + '*/')

db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()

for i in range(len(dir_list)):
    #Analyzed domain check and update
    domain = dir_list[i].split('/')[len(dir_list[i].split('/')) - 2]
    cursor.execute('''SELECT id FROM domain WHERE id=%s''', (domain,))
    if str(type(cursor.fetchone()))=="<type 'NoneType'>":
        cursor.execute('''INSERT INTO domain (id, adder, analyzed) VALUES (%s, %s, %s)''', (domain, adderName, 1))
        db.commit()
    else:
        cursor.execute('''UPDATE domain SET analyzed=1 WHERE id=%s''', (domain,))
        db.commit()

    #Discovered domains check and update
    if os.path.isfile(dir_list[i] + 'HS.txt'):
        hs = open(dir_list[i] + 'HS.txt' , "r")
        onions = []
        for l in hs.readlines():
            onions.append(l.strip("\n"))
        hs.close()
        for oni in onions:
            try:
                cursor.execute('''INSERT INTO domain (id, adder, analyzed) VALUES (%s, %s, %s)''', (oni, adderName, 0))
                db.commit()
            except:
                pass
            try:
                cursor.execute('''INSERT INTO find (domain1, domain2) VALUES (%s, %s)''', (domain, oni))
                db.commit()
            except:
                pass

    #Discovered btcaddresses check and update
    if os.path.isfile(dir_list[i] + 'btcs.txt'):
        btc = open(dir_list[i] + 'btcs.txt' , "r")
        btcadds = []
        for l in btc.readlines():
            btcadds.append(l.strip("\n"))
        btc.close()
        for addr in btcadds:
            try:
                cursor.execute('''INSERT INTO btcaddress (id) VALUES (%s)''', (addr,))
                db.commit()
            except:
                pass
            try:
                cursor.execute('''INSERT INTO contains_btc (domain, btcaddress) VALUES (%s, %s)''', (domain, addr))
                db.commit()
            except:
                pass

    #Discovered emails check and update
    if os.path.isfile(dir_list[i] + 'emails.txt'):
        email = open(dir_list[i] + 'emails.txt' , "r")
        mails = []
        for l in email.readlines():
            mails.append(l.strip("\n"))
        email.close()
        for mail in mails:
            try:
                cursor.execute('''INSERT INTO email (address) VALUES (%s)''', (mail,))
                db.commit()
            except:
                pass
            try:
                cursor.execute('''INSERT INTO contains_mail (domain, email) VALUES (%s, %s)''', (domain, mail))
                db.commit()
            except:
                pass

    #Portscan results storing on db
    if os.path.isfile(dir_list[i] + domain + '.port'):
        data = json.load(open(dir_list[i] + domain + '.port', "r"))
        for entry in data:
            try:
                cursor.execute('''INSERT INTO have (domain, port, status, banner) VALUES (%s, %s, %s, %s)''', (domain, entry['port'], entry['status'], entry['banner']))
                db.commit()
            except:
                pass

db.close()
