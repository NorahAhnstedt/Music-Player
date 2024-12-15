# **Music Control System with RPG Lights**

## **About The Project**
This project combines Python Programming and a Raspberry Pi to create a music control system that can be displayed through an application. The PI is equipped with RPG lights, which change color when the music is playing. Users can interact with the music control interface directly, using SSH to access the Pi remotely. The goal of this project is to provide an enjoyable experience for users.

The system will function using Pygame to create an interactive music interface, with buttons for playback controls. This will be done using If statements to dictate what will happen when a button is pressed. The LEDs, which are connected to the Pi through a breadboard, light up and cycle through colors when the variable state is equal to two, which is when the music is playing.

Key features include:
- On-screen music playback interface with the options - play, pause, skip, shuffle, and volume control
- LED lights synchronized with music playback that cycle through the randomized list of colors

## **List of Materials** 
- Raspberry Pi with Wi-Fi/Bluetooth capability
- MicroSD Card with Raspberry Pi OS
- Power Supply for Raspberry Pi
-  RPG LED lights
-  Resistors
-  Breadboard
-  Jumper wires
-  Computer capable of SSH access
-  Python libraries: Pygame, RPi.GPIO, time module, glob module, and random module

## **How to Wire** 
### **LED Light Circuit**
 <img width="637" alt="Ciruit wiring" src="https://github.com/user-attachments/assets/9923f37c-0d17-41bf-87ad-cce3942c80ba" />
 This is an example circuit created through Tinkercad, because it doesn't have a GPIO board option I used an Arduino Uno which is very similar. 
To create a circuit that does the same thing using a GPIO pin:
1. RGB LED 1 
   a. Red: GPIO 19
   b. Green: GPIO 13
   c. Blue: GPIO 6
   d. Cathode/Anode: GND and RGB LED 2's Cathode/Anode
2. RGB LED 2
   a. Red: GPIO 16
   b. Green: GPIO 20
   c. Blue: GPIO 21
   d. Cathode/Anode: RGB LED 3's Cathode/Anode
3. RGB LED 3 
   a. Red: GPIO 19
   b. Green: GPIO 13
   c. Blue: GPIO 6
   d. Cathode/Anode: RGB LED 4's Cathode/Anode
4. RGB LED 4
   a. Red: GPIO 16
   b. Green: GPIO 20
   c. Blue: GPIO 21
   d. Cathode/Anode: GND

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
The Python code can be broken down into three main components 
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
- Simple Guide to RGP LED's - https://www.build-electronic-circuits.com/rgb-led/#:~:text=Common%20Anode%20RGB%20LED,side%20of%20a%20power%20supply.
- Controlling RGB led using Raspberry pi - https://digitalab.org/2022/09/controlling-rgb-led-using-raspberry-pi/
- Tinkercad dashboard - https://www.tinkercad.com/dashboard
- RGB color picker - https://rgbcolorpicker.com/

### **Website used to convert and download .mp3 files**
FreeMP3Music - https://freemp3music.org/
MP3 juice - https://gugsfm.co.za/](https://emp3juice.la/)

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

## **The Future of this project**
Originally I had planned to create a robot using a simple robot kit, that could be controlled via remote control. This robot would house the Pi and allow the lights to move around despite being controlled by a computer application. This was something that I realized was an unrealistic goal to complete within the timeline of this project, however, I do think it will add to the overall performance of the project. Another thing that I hoped to do, which I knew that I wouldn't have time for, was to convert the pygame code into an app that was accessible through my phone, and then create more button controls for the robot. This is to make the entire project cohesive and allow for all of the variables to be manipulated through one app. 


## **Look at the attached files to see the finished product and image documentation throughout the project.** 


