from BeautifulSoup import BeautifulSoup
import re, sys, time, requests, os, time, thread

#######################################
# torify python log2.py kek.onion

reports = "/somewhere/over/the/rainbow/"
onii = "/another/place/onii.txt"

def addLink(links, linkToAdd, F):
    if not linkToAdd in links:
        links.append(str(linkToAdd))
        F.write(str(linkToAdd) + "\n")
    else:
        pass


def getEmails(page):
    ems = re.findall(r'[\w\.-]+@[\w\.-]+', page)
    for t in ems:
        f.write(t + '\n')


def getBTCS(page):
    btcs = re.findall(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', page)
    for b in btcs:
        B.write(b + '\n')


def getHS(page):
    hses = re.findall(r'[a-zA-Z0-9]{16}.onion', page)
    for hs in hses:
        H.write(hs + '\n')


header = {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
}


def Crawler(name, onions):
    for oni in onions:
        time.sleep(3)
        links = []
        Blinks = []
        links.append(oni)
        r00tUrl = oni
        i = 0
        for url in links:
            if len(url.split("/")) < 8:
                if os.path.isdir(reports + r00tUrl):
                    os.chdir(reports + r00tUrl)
                else:
                    os.mkdir(reports + r00tUrl)
                    os.chdir(reports + r00tUrl)
                f = open("emails.txt", "a")
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
    									getEmails(page)
    									getBTCS(page)
    									getHS(page)
    									addLink(links, Link, linksF)
    								elif str(link.get('href')) == "None":
    									pass
    								else:
    									Link = url + str(link.get('href'))[2:]
    									getEmails(page)
    									getBTCS(page)
    									getHS(page)
    									addLink(links, Link, linksF)
    							else:
    								pass
    						else:
    							addLink(links, str(link.get('href')), linksF)
    							getEmails(page)
    							getBTCS(page)
    							getHS(page)
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
                                                    getEmails(page)
                                                    getBTCS(page)
                                                    getHS(page)
                                            elif str(link.get('href')) == "None":
                                                pass
                                            elif str(link.get('href')).startswith(".."):
                                                Link = r00tUrl + str(link.get('href'))[2:]
                                                addLink(links, Link, linksF)
                                                getEmails(page)
                                                getBTCS(page)
                                                getHS(page)
                                            else:
    											if str(link.get('href')) == "javascript:;":
    												pass
    											else:
    												Link = r00tUrl + str(link.get('href'))
    												addLink(links, Link, linksF)
    												getEmails(page)
    												getBTCS(page)
    												getHS(page)
                                        else:
    										pass
                                    else:
    									addLink(links, str(link.get('href')), linksF)
    									getEmails(page)
    									getBTCS(page)
    									getHS(page)
    									addLink(Blinks, url, BlinksF)
                            except:
    							pass

            else:
                pass
            linksF.close()
            BlinksF.close()
            print "Scanned: " + url + " % time: " + time.ctime()
            H.close()
            f.close()
            B.close()

f = open(onii , "r")
#onions = ["3g2upl4pq6kufc4m.onion"]
onions = []
for l in f.readlines():
    onions.append(l.strip("\n"))

for i in range(0, len(onions)):
    thread.start_new_thread(Crawler, ("thread" ,onions[i:i+1000]))
    time.sleep(10)
    i+=1000
