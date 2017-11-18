CREATE DATABASE thtdb

CREATE TABLE domain(
id VARCHAR(30) NOT NULL,
adder VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE find(
domain1 VARCHAR(30) NOT NULL,
domain2 VARCHAR(30) NOT NULL,
PRIMARY KEY (domain1, domain2),
FOREIGN KEY (domain1) REFERENCES domain(id),
FOREIGN KEY (domain2) REFERENCES domain(id)
);

CREATE TABLE port(
num INT NOT NULL,
service_name VARCHAR(20) NOT NULL,
PRIMARY KEY (num),
UNIQUE (service_name)
);

CREATE TABLE have(
domain VARCHAR(30) NOT NULL,
port INT NOT NULL,
state ENUM('open', 'filtered', 'closed') NOT NULL,
banner VARCHAR(40),
PRIMARY KEY (domain, port),
FOREIGN KEY (domain) REFERENCES domain(id),
FOREIGN KEY (port) REFERENCES port(number)
);

CREATE TABLE btcaddress(
id VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE contains_btc(
domain VARCHAR(30) NOT NULL,
btcaddress VARCHAR(50) NOT NULL,
PRIMARY KEY (domain, btcaddress),
FOREIGN KEY (domain) REFERENCES domain(id),
FOREIGN KEY (btcaddress) REFERENCES btcaddress(id)
);

CREATE TABLE email(
address VARCHAR(40) NOT NULL,
PRIMARY KEY (address)
);

CREATE TABLE contains_mail(
domain VARCHAR(30) NOT NULL,
email VARCHAR(40) NOT NULL,
PRIMARY KEY (domain, email),
FOREIGN KEY (domain) REFERENCES domain(id),
FOREIGN KEY (email) REFERENCES email(address)
