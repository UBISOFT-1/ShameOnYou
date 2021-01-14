# ShameOnYou
A Python Module designed to find and brute force Zoom Meeting ID's, with different modes.

## Introduction
 This Idea began when a saw a zWarDial Concept that could crack almost 100 Zoom Meeting ID's in almost 60 Minutes. With that goal in mind, I started this project, to help the security research community in fixing such flaws in the Zoom Meeting Software.

### Limitations of other Tools

I saw many different tools, like ZoomBrute which have now become obsolete and are of no use anymore, so I decided to make something that works like a charm and has a lot of support hopefully. This is not only a Tool but a Python Module to Brute Force the Zoom Meeting ID and the Password if there is one, so it is easier to incooperate in other things, with litte work for others to do.

## Usage

**Note**
This Program is currently in BETA mode so, and is under active development, if you have any suggestions or want to work with me feel free to contact me on Github by starting a **ISSUE** or contacting me at *jacobkhanjamali@gmail.com*. 

## Supported OS

- Windows 10 [Zoom Needs to Be Installed for it to Work]
- Windows 7 (Provided if take snapshots of the start button for your use case)

## Requirements

Use any version of Python 3.6.x and install the following Modules to go with them.

- `pip install pyautogui`
- `pip install selenium`
- `pip install random`
- `pip install numpy`

## Usage

**Step 1**

Clone this Github Repository by Typing
`git clone https://github.com/UBISOFT-1/ShameOnYou.git`

**Step 2**

Extract the rockyou.rar to this Folder (ShameOnYou) with the rest of the scripts so that the Password Dict Should be used :)

**Step 3**

Open CMD and change Directory/Folder to ShameOnYou

`cd ShameOnYou`

**Step 5**

Then, type

`python3 main.py` *or* `python main.py` *or* `py main.py`

Leave it running do not touch anything, change the active window to Zoom if it does not itself.

This will start the Program, it is recommended if you have more *Important Stuff to Do*, the best stradegy is to download a Windows 10 VM and Install Zoom in it and let it running. 

## Update v1.BETA

Major Code Changes, Now Added a Password Brute Forcer, you can add your Custom Dictionary as Well.
- First Generates the Meeting ID
- Then if it works then goes on to Brute Force it if it is Password Protected
- When Password is BruteForced saves it in a File named Works.txt Format *meeting:password*
- Note in Zoom-Meeting.txt saves the meeting_ids like Format (meeting_id:req_pswd/no_req_psws)

**Success Rate** According to Current Testing 97%

**Captcha Evasion** [Works] Bypasser


### Wallpaper for Best Results

I added the Windows XP Bliss Wallpaper to use, as the Windows Button changes itself depending upon the background, Like see this Example below

![Windows Button Without Bliss](Windows_Button.PNG) ==> ![Windows Button Without Bliss](Windows_Button_2.PNG)

So for the best results use the Bliss Wallpaper Included and yes its nostalgic no need to say Thanks :)

### Demo

Here is a Demo of the Program itself [CLI]

##### Video Demo

I found a working ID Second Try, I mean lolz

[![Watch the video](https://img.youtube.com/vi/rJTbF7gdH7g/maxresdefault.jpg)](https://youtu.be/rJTbF7gdH7g)

Note This Video Does not show the Ottoman BruteForcer in Action, gonna make a video on that as well,

### Modes
`
self.meetings_dict = {
            'personal_meeting_old':9,
            'personal_meeting_new':10,
            'scheduled_meeting':11
        }
`

## Future Features
- Password BruteForcer [Completed]
- Adding a Server that connects all the VM's and increase the Brute Forcing Speed by stopping the duplicates.
- Support for MacOS, Ubuntu and Kali Linux [Hopefully]
- GUI (Coming Really Soon)

## Recommendations




## License

MIT License (C) 2021 Muneeb Ahmad

## Read before using

Zoom Bombing or joining a Zoom Meeting without Permission is considered a intrusion of privacy and it is strictly prohibited, do not use this for illegal purposes,
as this project is soley intended for helping the research community and making this to raise awareness and hopefully stopping this from happening. If you use this for
illegal purposes then it is totally on you my intention was clear and and it is that this is indended for research purposes. :) (Hope you Understand Hehe)
