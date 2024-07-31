import os
import pyfiglet
import requests
from colorama import Fore, Style
import time

def clear():
    os.system("clear||cls")

class colors:
    @staticmethod
    def banner(txt):
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{txt}{Fore.RESET}{Style.NORMAL}")

    @staticmethod
    def credits(txt):
        print(f"{Fore.YELLOW}[!]{Fore.RESET}{Style.DIM} {txt}{Fore.RESET}{Style.NORMAL}")

    @staticmethod
    def menu_option(txt):
        print(f"{Fore.GREEN}[+]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

    @staticmethod
    def error(txt):
        print(f"{Fore.RED}[-]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

    @staticmethod
    def success(txt):
        print(f"{Fore.GREEN}[+]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

def cape_generator_menu():
    clear()

    # Tela inicial com título em roxo usando pyfiglet
    banner_text = pyfiglet.figlet_format("Royalty Tools", font="slant")
    colors.banner(banner_text)

    # Créditos
    colors.credits("Credits: Royalty Tools Team")

    # Menu de opções
    colors.menu_option("Select any option from the menu:\n")
    print(f"{Fore.LIGHTMAGENTA_EX}1- Generate Capes\n2- Return to main menu{Fore.RESET}\n")

    # Opção do usuário
    colors.menu_option("Enter your choice: ")
    choice = input().strip()

    if choice == "1":
        generate_capes()
    elif choice == "2":
        main_menu()  # Retorna ao menu principal
    else:
        colors.error("Invalid option. Exiting.")
        sys.exit()

def generate_capes():
    cape_gen_script_url = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/generate_capes.py"  # Substitua com a URL correta
    login_file_url = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/userpass.txt"  # Substitua com a URL correta

    # Criar diretório para resultados se não existir
    if not os.path.exists("results/capes"):
        os.makedirs("results/capes")

    # Baixar e executar o script de geração de capas
    response = requests.get(cape_gen_script_url)
    if response.status_code == 200:
        exec(response.text)
        colors.success("Cape generation script executed successfully.")
    else:
        colors.error(f"Failed to load cape generation script. Status code: {response.status_code}")

    # Gerar capes
    try:
        response = requests.get(login_file_url)
        response.raise_for_status()
        logins = response.text.splitlines()

        for login in logins:
            # A função de geração de capa deve ser implementada no script que você irá baixar
            # Assumindo que a função seja `generate_cape(login)`
            generate_cape(login)
            time.sleep(30)  # Cooldown de 30 segundos entre cada geração

            # Checar se já gerou 20 capas
            if count_generated_capes() >= 20:
                colors.error("Limite de 20 capas geradas em um dia alcançado. Programa será encerrado.")
                break
    except requests.RequestException as e:
        colors.error(f"Erro ao acessar o arquivo de logins: {e}")

def generate_cape(login):
    # Implementar a função para gerar capa com base no login
    pass

def count_generated_capes():
    # Contar o número de capas geradas no dia
    return len([f for f in os.listdir("results/capes") if os.path.isfile(os.path.join("results/capes", f))])

if __name__ == "__main__":
    cape_generator_menu()
