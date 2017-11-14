import MySQLdb, sys, os


############### INIT THE DB
db = MySQLdb.connect( "localhost", os.environ["dbUser"], os.environ["dbPass"], os.environ["dbName"] )
cursor = db.cursor()


createTable = """CREATE TABLE REPORTS (
                  DOMAIN CHAR(62) NOT NULL,
                  relatedONIONS LONGTEXT,
                  btcAddresses LONGTEXT,
                  emails LONGTEXT,
                  ftp CHAR,
                  ssh CHAR, telnet CHAR, smtp CHAR, tftp CHAR, http CHAR,
                  sftp CHAR, netbios-ne CHAR, netbios-dgram CHAR,
                  netbios-ssn CHAR, snmp CHAR, imap3 CHAR, https CHAR,
                  klogin CHAR, kshell CHAR, kerberos-adm CHAR, simap CHAR,
                  spop3 CHAR, mysql CHAR, postgres CHAR, irc CHAR,
                  trans-proxy CHAR, mongodb CHAR, ricohet CHAR, bitcoin CHAR,
                  vnc CHAR, xmpp CHAR, pgpKey LONGTEXT, ipAddresses LONGTEXT)
                  """

##### RUN THIS ONCE
# cursor.execute(createTable)

# some code here, from json to db

db.close()
