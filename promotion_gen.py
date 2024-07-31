import random
import string
import os
from colorama import init, Fore, Style
import pyfiglet

# Inicializa a colorama
init(autoreset=True)

def clear_screen():
    # Limpa a tela de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_code():
    # Gera um código aleatório de 24 caracteres
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

def is_blacklisted(code, blacklist):
    # Verifica se o código está na blacklist
    return code in blacklist

def load_blacklist(filename):
    # Carrega a blacklist a partir do arquivo
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

def save_blacklist(blacklist, filename):
    # Salva a blacklist no arquivo
    with open(filename, 'w') as file:
        for item in blacklist:
            file.write(f"{item}\n")

def generate_links(num_links, base_url, output_file, blacklist_file):
    # Gera links e salva no arquivo
    blacklist = load_blacklist(blacklist_file)
    generated_links = []

    while len(generated_links) < num_links:
        code = generate_code()
        if not is_blacklisted(code, blacklist):
            link = f"{base_url}{code}"
            generated_links.append(link)
            blacklist.add(code)
    
    with open(output_file, 'w') as file:
        for link in generated_links:
            file.write(f"{link}\n")
    
    save_blacklist(blacklist, blacklist_file)
    return generated_links

def promotion_generator_menu():
    # Função do menu do gerador de promoções
    clear_screen()
    
    # Exibindo o texto em roxo usando pyfiglet
    banner_text = pyfiglet.figlet_format("Royalty Tools", font="slant")
    print(Fore.MAGENTA + banner_text)
    print(Fore.YELLOW + "[!] Credits: Royalty Tools Team")
    print(Fore.GREEN + "[+] Select any option from the menu:\n")
    
    # Menu de opções
    print(Fore.MAGENTA + "[1] 3 Months Discord Nitro")
    print(Fore.MAGENTA + "[2] 1 Month Discord Nitro")

    # Exibir o prompt com [+] verde
    print(Fore.GREEN + "[+] Enter your choice: " + Fore.RESET, end='')
    
    choice = input().strip()
    
    if choice == "1":
        num_links = 3
        base_url = "https://discord.com/billing/promotions/"
    elif choice == "2":
        num_links = 1
        base_url = "https://discord.com/billing/promotions/"
    else:
        print(Fore.RED + "Invalid choice. Exiting.")
        return
    
    # Definindo os arquivos de saída e blacklist
    output_file = "results/promotion_gen/links.txt"
    blacklist_file = "results/promotion_gen/blacklist.txt"

    # Gera os links
    links = generate_links(num_links, base_url, output_file, blacklist_file)

    # Exibindo os links no terminal
    print("\nLinks gerados:")
    for link in links:
        print(Fore.GREEN + link)

    # Perguntar ao usuário se deseja gerar mais links
    choice = input("\nDeseja gerar mais códigos? (s/n): ").strip().lower()
    if choice == 's':
        promotion_generator_menu()

if __name__ == "__main__":
    promotion_generator_menu()
