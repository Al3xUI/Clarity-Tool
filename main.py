import os
import requests
from pystyle import Colors, Colorate


"""def update_checker():
    try:
        response = requests.get("https://api.github.com/repos/Al3xUI/clarity-tool/releases/latest")
        response.raise_for_status()
        data = response.json()
        latest_version = data.get("tag_name", "unknown")

        with open("version.txt", "r") as version_file:
            current_version = version_file.read().strip()

        if latest_version != current_version:
            print(f"Une nouvelle version de Clarity Tool est disponible : {latest_version}")
            choice = input("Voulez-vous mettre à jour maintenant ? (y/n) ").lower()

            if choice == "y":
                try:
                    os.system("git clone https://github.com/Al3xUI/clarity-tool.git")
                    if os.name == 'nt': os.system("cd clarity-tool && setup.bat && python main.py")
                    else: os.system("cd clarity-tool && chmod +x setup.sh && ./setup.sh && python3 main.py")
                except requests.RequestException: print("Échec de la vérification des mises à jour.")
            else: print("Mise à jour annulée.")
        else: print("Vous utilisez déjà la dernière version de Clarity Tool.")
    except FileNotFoundError: print("Fichier 'version.txt' introuvable.")"""


def display_menu():

    title = "Clarity Tool \ made by Alex \ v1.0"

    if os.name == 'nt':
        os.system(f"title {title}")
        os.system('cls')
    else:
        os.system(f'echo -n -e "\033]0;{title}\007"')
        os.system('clear')

    menu = """
                 ▄████▄   ██▓    ▄▄▄       ██▀███   ██▓▄▄▄█████▓▓██   ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
                ▒██▀ ▀█  ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
                ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
                ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
                ▒ ▓███▀ ░░██████▒▓█   ▓██▒░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
                ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
                  ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
                ░          ░ ░    ░   ▒     ░░   ░  ▒ ░  ░       ▒ ▒ ░░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                ░ ░          ░  ░     ░  ░   ░      ░            ░ ░                     ░ ░      ░ ░      ░  ░
                ░                                                ░ ░                                           

                                                    Made with <3 By Alex                        
                                                        version 0.0.1                 
                                                              ╦                     
                                                              ║                     
                                                              ║                     
                                   ╔══════════════════════════╩════════════════════════╗              
                                   ║                                                   ║                             
            ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗
            ║   [1] >                                       ║ ║   [10] >                                      ║
            ║   [2] >                                       ║ ║   [11] >                                      ║
            ║   [3] >                                       ║ ║   [12] >                                      ║
            ║   [4] >                                       ║ ║   [13] >                                      ║ 
            ║   [5] >                                       ║ ║   [14] >                                      ║
            ║   [6] >                                       ║ ║   [15] >                                      ║
            ║   [7] >                                       ║ ║   [16] >                                      ║ 
            ║   [8] >                                       ║ ║   [17] >                                      ║ 
            ║   [9] >                                       ║ ║   [18] >                                      ║          
            ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝ 
            
   tapez "exit" pour quitter
    """
    print(Colorate.Horizontal(Colors.blue_to_purple, menu))


def execute_script(choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    match choice:
        case 1: tool_info.exec()
        case _: print("Choix invalide.")
    main()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
#    update_checker()
    display_menu()

    try:
        choice = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'Entrez un nombre [>] ')))
        if choice == "exit": exit()
        else: execute_script(choice)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


if __name__ == "__main__":
    main()

# 🚪 <-- We commented the backdoor, see?
