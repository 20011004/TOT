import json, subprocess, os

from Maltego import *

pathToReports = "/reports/"

def trx_onionDate(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            TRX.addEntity("maltego.Phrase",str(data["dateScanned"]))
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

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
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionPGPKeys(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            TRX.addUIMessage("PGP keys found",UIM_PARTIAL) # to change
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionIpAddress(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            if str(data["identifierReport"]["ipAddresses"]) == "None":
                TRX.addUIMessage("IP not found",UIM_PARTIAL)
            else:
                TRX.addEntity("maltego.IPv4Address",str(data["identifierReport"]["ipAddresses"]))
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionEmail(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            try:
                for i in data["identifierReport"]["emailAddresses"]:
                    TRX.addEntity("maltego.EmailAddress",str(i))
            except:
                pass
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionBitcoin(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            try:
                for i in data["identifierReport"]["bitcoinAddresses"]:
                    TRX.addEntity("maltego.BtcAddress",str(i))
            except:
                pass
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedServices(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            try:
                for i in data["identifierReport"]["relatedOnionServices"]:
                    TRX.addEntity("maltego.Domain",str(i))
            except:
                pass
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()

def trx_onionRelatedDomains(Domain):
    TRX = MaltegoTransform()

    try:
        if os.path.isfile(pathToReports + Domain.Value + ".scan"):
            data = json.loads(open(pathToReports + Domain.Value + ".scan", "r").read())
            try:
                for i in data["identifierReport"]["relatedOnionDomains"]:
                    TRX.addEntity("maltego.Domain",str(i))
            except:
                pass
        else:
            TRX.addUIMessage("Error: " + str(Domain.Value) + " not scanned!",UIM_PARTIAL)
    except:
        TRX.addUIMessage("Some error occurred",UIM_PARTIAL)

    return TRX.returnOutput()
