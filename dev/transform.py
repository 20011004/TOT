import json, subprocess, os, MySQLdb

from Maltego import *

pathToReports = "/reports/"

dbAddr = '' #change with ip in case of remote db
dbUser = '' #fill with username that has access to db
dbPass = '' #fill with password related to username
dbName = 'totdb' #needs to exist (read README.txt file)!

db = MySQLdb.connect(host=dbAddr, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()

#Domains that contain the specified email
def domainsWithEmail(email):
    cursor.execute('''SELECT domain FROM contains_mail WHERE email=%s''', (email,))
    return cursor.fetchall()

#Domains that contain the specified btc
def domainsWithBtc(btc):
    cursor.execute('''SELECT domain FROM contains_btc WHERE btcaddress=%s''', (btc,))
    return cursor.fetchall()

#Domains that contain the specified port with specified status
def domainsWithPort(port, status):
    cursor.execute('''SELECT domain FROM have WHERE port=%s AND status=%s''', (port, status))
    return cursor.fetchall()

#Domains that contain the specified domain
def domainsWithDomain(domain):
    cursor.execute('''SELECT domain1 FROM find WHERE domain2=%s''', (domain,))
    return cursor.fetchall()

#Emails found in specified domain
def mailsInDomain(domain):
    cursor.execute('''SELECT email FROM contains_mail WHERE domain=%s''', (domain,))
    return cursor.fetchall()

#Btcs found in specified domain
def btcsInDomain(domain):
    cursor.execute('''SELECT btcaddress FROM contains_btc WHERE domain=%s''', (domain,))
    return cursor.fetchall()

#Ports with specified status found in specified domain
def portsInDomain(status, domain):
    cursor.execute('''SELECT port FROM have WHERE status=%s AND domain=%s''', (status, domain))
    return cursor.fetchall()

#Domains found in specified domain
def domainsInDomain(domain):
    cursor.execute('''SELECT domain2 FROM find WHERE domain1=%s''', (domain,))
    return cursor.fetchall()

def trx_onionDetected(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            if str(data["webDetected"]) == "True":
                wwweb = TRX.addEntity("maltego.Website",Domain.Value)
            else:
                TRX.addUIMessage("Web not detected",UIM_PARTIAL)
            if str(data["sshDetected"]) == "True":
                TRX.addEntity("maltego.Service","22:ssh")
            else:
                TRX.addUIMessage("Ssh not detected",UIM_PARTIAL)
            if str(data["ricochetDetected"]) == "True":
                TRX.addEntity("maltego.Service","9878:ricochet")
            else:
                TRX.addUIMessage("Ricochet not found",UIM_PARTIAL)
            if str(data["ricochetDetected"]) == "True":
                TRX.addEntity("maltego.Service","6676:irc")
            else:
                TRX.addUIMessage("IRC not found",UIM_PARTIAL)
            if str(data["ftpDetected"]) == "True":
                TRX.addEntity("maltego.Service","21:ftp")
            else:
                TRX.addUIMessage("Ftp not found",UIM_PARTIAL)
            if str(data["ftpDetected"]) == "True":
                TRX.addEntity("maltego.Service","25:smtp")
            else:
                TRX.addUIMessage("SMTP not found",UIM_PARTIAL)
            if str(data["bitcoinDetected"]) == "True":
                TRX.addEntity("maltego.Service","8333:bitcoin")
            else:
                TRX.addUIMessage("Bitcoin not found",UIM_PARTIAL)
            if str(data["mongodbDetected"]) == "True":
                TRX.addEntity("maltego.Service","27017:mongodb")
            else:
                TRX.addUIMessage("MongoDB not found",UIM_PARTIAL)
            if str(data["vncDetected"]) == "True":
                TRX.addEntity("maltego.Service","5900:vnc")
            else:
                TRX.addUIMessage("VNC not found",UIM_PARTIAL)
            if str(data["xmppDetected"]) == "True":
                TRX.addEntity("maltego.Service","5222:xmpp")
            else:
                TRX.addUIMessage("XMPP not found",UIM_PARTIAL)
            if str(data["skynetDetected"]) == "True":
                TRX.addUIMessage("Skynet DETECTED",UIM_PARTIAL)
            else:
                TRX.addUIMessage("Skynet NOT detected",UIM_PARTIAL)
            if str(data["tlsDetected"]) == "True":
                wwweb.setNote("TLS")
            else:
                pass
        else:
            TRX.addUIMessage(str(Domain.Value) + " not scanned.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionPGPKeys(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This is not ready.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionIpAddress(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This is not ready.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionEmail(Domain):
    TRX = MaltegoTransform()

    try:
        ems = mailsInDomain(Domain.Value)
        if len(ems) > 0:
            for i in ems:
                TRX.addEntity("maltego.EmailAddress",str(i))
        else:
            TRX.addUIMessage(str(Domain.Value) + " not scanned.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionBitcoin(Domain):
    TRX = MaltegoTransform()

    try:
        btcs = btcsInDomain(Domain.Value)
        if len(btcs) >:
            for b in btcs:
                TRX.addEntity("maltego.BtcAddress",str(b))
        else:
            TRX.addUIMessage(str(Domain.Value) + " not scanned.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedServices(Domain):
    TRX = MaltegoTransform()

    try:
        doms = domainsInDomain(Domain.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d))
        else:
            TRX.addUIMessage(str(Domain.Value) + " not scanned.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedDomains(Domain):
    TRX = MaltegoTransform()

    TRX.addUIMessage("This is not ready.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithDomain(Domain):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithDomain(Domain.Value)
        if len(doms) > 0:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(d))
        else:
            TRX.addUIMessage(str(Domain.Value) + " not scanned.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithBtc(BtcAddress):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithBtc(BtcAddress.Value)
        if len(doms) >:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(b))
        else:
            TRX.addUIMessage(str(BtcAddress.Value) + " not found.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_reverseDomainsWithEmail(Email):
    TRX = MaltegoTransform()

    try:
        doms = domainsWithEmail(Email.Value)
        if len(doms) >:
            for d in doms:
                TRX.addEntity("maltego.Domain",str(b))
        else:
            TRX.addUIMessage(str(Email.Value) + " not found.",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred.",UIM_PARTIAL)

    return TRX.returnOutput()
