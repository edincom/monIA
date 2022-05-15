Matricule : 195357 et 20038

Le projet a pour but de réaliser une intelligence artificielle pour le jeu Othello afin de donner le meilleur résultat possible.Celui-ci devra interagir avec le serveur et devra envoyer et répondre à certaines requêtes afin de jouer sur celui-ci.

Stratégie utilisée:
La stratégie utilisée se base sur trois fonctions. PossibleMoves calcule et renvoie la liste des mouvements possibles à effectuer. Une fonction caclulera le meilleur coup possible qui correspond au nombre max de pions à éliminer. On prend le mouvement correspondant avec la fonction BestMove.On envoie au serveur la réponse de notre meilleur mouvement avec la fonction ComputerMove.

Procédure:

Lancer la commande suivante à partir du réperatoire PI2CChampionshipRunner: python server.py othello
Vous avez maintenant lancé le serveur.

Pour connecter le client:
Lancer la commande:  python monIa.py.
Vous êtes maintenant connectés au serveur et prêt à jouer.

import socket: Pour effectuer les communications avec le serveur
import json : Format du message envoyé au serveur
import threading: Lancer le processus de communication 
