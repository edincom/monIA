from http import client
import socket
import json
import threading

#Envoie de la requête et réception de la réponse du serveur
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
s.close()

#Première connection établie, établissement de l'échange message ping pong

s = socket.socket()
print("Socket succesfully created")
s.bind(("0.0.0.0", 8888))
s.listen()
print("Socket is listening")

client, address = s.accept()

def client_receive():
   while True:
      try:
         request = json.loads(client.recv(2048).decode())
         if request == {'request': 'ping'}:                   #Request ping reçue
            pong = {'response': 'pong'}
            data2 = json.dumps(pong)
            client.send(bytes(data2,encoding="utf-8"))        #Réponse Pong envoyéé   
            print("Pong envoyé")
         else:
            print(request)

      except:
         pass

receive_thread = threading.Thread(target = client_receive)
receive_thread.start()