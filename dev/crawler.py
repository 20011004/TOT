from BeautifulSoup import BeautifulSoup
import re, sys, time, requests, os, time, thread

#######################################
# torify python crawler.py

active_threads = 0


def addLink(links, linkToAdd, F):
    if not linkToAdd in links:
        links.append(str(linkToAdd))
        F.write(str(linkToAdd) + "\n")
    else:
        pass


def getEmails(page, E, EMAILs):
    print "[+]Searching emails..."
    ems = re.findall(r'[\w\.-]+@[\w\.-]+', page)
    for t in ems:
        if not t in EMAILs:
            E.write(t + '\n')
            EMAILs.append(t)
        else:
            pass


def getBTCS(page, B, BTCs):
    print "[+]Searching btcs..."
    btcs = re.findall(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', page)
    for b in btcs:
        if not b in BTCs:
            B.write(b + '\n')
            BTCs.append(b)
        else:
            pass


def getHS(page, H, HSes):
    print "[+]Searching HS..."
    hses = re.findall(r'[a-zA-Z0-9]{16}.onion', page)
    for hs in hses:
        if not hs in HSes:
            H.write(hs + '\n')
            HSes.append(hs)
        else:
            pass


header = {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
}


def Crawler(name, onions):
    global active_threads
    active_threads += 1
    for oni in onions:
        links = []
        Blinks = []
        ems = []
        btcss = []
        hses = []
        links.append(oni)
        r00tUrl = oni
        i = 0
        for url in links:
            if len(url.split("/")) < 8:
                if os.path.isdir("/home/user/Scrivania/reports/" + r00tUrl):
                    os.chdir("/home/user/Scrivania/reports/" + r00tUrl)
                else:
                    os.mkdir("/home/user/Scrivania/reports/" + r00tUrl)
                    os.chdir("/home/user/Scrivania/reports/" + r00tUrl)
                E = open("emails.txt", "a")
                B = open("btcs.txt", "a")
                H = open("HS.txt", "a")
                linksF = open("good.txt", "a")
                BlinksF = open("bad.txt", "a")
                if i == 0:  # scan the r00t once
    				i = 1
    				try:
    					response = requests.get("http://" + url, headers=header)
    					page = str(BeautifulSoup(response.content))
    					soup = BeautifulSoup(page)
    					for link in soup.findAll('a'):
    						time.sleep(0.1)
    						if not str(link.get('href')).startswith("http"):
    							if not str(link.get('href')).startswith("#"):
    								if str(link.get('href')).startswith("/"):
    									Link = url + str(link.get('href'))
    									getEmails(page, E, ems)
    									getBTCS(page, B, btcss)
    									getHS(page, H, hses)
    									addLink(links, Link, linksF)
    								elif str(link.get('href')) == "None":
    									pass
    								else:
    									Link = url + str(link.get('href'))[2:]
    									getEmails(page, E, ems)
    									getBTCS(page, B, btcss)
    									getHS(page, H, hses)
    									addLink(links, Link, linksF)
    							else:
    								pass
    						else:
    							addLink(links, str(link.get('href')), linksF)
    							getEmails(page, E, ems)
    							getBTCS(page, B, btcss)
    							getHS(page, H, hses)
    				except:
    					pass
                else:
                    if url == oni:
                        pass
                    else:
                        # if it's not the same site, skip
                        if not url.split("/")[0] == r00tUrl:
                            pass
                        else:
                            try:
                                response = requests.get("http://" + url, headers=header)
                                print "=====> good: " + url
                                page = str(BeautifulSoup(response.content))
                                soup = BeautifulSoup(page)
                                for link in soup.findAll('a'):
    	                            # time.sleep(0.1)
                                    if not str(link.get('href')).startswith("http"):
                                        if not str(link.get('href')).startswith("#"):
                                            if str(link.get('href')).startswith("/"):
                                                if str(link.get('href')) == "/":
                                                    pass
                                                else:
                                                    Link = r00tUrl + str(link.get('href'))
                                                    addLink(links, Link, linksF)
                                                    getEmails(page, E, ems)
                                                    getBTCS(page, B, btcss)
                                                    getHS(page, H, hses)
                                            elif str(link.get('href')) == "None":
                                                pass
                                            elif str(link.get('href')).startswith(".."):
                                                Link = r00tUrl + str(link.get('href'))[2:]
                                                addLink(links, Link, linksF)
                                                getEmails(page, E, ems)
                                                getBTCS(page, B, btcss)
                                                getHS(page, H, hses)
                                            else:
    											if str(link.get('href')) == "javascript:;":
    												pass
    											else:
    												Link = r00tUrl + str(link.get('href'))
    												addLink(links, Link, linksF)
    												getEmails(page, E, ems)
    												getBTCS(page, B, btcss)
    												getHS(page, H, hses)
                                        else:
    										pass
                                    else:
    									addLink(links, str(link.get('href')), linksF)
    									getEmails(page, E, ems)
    									getBTCS(page, B, btcss)
    									getHS(page, H, hses)
    									addLink(Blinks, url, BlinksF)
                            except:
    							pass

            else:
                pass
            linksF.close()
            BlinksF.close()
            print "Scanned: " + url + " % time: " + time.ctime()
            H.close()
            E.close()
            B.close()
    active_threads -= 1
    return

f = open("/home/user/Scrivania/reports/pielco11.ovh/HS.txt" , "r")
onions = []
for l in f.readlines():
    onions.append(l.strip("\n"))

index = 0
done = False
while True:
    if (active_threads<=15) and not done:
        if (len(onions) - index)>=50:
            thread.start_new_thread(Crawler, ("thread", onions[index:index+50]))
            print "Thread started"
            index += 50
        else:
            thread.start_new_thread(Crawler, ("thread", onions[index:]))
            print "Thread started"
            done = True
    elif (active_threads==0) and done:
        break
        print "Scan completed"
    time.sleep(15)
