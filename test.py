from http import client
import socket
import json
import threading


#Règle du jeu
directions = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    (-1,  1),
    ( 1, -1),
    (-1, -1)
]

def coord(index):
    return index // 8, index % 8

def add(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return l1 + l2, c1 + c2

def index(coord):
    l, c = coord
    return l*8+c

def isInside(coord):
    l, c = coord
    return 0 <= l < 8 and 0 <= c < 8

def walk(start, direction):
    current = start
    while isInside(current):
        current = add(current, direction)
        yield current
class GameEnd(Exception):
	def __init__(self, lastState):
		self.__state = lastState

	@property
	def state(self):
		return self.__state

	def __str__(self):
		return 'Game Over'

class GameWin(GameEnd):
	def __init__(self, winner, lastState):
		super().__init__(lastState)
		self.__winner = winner

	@property
	def winner(self):
		return self.__winner

	def __str__(self):
		return super().__str__() + ': {} win the game'.format(self.winner)

class BadMove(Exception):
	pass

class GameDraw(GameEnd):
	def __init__(self, lastState):
		super().__init__(lastState)

	def __str__(self):
		return super().__str__() + ': Draw'

class GameLoop(GameDraw):
	def __init__(self, lastState):
		super().__init__(lastState)

	def __str__(self):
		return super().__str__() + ': Stopped because of lopping behavior'

class BadGameInit(Exception):
	pass



def willBeTaken(state, move):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    if not (0 <= move < 64):
        raise BadMove('Your must be between 0 inclusive and 64 exclusive')

    if move in state['board'][0] + state['board'][1]:
        raise BadMove('This case is not free')

    board = []
    for i in range(2):
        board.append(set((coord(index) for index in state['board'][i])))

    move = coord(move)

    cases = set()
    for direction in directions:
        mayBe = set()
        for case in walk(move, direction):
            if case in board[otherIndex]:
                mayBe.add(case)
            elif case in board[playerIndex]:
                cases |= mayBe
                break
            else:
                break

    if len(cases) == 0:
        raise BadMove('Your move must take opponent\'s pieces')
    
    return [index(case) for case in cases]

def possibleMoves(state):
    res = []
    for move in range(64):
        try:
            willBeTaken(state, move)
            res.append(move)
        except BadMove:
            pass
    return res

def random(player, board):
   return random.choice(possibleMoves(player, board))

#Envoie de la requête et réception de la réponse du serveur
a = input("Nom de l'utilisateur : ")
b = int(input("Numéro de port : "))
e = str(input("Matricule 1 : "))
f = str(input("Matricule 2 : "))
m = {
   "request": "subscribe",
   "port": b,
   "name": a,
   "matricules": [e, f]
}

data = json.dumps(m)
s = socket.socket()
s.connect(("localhost", 3000))


s.sendall(bytes(data,encoding="utf-8"))

received = s.recv(1024)
received = received.decode("utf-8")
print(received)
s.close()

#Première connection établie, établissement de l'échange de messages entre client et serveur

s = socket.socket()
print("Socket succesfully created")
s.bind(("0.0.0.0", b))


a = str()
nbdevie = int()
list_of_errors = []
state_of_the_game = []

the_move_played = int

def clienttoserver():
   while True:
      s.listen() 
      client, address = s.accept()
      try:
        request = json.loads(client.recv(2048).decode("utf-8"))
        print("Requête reçue : ")
        if request["request"] == 'ping':                     #Requête Ping du serveur
            print("Ping reçu")
            pong = {'response': 'pong'}
            data2 = json.dumps(pong)
            client.send(bytes(data2,encoding="utf-8"))        #Réponse Pong envoyée
            print("Pong envoyé")
        elif request["request"] == "play":                   #Requête de coup du serveur
            print("Requête de coup de la part du serveur")
            c = request["state"]
            possiblemove = possibleMoves(c)
            the_move_played = random.choices(possiblemove)
            moncoup = {"response": "move", "move": the_move_played, "message": "Fun message"}
            data3 = json.dumps(moncoup)
            client.send(bytes(data3, encoding="utf-8"))       #Réponse du coup envoyé
            print("Coup envoyé")
        elif len(request) == 0:
            s.close()
        else:
            print("a")
            print(request)
      except:
          pass             

receive_thread = threading.Thread(target = clienttoserver)
receive_thread.start()