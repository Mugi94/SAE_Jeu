import socket
import threading

lock = threading.Lock()

def client_thread(conn, addr, clients, start_event, ready_players, max_connections):
    print(f"Connexion établie avec {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Message reçu de {addr}: {data.decode()}")

            # Si le message reçu est "ready_to_play", signaler au serveur que le joueur est prêt
            if data.decode() == "ready_to_play":
                with lock:
                    ready_players.append(addr)
                    if len(ready_players) == max_connections:
                        start_event.set()
            # Si le message commence par '/quit', déconnecter le client
            elif data.decode() == "/quit":
                print(f"{addr} a quitté le chat.")
                break
            # Envoyer le message aux autres clients
            else:
                message = data.decode()
                with lock:
                    for client_conn in clients:
                        if client_conn != conn:
                            client_conn.sendall(f"{addr}: {message}".encode())
        except ConnectionResetError:
            pass  
        except OSError as e:
            if e.errno == 10053:
                print(f"Connexion avec {addr} fermée par l'hôte.")
            else:
                print(f"Erreur lors de la communication avec {addr}: {e}")
            break

    # Si le jeu n'a pas encore commencé, ne pas supprimer la connexion fermée de la liste des clients
    if not start_event.is_set():
        return

def main():
    host = '127.0.0.1'
    port = 12345
    clients = []
    ready_players = []
    start_event = threading.Event()

    max_connections = int(input("Combien d'hôtes autorisez-vous ? "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Serveur en écoute sur {host}:{port}")

    while True:
        conn, addr = server.accept()

        with lock:
            clients.append(conn)
            print(f"Nouvelle connexion de {addr}. Nombre de personnes connectées : {len(clients)}")

        thread = threading.Thread(target=client_thread, args=(conn, addr, clients, start_event, ready_players, max_connections))
        thread.start()

        if len(clients) == max_connections:
            # Attendre que tous les joueurs soient prêts à jouer
            start_event.wait()
            # Une fois que tous les joueurs sont prêts, envoyer le signal à chacun
            for client_conn in clients:
                client_conn.sendall(b"start_game")
            print("Les joueurs sont prêts !")

if __name__ == "__main__":
    main()
