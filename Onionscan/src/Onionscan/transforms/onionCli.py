import socket, setVar


class onionRequest():
	def __init__(self):
		self.sock = socket.socket()
		self.sock.connect((setVar.host, setVar.port))
		self.key = setVar.key

	def do_get(self, url):
		self.sock.sendall(self.key+","+url)
		buf = self.sock.recv(256)
		data = ""; data += buf
		while True:
			buf = self.sock.recv(256)
			data += buf
			if buf.endswith("END"):
				break
			else:
				pass
		data = data[:-3]
		return data

