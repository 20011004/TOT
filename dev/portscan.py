 #!/usr/bin/python
import socket, socks, json, urllib2, sys, os, time, thread

from scapy.all import *


############## define vars
# RUN WITH PROXYCHAINS
#inFile = sys.argv[1]

reports = "/somewhere/over/the/rainbow/"
onii = "/another/place/onii.txt"
checkitList = ""

ports = [21, 22, 23, 25, 69, 80, 115, 137, 138, 139, 161, 220, 443,
        543, 544, 749, 993, 995, 3306, 5432, 6667, 8081, 27017, 9878, 8333,
        5900, 5222]

servs = ["ftp", "ssh", "telnet", "smtp", "tftp", "http", "sftp", "netbios-ne",
        "netbios-dgram", "netbios-ssn", "snmp", "imap3", "https", "klogin", "kshell",
        "kerberos-adm", "simap", "spop3", "mysql", "postgres", "irc", "trans-proxy", "mongodb",
        "ricochet", "bitcoin", "vnc", "xmpp"]


############## functions for detecting here
def onionScapyStealth(Domain, Port):
    src_port = RandShort()
    stealth_scan_resp = sr1(IP(dst=Domain)/TCP(sport=src_port,dport=Port,flags="S"),timeout=10)
    if(str(type(stealth_scan_resp))=="<type 'NoneType'>"):
        return "Filtered"
    elif(stealth_scan_resp.haslayer(TCP)):
        if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=Domain)/TCP(sport=src_port,dport=Port,flags="R"),timeout=10)
            return "Open"
        elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
            return "Closed"
    elif(stealth_scan_resp.haslayer(ICMP)):
        if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            return "Filtered"

############## functions for infos here

def onionInfoHTTP(Domain, ssl):
    try:
        return dict(urllib2.urlopen("http://" + Domain).info())["server"]
    except:
        return "error"

def onionInfoGeneral(Domain, Port):
    try:
        sock = socket.socket()
        sock.connect((Domain,Port))
        banner = sock.recv(1024)
        if len(banner.split(" ")) > 1:
            return banner.split(" ")[0] + ":" + banner.split(" ")[1][:-1]
        else:
            return banner[:-1]
    except:
        return "none"

################ stop functions, let's play
################ take a coffee, maybe two

def ScanTot(name, onions):
    for oni in onions:
        time.sleep(3)
        report = {}
        scanReport = []
        Domain = oni
        if Domain in checkitList:
            pass
        else:
            for port in ports:
                time.sleep(1)
                try:
                    stat = onionScapyStealth(Domain, port)
                    banner = servs[ports.index(port)]
                    if stat == "Closed":
                        pass
                    else:
                        if str(port) == "80" and stat == "Open":
                            banner = onionInfoHTTP(Domain, False)
                        elif str(port) == "443" and stat == "Open":
                            banner = onionInfoHTTP(Domain, True)
                        elif str(port) == "22" and stat == "Open":
                            banneR = onionInfoGeneral(Domain, port)
                            if len(banneR.split(":")) > 1:
                                scanReport.append({"os": banneR.split(":")[1]})
                                banner = banneR.split(":")[0]
                            else:
                                banner = banneR.split(":")[0]
                        scanReport.append({"banner": banner, "status": stat, "port": port})
                except:
                    scanReport.append({"banner": "none", "status": "error", "port": port})

            report = json.dumps(scanReport)
            if os.path.isdir(reports + Domain):
                os.chdir(reports + Domain)
            else:
                os.mkdir(reports + Domain)
                os.chdir(reports + Domain)

            f = open(Domain + ".port", "w")
            f.write(report)
            f.close()

            print "Scanned: " + Domain + " % time: " + time.ctime()


f = open(onii , "r")
onions = []
for l in f.readlines():
    onions.append(l.strip("\n"))

for u in range(0, len(onions)):
    doms = onions[u:u+500]
    for i in range(0, len(doms)):
        thread.start_new_thread(ScanTot, ("thread" ,onions[i:i+50]))
        i+=50
    time.sleep(60*60*3)
    u += 500