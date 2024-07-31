import os
import sys
import pyfiglet
import requests
import time
from colorama import Fore, Style

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
        print(f"{Fore.RED}[!]{Fore.RESET}{Style.DIM} {txt}{Fore.RESET}{Style.NORMAL}")

    @staticmethod
    def success(txt):
        print(f"{Fore.GREEN}[+]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

def cape_generator_menu():
    clear()
    banner_text = pyfiglet.figlet_format("Royalty Tools", font="slant")
    colors.banner(banner_text)
    
    colors.credits("Credits: Royalty Tools Team")
    colors.menu_option("Select any option from the menu:\n")
    print(f"{Fore.MAGENTA}[1]{Fore.RESET} Generate Capes")
    print(f"{Fore.MAGENTA}[2]{Fore.RESET} Return to main menu")
    colors.menu_option("Enter your choice: ")
    
    choice = input().strip()
    if choice == "1":
        generate_capes()
    elif choice == "2":
        return
    else:
        colors.error("Invalid option. Exiting.")
        sys.exit()

def download_code(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        colors.error(f"Failed to download file. Status code: {response.status_code}")
        sys.exit()

def generate_capes():
    login_file_url = "https://raw.githubusercontent.com/pigmine797/cape_gen/main/opt.txt"  # Substitua pela URL correta
    code_file_url = "https://raw.githubusercontent.com/pigmine797/cape_gen/main/cape_generator.py"  # Substitua pela URL correta

    code_script = download_code(code_file_url)
    login_data = download_code(login_file_url)

    login_lines = login_data.splitlines()
    
    if not os.path.exists("results/capes"):
        os.makedirs("results/capes")

    def get_current_day():
        return time.strftime("%Y-%m-%d")

    def load_generated_count():
        day = get_current_day()
        count_file = f"results/capes/count_{day}.txt"
        if os.path.exists(count_file):
            with open(count_file, "r") as f:
                return int(f.read().strip())
        else:
            return 0

    def save_generated_count(count):
        day = get_current_day()
        count_file = f"results/capes/count_{day}.txt"
        with open(count_file, "w") as f:
            f.write(str(count))

    generated_today = load_generated_count()

    if generated_today >= 20:
        colors.error("Limit of 20 capes per day reached. Exiting.")
        sys.exit()

    colors.success("Generating capes...")

    for login in login_lines:
        email, password = login.split(":")
        cape_filename = f"results/capes/{email}.txt"
        
        # Execute the cape generation script
        exec(code_script)  # Execute the external code (ensure it’s safe)
        
        with open(cape_filename, "w") as f:
            f.write(f"Login: {login}\n")
            f.write("Generated cape content here...")  # Replace this with actual content from the script

        generated_today += 1
        save_generated_count(generated_today)

        if generated_today >= 20:
            colors.error("Limit of 20 capes per day reached. Exiting.")
            break
        
        time.sleep(30)  # Cooldown of 30 seconds

    colors.success("Cape generation completed.")

if __name__ == "__main__":
    cape_generator_menu()
