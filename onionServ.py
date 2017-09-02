import socket, time
import setVar

print "="*30
print "[+] Starting onionServ at " + setVar.host + ":" + str(setVar.port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((setVar.host, setVar.port))
sock.listen(1)

print "[+] Server started..."

while True:
	"[+] Waiting for connection"
	cli = sock.accept()
	req = cli[0].recv(55)
	key = req.split(",")[0]
	host = req.split(",")[1]
	print "[-] New connection from " + str(cli[1])
	print "[>] Key " + key
	print "[>] Domain " + host

	if key == setVar.key:
		print "[+] Key accepted"
		data = open(host+".scan", "r")
		size = 0
		buf = data.read(256)
		size += len(buf)
		while buf != "":
			cli[0].send(buf)
			buf = data.read(256)
			size += len(buf)
		cli[0].send("END")
		print "[<] Sent " + str(size) + " B"
		print "="*30
		time.sleep(0.1)
		cli[0].close()
	else:
		print "[!] Key not accepted, closing..."
		print "="*30
		cli[0].sendall("Error.")
		time.sleep(0.1)
		cli[0].close()
