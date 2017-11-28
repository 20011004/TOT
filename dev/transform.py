import json, subprocess, os, MySQLdb

from Maltego import *

pathToReports = "/reports/"

dbAddr = '' #change with ip in case of remote db
dbUser = '' #fill with username that has access to db
dbPass = '' #fill with password related to username
dbName = 'totdb' #needs to exist (read README.txt file)!

#Domains that contain the specified email
def domainsWithEmail(email):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT domain FROM contains_mail WHERE email=%s''', (email,))
    result = cursor.fetchall()
    db.close()
    return result

#Domains that contain the specified btc
def domainsWithBtc(btc):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT domain FROM contains_btc WHERE btcaddress=%s''', (btc,))
    result = cursor.fetchall()
    db.close()
    return result

#Domains that contain the specified port with specified status
def domainsWithPort(port, status):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT domain, banner FROM have WHERE port=%s AND status=%s''', (port, status))
    result = cursor.fetchall()
    db.close()
    return result

#Domains that contain the specified domain
def domainsWithDomain(domain):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT domain1 FROM find WHERE domain2=%s''', (domain,))
    result = cursor.fetchall()
    db.close()
    return result

#Emails found in specified domain
def mailsInDomain(domain):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT email FROM contains_mail WHERE domain=%s''', (domain,))
    result = cursor.fetchall()
    db.close()
    return result

#Btcs found in specified domain
def btcsInDomain(domain):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT btcaddress FROM contains_btc WHERE domain=%s''', (domain,))
    result = cursor.fetchall()
    db.close()
    return result

#Ports with specified status found in specified domain
def portsInDomain(status, domain):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT port, banner FROM have WHERE status=%s AND domain=%s''', (status, domain))
    result = cursor.fetchall()
    db.close()
    return result

#Domains found in specified domain
def domainsInDomain(domain):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT domain2 FROM find WHERE domain1=%s''', (domain,))
    result = cursor.fetchall()
    db.close()
    return result

#Mails inside the db
def totalEmails():
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT count(*) FROM email''')
    result = int(cursor.fetchall()[0][0])
    db.close()
    return result

#Btcs inside the db
def totalBtcs():
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT count(*) FROM btcaddress''')
    result = int(cursor.fetchall()[0][0])
    db.close()
    return result

#Domains inside the db
def totalDomains():
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT count(*) FROM domain''')
    result = int(cursor.fetchall()[0][0])
    db.close()
    return result

#Number of domains with the specified port with status open
def totalDomainsWithOpenPort(port):
    db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
    cursor = db.cursor()
    cursor.execute('''SELECT count(*) FROM have WHERE port=%s AND status=%s''', (port, "open"))
    result = int(cursor.fetchall()[0][0])
    return result

def trx_onionDetected(Domain):
    TRX = MaltegoTransform()

    try:
        servs = portsInDomain("open", Domain.Value)
        if len(servs) > 0:
            for s in servs:
                TRX.addEntity("maltego.Service",str(int(s[0])) + ":" + str(s[1]))
        else:
            TRX.addUIMessage("No services found in " + str(Domain.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionPGPKeys(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This transform is not ready to be used.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionIpAddress(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This transform is not ready to be used.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionEmail(Domain):
    TRX = MaltegoTransform()

    try:
        ems = mailsInDomain(Domain.Value)
        if len(ems) > 0:
            for i in ems:
                TRX.addEntity("maltego.EmailAddress",str(i).strip(",'()"))
        else:
            TRX.addUIMessage("No emails found in " + str(Domain.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionBitcoin(Domain):
    TRX = MaltegoTransform()

    try:
        btcs = btcsInDomain(Domain.Value)
        if len(btcs) > 0:
            for b in btcs:
                TRX.addEntity("maltego.BtcAddress",str(b).strip(",'()"))
        else:
            TRX.addUIMessage("No Bitcoin addresses found in " + str(Domain.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedServices(Domain):
    TRX = MaltegoTransform()

    try:
        doms = domainsInDomain(Domain.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d).strip(",'()"))
        else:
            TRX.addUIMessage("No onion domains found in " + str(Domain.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedDomains(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This transform is not ready to be used.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithDomain(Domain):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithDomain(Domain.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d).strip(",'()"))
        else:
            TRX.addUIMessage("No domains found with this domain " + str(Domain.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithBtc(BtcAddress):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithBtc(BtcAddress.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d).strip(",'()"))
        else:
            TRX.addUIMessage("No domains found with this Bitcoin address " + str(BtcAddress.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithEmail(Email):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithEmail(Email.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d).strip(",'()"))
        else:
            TRX.addUIMessage("No domains found with this Email " + str(Email.Value),UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()
