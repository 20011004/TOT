import MySQLdb, sys, os, json, glob

dbAddr = 'localhost' #change with ip in case of remote db
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
    hs = open(dir_list[i] + 'HS.txt' , "r")
    onions = []
    for l in hs.readlines():
        onions.append(l.strip("\n"))
    hs.close()
    for oni in onions:
        cursor.execute('''SELECT id FROM domain WHERE id=%s''', (oni,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO domain (id, adder, analyzed) VALUES (%s, %s, %s)''', (oni, adderName, 0))
            db.commit()
        cursor.execute('''SELECT domain1, domain2 FROM find WHERE domain1=%s AND domain2=%s''', (domain, oni))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO find (domain1, domain2) VALUES (%s, %s)''', (domain, oni))
            db.commit()

    #Discovered btcaddresses check and update
    btc = open(dir_list[i] + '/btcs.txt' , "r")
    btcadds = []
    for l in btc.readlines():
        btcadds.append(l.strip("\n"))
    btc.close()
    for addr in btcadds:
        cursor.execute('''SELECT id FROM btcaddress WHERE id=%s''', (addr,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO btcaddress (id) VALUES (%s)''', (addr,))
            db.commit()
        cursor.execute('''SELECT domain, btcaddress FROM contains_btc WHERE domain=%s AND btcaddress=%s''', (domain, addr))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO contains_btc (domain, btcaddress) VALUES (%s, %s)''', (domain, addr))
            db.commit()

    #Discovered emails check and update
    email = open(dir_list[i] + '/emails.txt' , "r")
    mails = []
    for l in email.readlines():
        mails.append(l.strip("\n"))
    email.close()
    for mail in mails:
        cursor.execute('''SELECT address FROM email WHERE address=%s''', (mail,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO email (address) VALUES (%s)''', (mail,))
            db.commit()
        cursor.execute('''SELECT domain, email FROM contains_mail WHERE domain=%s AND email=%s''', (domain, mail))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO contains_mail (domain, email) VALUES (%s, %s)''', (domain, mail))
            db.commit()

    #Portscan results storing on db
    data = json.load(open(dir_list[i] + '/' + domain + '.port'))
    port_stuff = []
    for entry in data:
        #port_stuff.append((domain, entry['port'], entry['status'], entry['banner']))
        cursor.execute('''SELECT domain, port FROM have WHERE domain=%s AND port=%s''', (domain, entry['port']))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO have (domain, port, status, banner) VALUES (%s, %s, %s, %s)''', (domain, entry['port'], entry['status'], entry['banner']))
            db.commit()

db.close()
