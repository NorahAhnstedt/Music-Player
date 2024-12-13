# **Music Control System with Mobile Robot**

## **About The Project**
This project combines Python Programming and robotics to create a music control system that can be displayed through an application. The PI is housed within a mobile robot, allowing the LED lights, which change color when the music is playing, to move around via remote control. Users can interact with the music control interface directly, even with the Pi being attached to the robot due to using SSH to access the Pi remotely. The goal of this project is to provide an enjoyable experience for users.

The system will function using Pygame to create an interactive music interface, with buttons for playback controls. This will be done using If statements to dictate what will happen when a button is pressed. The LEDs, which are connected to the Pi through a breadboard, light up and cycle through colors when the variable state is equal to two, which is when the music is playing. This aspect adds a visual element and makes the application interface and robot component more cohesive. The robot's mobility is controlled via a remote. 

Key features include:
- On-screen music playback interface with the options - play, pause, skip, shuffle, and volume control
- LED lights synchronized with music playback that cycle through the randomized list of colors
- Robot movement controlled by a remote

## **List of Materials** 
- Raspberry Pi with Wi-Fi/Bluetooth capability
- MicroSD Card with Raspberry Pi OS
- Power Supply for Raspberry Pi
- Simple Robot kit
- Remote control
-  RPG LED strips
-  Resistors
-  Breadboard
-  Jumper wires
-  Computer capable of SSH access
-  Python libraries: Pygame, RPi.GPIO, time module, glob module, and random module

## **How to Wire** 
### **LED Light Circuit**
[ ] add here 

### **Robot Assembly** 
[ ] add here 

## **How to Run the Program** 
1. **Setup Raspberry Pi.** Install the required libraries:
   ```
   pip install Pygame
   pip install RPi.GPIO
   pip install random
   pip install time
   ```
2. **Download and Transfer Music Files.** Find online resources that allow you to convert other file types into .mp3 files (see resource section below) then place .mp3 files in the directory where the python script is located on the Raspberry Pi, `party_robot`
3. **SSH into Raspberry Pi.**
   ```bash
   ssh pi@<respberry_pi_ip_adress>
   ```
4. **Run Python Script**
   ```bash
   python3 party_robot.py
   ```
5. **Interact with the Music System.** Use the computer's keyboard and mousepad to control music playback and remote control for movement.

## **What Does the Code Do?**
The Python code can be broken down into four main components 
1. **Pygame Application**
   - this is the part that creates a GUI with buttons for play, pause, skip, shuffle, and volume control
   - It responds to mouse clicks which trigger corresponding actions within other components
2. **Music Playlist**
   - Uses Pygame mixer to load and manage a playlist
   - the playlist starts as a blank list that is appended for each file containing .mp3 in the directory `party_robot`.
   - This is the part that implements functions for pause, play, skip, shuffle, and volume adjustments made through the GUI
3. **LED Control**
   -Uses the RPi.GPIO library to manage the LED light strips
   -Cyles through colors while music is being played and turns off when music is paused
4. **Robot Control**
   -Reads input from remote control to move the robot
   - Where Pi is located, meaning both the speaker and LED lights can move, through user interaction

To learn more about how each aspect works together look at the Python script called `party_robot.py` as it contains line by line description of what each piece of code does. 

## **Resources** 

### **Images rendered onto buttons on GUI** 
- Skip Previous - https://www.streamlinehq.com/icons/download/skip-previous--32230
- Skip Next - https://www.streamlinehq.com/icons/download/skip-next--32230
- Play - https://www.streamlinehq.com/icons/download/play-arrow--32230
- Pause - https://www.streamlinehq.com/icons/download/pause--32230
- Plus Sign - https://www.streamlinehq.com/icons/download/add-1--25622
- Minus Sign - https://www.streamlinehq.com/icons/download/subtract-1--25622

### **Learning to use Pygame to create applications** 
- Get started in pygame in 10 minutes - https://www.youtube.com/watch?v=y9VG3Pztok8
- Display images - https://www.geeksforgeeks.org/python-display-images-with-pygame/
- Making apps with pygame - https://www.geeksforgeeks.org/making-apps-with-pygame/
- Moving shapes in pygame - https://www.youtube.com/watch?v=-3oC2C5oNFc
- Pygame.Mouse https://www.pygame.org/docs/ref/mouse.html

### **Using RPG LED strips** 
- Controlling RGB led using Raspberry pi - https://digitalab.org/2022/09/controlling-rgb-led-using-raspberry-pi/
- Breadboard Circuit tutorial - Simple LED - https://www.youtube.com/watch?v=zvCdkV52cis
- Lesson 7 RGB LED - https://learn.sunfounder.com/lesson-7-rgb-led/
- Lighting Terms - https://www.environmentallights.com/library/pwm
- RGB color picker - https://rgbcolorpicker.com/


### **Robot Setup**
[ ] Insert here 

### **Website used to convert and download .mp3 files**
- FreeMP3Music - https://freemp3music.org/
- MP3 juice - https://emp3juice.la/

#### **.mp3 files used for project**
- Endor - Pump It Up (official video)
- Disclosure - You & Me (Flume Remix) [Official Video]
- Dom Dolla - Saving Up
- FISHER x KITA ALEXANDER - ATMOSPHERE [LYRIC VIDEO]
- PAWSA - PICK UP THE PHONE ft. Nate Dogg (Lyrics)
- LF SYSTEM - Afraid To Feel (Official Lyric Video)
- Flume feat. Toro y Moi - The Difference (Official Music Video)
- Empire Of The Sun - Walking On A Dream (Official Music Video)
- Louis The Child & Icona Pop - Weekend (Audio)
- Music Sounds Better With You - Stardust



## **Look at the attached files to see the finished product and image documentation throughout the project.** 


