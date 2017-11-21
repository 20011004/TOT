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
    hs = open(dir_list[i] + '/HS.txt' , "r")
    onions = []
    domain_stuff = []
    for l in hs.readlines():
        onions.append(l.strip("\n"))
    hs.close()
    for oni in onions:
        cursor.execute('''SELECT id FROM domain WHERE id=%s''', (oni,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO domain (id, adder, analyzed) VALUES (%s, %s, %s)''', (oni, adderName, 0))
            db.commit()
        domain_stuff.append((domain,oni))
    cursor.executemany('''INSERT INTO find (domain1, domain2) VALUES (%s, %s)''', domain_stuff)
    db.commit()

    #Discovered btcaddresses check and update
    btc = open(dir_list[i] + '/btcs.txt' , "r")
    btcadds = []
    btc_stuff = []
    for l in btc.readlines():
        btcadds.append(l.strip("\n"))
    btc.close()
    for addr in btcadds:
        cursor.execute('''SELECT id FROM btcaddress WHERE id=%s''', (addr,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO btcaddress (id) VALUES (%s)''', (addr,))
            db.commit()
        btc_stuff.append((domain,addr))
    cursor.executemany('''INSERT INTO contains_btc (domain, btcaddress) VALUES (%s, %s)''', btc_stuff)
    db.commit()

    #Discovered emails check and update
    email = open(dir_list[i] + '/emails.txt' , "r")
    mails = []
    mail_stuff = []
    for l in email.readlines():
        mails.append(l.strip("\n"))
    email.close()
    for mail in mails:
        cursor.execute('''SELECT address FROM email WHERE address=%s''', (mail,))
        if str(type(cursor.fetchone()))=="<type 'NoneType'>":
            cursor.execute('''INSERT INTO email (address) VALUES (%s)''', (mail,))
            db.commit()
        mail_stuff.append((domain,mail))
    cursor.executemany('''INSERT INTO contains_mail (domain, email) VALUES (%s, %s)''', mail_stuff)
    db.commit()

    #Portscan results storing on db
    data = json.load(open(dir_list[i] + '/' + domain + '.port'))
    port_stuff = []
    for entry in data:
        port_stuff.append((domain, entry['port'], entry['status'], entry['banner']))
    cursor.executemany('''INSERT INTO have (domain, port, state, banner) VALUES (%s, %s, %s, %s)''', port_stuff)
    db.commit()

db.close()
