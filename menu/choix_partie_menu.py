import pygame
import sys
import socket
import constants as const
from bouton import Bouton
from menu.choix_personnage_menu import choix_personnage_menu
import tkinter as tk

def choix_nombre_joueurs(screen, stats):
    width = screen.get_width()
    height = screen.get_height()

    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 105)
    text_font = pygame.font.SysFont("Helvetic", 50)

    taille_bordure = 2

    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0,0))

        title_bord = title_font.render("La Cité Academique", True, (255, 255, 255))
        title = title_font.render("La Cité Academique", True, (239, 114, 52)) # (10, 170, 225)

        title_bord_rect = title_bord.get_rect(center=(const.WIDTH//2, 100))
        title_rect = title.get_rect(center=(const.WIDTH//2, 100))
        
        for x_offset in range(-taille_bordure, taille_bordure + 1):
            for y_offset in range(-taille_bordure, taille_bordure + 1):
                screen.blit(title_bord, (title_bord_rect.x + x_offset, title_bord_rect.y + y_offset))
        
        screen.blit(title, title_rect)

        choix_2_joueurs = Bouton(menu_button, (width*0.5, 250), "2 JOUEURS", text_font, "black", "White")
        choix_3_joueurs = Bouton(menu_button, (width*0.5, 400), "3 JOUEURS", text_font, "black", "White")
        choix_4_joueurs = Bouton(menu_button, (width*0.5, 550), "4 JOUEURS", text_font, "black", "White")
        for button in [choix_2_joueurs, choix_3_joueurs, choix_4_joueurs]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if choix_2_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 2, stats)
                    run = False

                if choix_3_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 3, stats)
                    run = False

                if choix_4_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 4, stats)
                    run = False

        pygame.display.update()

def on_multijoueur_click():
    ip = '127.0.0.1'
    port = 12345
    multit(ip, port)

def multit(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Tentative de connexion au serveur
            s.connect((ip, port))
            print("Connexion réussie au serveur sur", ip, ":", port)
            # Envoi d'un signal au serveur pour indiquer que le client est prêt à jouer
            s.sendall(b"ready_to_play")
    except socket.error as e:
        print("Impossible de se connecter au serveur:", e)

    # Lancer le client de chat dans une fenêtre séparée
    root = tk.Tk()
    chat_client = ChatClient(root)
    root.mainloop()

import socket
import tkinter as tk
import threading

class ChatClient:
    def __init__(self, master, ip, port):
        self.master = master
        self.master.title("Jeu Multijoueur")
        self.ip = ip
        self.port = port
        
        # Création du champ de saisie
        self.entry = tk.Entry(master)
        self.entry.pack(fill=tk.X, padx=5, pady=5)
        self.entry.bind("<Return>", self.send_message)
        
        # Création de la zone de texte
        self.text_area = tk.Text(master)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialisation du socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.socket.connect((self.ip, self.port))
            print("Connexion réussie au serveur sur", self.ip, ":", self.port)
            # Envoi d'un signal au serveur pour indiquer que le client est prêt à jouer
            self.socket.sendall(b"ready_to_play")
            # Démarrer le thread pour recevoir les messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except socket.error as e:
            print("Impossible de se connecter au serveur:", e)

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            try:
                self.socket.sendall(message.encode())
                self.entry.delete(0, tk.END)
                # Ajouter le message envoyé à la zone de texte
                self.text_area.insert(tk.END, f"Vous: {message}\n")
                self.text_area.see(tk.END)  # Faire défiler vers le bas pour afficher le nouveau message
            except socket.error as e:
                print("Erreur lors de l'envoi du message:", e)

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if data:
                    # Ajouter le message reçu à la zone de texte
                    self.text_area.insert(tk.END, f"Adversaire: {data.decode()}\n")
                    self.text_area.see(tk.END)  # Faire défiler vers le bas pour afficher le nouveau message
            except socket.error as e:
                print("Erreur lors de la réception du message:", e)

def on_multijoueur_click():
    ip = '127.0.0.1'
    port = 12345
    root = tk.Tk()
    chat_client = ChatClient(root, ip, port)
    root.mainloop()


def choix_partie_menu(screen, stats):
    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 105)
    text_font = pygame.font.SysFont("Helvetic", 50)

    taille_bordure = 2

    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        title_bord = title_font.render("La Cité Academique", True, (255, 255, 255))
        title = title_font.render("La Cité Academique", True, (239, 114, 52)) # (10, 170, 225)

        title_bord_rect = title_bord.get_rect(center=(const.WIDTH//2, 100))
        title_rect = title.get_rect(center=(const.WIDTH//2, 100))
        
        for x_offset in range(-taille_bordure, taille_bordure + 1):
            for y_offset in range(-taille_bordure, taille_bordure + 1):
                screen.blit(title_bord, (title_bord_rect.x + x_offset, title_bord_rect.y + y_offset))
        
        screen.blit(title, title_rect)

        solo_button = Bouton(menu_button, (640, 250), "SOLO", text_font, "black", "White")
        multi_button = Bouton(menu_button, (640, 400), "MULTIJOUEUR", text_font, "black", "White")
        back_button = Bouton(menu_button, (640, 550), "RETOUR", text_font, "black", "White")
        for button in [solo_button, multi_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_button.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 1, stats)
                    run = False

                if multi_button.checkForInput(mouse_pos):
                    # on_multijoueur_click()
                    # ChatClient()
                    choix_nombre_joueurs(screen, stats)
                    run = False

                if back_button.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    stats = None
    choix_partie_menu(screen, stats)
