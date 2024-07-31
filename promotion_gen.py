import random
import string
import os
from colorama import init, Fore, Style

# Inicializa a colorama
init(autoreset=True)

# Função para gerar um código aleatório de 24 caracteres
def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

# Função para verificar se o código está na blacklist
def is_blacklisted(code, blacklist):
    return code in blacklist

# Função para carregar a blacklist a partir do arquivo
def load_blacklist(filename):
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

# Função para salvar a blacklist no arquivo
def save_blacklist(blacklist, filename):
    with open(filename, 'w') as file:
        for item in blacklist:
            file.write(f"{item}\n")

# Função principal para gerar links e salvar no arquivo
def generate_links(num_links, base_url, output_file, blacklist_file):
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

# Definindo as variáveis
base_url = "https://promos.discord.gg/"
output_file = "results/promotion_gen/links.txt"
blacklist_file = "results/promotion_gen/blacklist.txt"

def clear_screen():
    # Limpa a tela de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    import pyfiglet
    banner_text = pyfiglet.figlet_format("Royalty Tools", font="slant")
    print(Fore.MAGENTA + banner_text)

def promotion_generator_menu():
    clear_screen()
    print_banner()
    
    print(Fore.LIGHTBLACK_EX + "[!] Credits: Royalty Tools Team")
    print(Fore.GREEN + "[+] Select any option from the menu:\n")
    print(Fore.MAGENTA + "[1] 3 Months Discord Nitro")
    print(Fore.MAGENTA + "[2] 1 Month Discord Nitro")
    print(Fore.GREEN + "[3] Return to main menu")
    
    try:
        choice = int(input(Fore.GREEN + "[+] Enter your choice: "))
        
        if choice in [1, 2]:
            num_links = int(input("Quantos códigos deseja gerar? "))
            if num_links <= 0:
                raise ValueError("O número de códigos deve ser maior que zero.")
                
            if choice == 1:
                output_file = "results/promotion_gen/links_3months.txt"
            elif choice == 2:
                output_file = "results/promotion_gen/links_1month.txt"
                
            links = generate_links(num_links, base_url, output_file, blacklist_file)
            
            print("\nLinks gerados:")
            for link in links:
                print(Fore.GREEN + link)
        
        elif choice == 3:
            return  # Retorna ao menu principal
        
        else:
            print(Fore.RED + "Opção inválida.")
    
    except ValueError as e:
        print(Fore.RED + f"Entrada inválida: {e}")
    
    input(Fore.GREEN + "[+] Pressione Enter para continuar...")

# Executa o menu do gerador de promoções
while True:
    promotion_generator_menu()
    choice = input(Fore.GREEN + "[+] Deseja retornar ao menu principal? (s/n): ").strip().lower()
    if choice != 's':
        break
