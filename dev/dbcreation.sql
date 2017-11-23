CREATE DATABASE totdb;

USE totdb;

CREATE TABLE domain(
id VARCHAR(120) NOT NULL,
adder VARCHAR(30) NOT NULL,
analyzed TINYINT(1) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE find(
domain1 VARCHAR(120) NOT NULL,
domain2 VARCHAR(120) NOT NULL,
PRIMARY KEY (domain1, domain2),
FOREIGN KEY (domain1) REFERENCES domain(id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (domain2) REFERENCES domain(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE port(
num INT NOT NULL,
service_name VARCHAR(20) NOT NULL,
PRIMARY KEY (num),
UNIQUE (service_name)
);

CREATE TABLE have(
domain VARCHAR(120) NOT NULL,
port INT NOT NULL,
status ENUM('open', 'filtered', 'closed', 'error') NOT NULL,
banner VARCHAR(80),
PRIMARY KEY (domain, port),
FOREIGN KEY (domain) REFERENCES domain(id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (port) REFERENCES port(num) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE btcaddress(
id VARCHAR(40) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE contains_btc(
domain VARCHAR(120) NOT NULL,
btcaddress VARCHAR(40) NOT NULL,
PRIMARY KEY (domain, btcaddress),
FOREIGN KEY (domain) REFERENCES domain(id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (btcaddress) REFERENCES btcaddress(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE email(
address VARCHAR(100) NOT NULL,
PRIMARY KEY (address)
);

CREATE TABLE contains_mail(
domain VARCHAR(120) NOT NULL,
email VARCHAR(100) NOT NULL,
PRIMARY KEY (domain, email),
FOREIGN KEY (domain) REFERENCES domain(id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (email) REFERENCES email(address) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO port (num, service_name) VALUES
(21, 'ftp'),
(22, 'ssh'),
(23, 'telnet'),
(25, 'smtp'),
(69, 'tftp'),
(80, 'http'),
(115, 'sftp'),
(137, 'netbios-ne'),
(138, 'netbios-dgram'),
(139, 'netbios-ssn'),
(161, 'snmp'),
(220, 'imap3'),
(443, 'https'),
(543, 'klogin'),
(544, 'kshell'),
(749, 'kerberos-adm'),
(993, 'simap'),
(995, 'spop3'),
(3306, 'mysql'),
(5432, 'postgres'),
(6667, 'irc'),
(8081, 'trans-proxy'),
(27017, 'mongodb'),
(9878, 'ricochet'),
(8333, 'bitcoin'),
(5900, 'vnc'),
(5222, 'xmpp');
