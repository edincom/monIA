import socket
import json
s = socket.socket()
message = {
   "request": "subscribe",
   "port": 8888,
   "name": "fun_name_for_the_client",
   "matricules": ["12345", "67890"]
}
jsonStr = json.dumps(message)
s.connect(("localhost", 3000))
s.sendall(bytes(message,encoding="utf-8"))
print(s.recv(2048))

