# ShameOnYou
A Python Module designed to find and brute force Zoom Meeting ID's, with different modes.

## Introduction
 This Idea began when a saw a zWarDial Concept that could crack almost 100 Zoom Meeting ID's in almost 60 Minutes. With that goal in mind, I started this project, to help the security research community in fixing such flaws in the Zoom Meeting Software.

### Limitations of other Tools

I saw many different tools, like ZoomBrute which have now become obsolete and are of no use anymore, so I decided to make something that works like a charm and has a lot of support hopefully. This is not only a Tool but a Python Module to Brute Force the Zoom Meeting ID, so it is easier to incooperate in other things, with litte work for others to do.

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

`python3 main.py`

This will start the Program, it is reccomended if you have more *Important Stuff to Do*, the best stradegy is to download a Windows 10 VM and Install Zoom in it and let it running. 

### Wallpaper for Best Results

I added the Windows XP Bliss Wallpaper to use, as the Windows Button changes itself depending upon the background, Like see this Example below

![Windows Button Without Bliss](Windows_Button.PNG) ==> ![Windows Button Without Bliss](Windows_Button_2.PNG)

So for the best results use the Bliss Wallpaper Included and yes its nostalgic no need to say Thanks :)

### Demo

Here is a Demo of the Program itself [CLI]

##### Video Demo

I found a working ID Second Try, I mean lolz

[![Watch the video](https://img.youtube.com/vi/rJTbF7gdH7g/maxresdefault.jpg)](https://youtu.be/rJTbF7gdH7g)

### Modes
`
self.meetings_dict = {
            'personal_meeting_old':9,
            'personal_meeting_new':10,
            'scheduled_meeting':11
        }
`

## Future Features

- Adding a Server that connects all the VM's and increase the Brute Forcing Speed by stopping the duplicates.
- Password Cracker
- Support for MacOS, Ubuntu and Kali Linux [Hopefully]
- GUI (Comming Really Soon)

## License

MIT License (C) 2021 Muneeb Ahmad

## Read before using

Zoom Bombing or joining a Zoom Meeting without Permission is considered a intrusion of privacy and it is strictly prohibited, do not use this for illegal purposes,
as this project is soley intended for helping the research community and making this to raise awareness and hopefully stopping this from happening. If you use this for
illegal purposes then it is totally on you my intention was clear and and it is that this is indended for research purposes. :) (Hope you Understand Hehe)
