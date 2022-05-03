import socket
import json

m = {
   "request": "subscribe",
   "port": 8888,
   "name": "fun_name_for_the_client",
   "matricules": ["12345", "67890"]
}

data = json.dumps(m)
s = socket.socket()

s.connect(("localhost", 3000))
s.sendall(bytes(data,encoding="utf-8"))


received = s.recv(1024)
received = received.decode("utf-8")




print(received)