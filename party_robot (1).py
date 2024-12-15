import pygame
import time
import random
import glob
from pygame import mixer

pygame.init()
GPIO.setmode(GPIO.BCM)

RED_PIN1 = 19
GREEN_PIN1 = 13
BLUE_PIN1 = 6

RED_PIN2 = 16
GREEN_PIN2 = 20
BLUE_PIN2 = 21

# Initialize GPIO
GPIO.setup([RED_PIN1, GREEN_PIN1, BLUE_PIN1, RED_PIN2, GREEN_PIN2, BLUE_PIN2], GPIO.OUT)

# PWM Setup
red_pwm1 = GPIO.PWM(RED_PIN1, 1000)  # 1 kHz frequency
green_pwm1 = GPIO.PWM(GREEN_PIN1, 1000)
blue_pwm1 = GPIO.PWM(BLUE_PIN1, 1000)

red_pwm2 = GPIO.PWM(RED_PIN2, 1000)
green_pwm2 = GPIO.PWM(GREEN_PIN2, 1000)
blue_pwm2 = GPIO.PWM(BLUE_PIN2, 1000)

red_pwm1.start(0)
green_pwm1.start(0)
blue_pwm1.start(0)
red_pwm2.start(0)
green_pwm2.start(0)
blue_pwm2.start(0)

# Color Data
colors = [
    (255, 0, 0), (225, 0, 168), (225, 154, 0), (255, 255, 0),
    (144, 238, 144), (0, 255, 0), (173, 208, 231), (0, 0, 255),
    (166, 0, 225), (255, 255, 255)]


def set_color(pwm_red, pwm_green, pwm_blue, red, green, blue):
    pwm_red.ChangeDutyCycle(red / 255 * 100)    # Scale 0-255 to 0-100%
    pwm_green.ChangeDutyCycle(green / 255 * 100)
    pwm_blue.ChangeDutyCycle(blue / 255 * 100)

def turn_off():
    red_pwm1.stop()
    green_pwm1.stop()
    blue_pwm1.stop()
    red_pwm2.stop()
    green_pwm2.stop()
    blue_pwm2.stop()
    GPIO.cleanup()


#constants
WIDTH, HEIGHT = 800, 600
WHITE = (225, 225, 255) #sets up amount of red green and blue in varible White
GREEN = (0,255,0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
circle_radius = 50
smaller_circle_radius = circle_radius // 2
volume_square_width = 100  # Width of the volume rectangle
volume_square_height = 50  # Height of the volume rectangle
directory = "/home/norahahnstedt/party_robot" #saves this path to a directory under "directory" to be used in line 13

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set's the size of application as vairable width and height
pygame.display.set_caption("Control system") #sets title of application widow


#load songs
def get_songs(): #this is where I will load in each of my downloaded songs, this song will be the first thing called in the main function
    playlist = [] #creates an empty list to add songs to as directory is scanned for audio files
    mp3_files = glob.glob(f"/home/norahahnstedt/party_robot/*.mp3")
    for file in mp3_files: #for each file in the files seach
            playlist.append(file)
    return playlist

#load images (app)
def load_images(file_path, size):
    image = pygame.image.load(file_path)
    return pygame.transform.scale(image, size)

backward_skip_image = load_images("/home/norahahnstedt/party_robot/skipback.svg", (circle_radius * 2, circle_radius * 2)) #loads skip button image #THIS IS WHERE YOU PUT THE PATH TO IMAGE FOR SKIP BACK
forward_skip_image = load_images("/home/norahahnstedt/party_robot/SkipNext.svg", (circle_radius * 2, circle_radius * 2))
play_image = load_images("/home/norahahnstedt/party_robot/Play.svg", (circle_radius * 2, circle_radius * 2)) #THIS IS WHERE PLAY IMAGE PATH GOES
pause_image = load_images("/home/norahahnstedt/party_robot/Pause.svg", (circle_radius * 2, circle_radius * 2)) #THIS IS WHERE PAUSE IMAGE PATH GOES
minus_image = load_images("/home/norahahnstedt/party_robot/Minus.png", (smaller_circle_radius, smaller_circle_radius))
plus_image = load_images("/home/norahahnstedt/party_robot/Plus.png", (smaller_circle_radius , smaller_circle_radius))

#pause/play/skips
play_button_x, play_button_y = WIDTH // 2, HEIGHT // 2
circle_center_forward = (play_button_x + 150, play_button_y)  # Position circle 100px to the right of the play button
circle_center_backward = (play_button_x - 150, play_button_y) # Position circle 100px to left of play button
#shuffle
shuffle_button_y = HEIGHT // 2 + 150  # Position it 150px below the center (adjust as needed)
shuffle_button_x = WIDTH // 2  # Center it horizontally
shuffle_button_width, shuffle_button_height = 200, 50  # Width and height of the rectangle
#volume
minus_button_center = (WIDTH // 2 - 100, 90)  # Left circle
plus_button_center = (WIDTH // 2 + 100, 90)   # Right circle
volume_square_x = WIDTH // 2 - volume_square_width // 2  # Center the volume square between the buttons
volume_square_y = 65  # Set the vertical position for the volume display rectangle

#Vairbles
playlist = get_songs()
current_song_index = 0
shuffle = False
volume = 50
state = 1  # 1: Paused, 2: Playing

#Functions
# Volume setup
def toggle_volume_up():
    global volume
    volume = min(volume + 5, 100)
    mixer.music.set_volume(volume / 100)

def toggle_volume_down():
    global volume
    volume = max(volume - 5, 0)
    mixer.music.set_volume(volume / 100)

#Shuffle control
def toggle_shuffle():
    global shuffle, playlist, current_song_index
    shuffle = not shuffle

    if shuffle:
        current_song=playlist[current_song_index]
        playlist = random.sample(playlist, len(playlist))
        current_song_index = playlist.index(current_song)

    else:
        playlist = get_songs()
        current_song_index %= len(playlist)

#Music Control
def play_audio():
    global state  # Allows function to modify the variable "state" defined outside
    song = playlist[current_song_index % len(playlist)]
    if state == 1:  # If paused, unpause the music
        if mixer.music.get_pos() == -1:  # If no song is loaded, load and play the current song
            mixer.music.load(song)
            mixer.music.play()
        else:
            mixer.music.unpause()
        state = 2  # Change state to "Playing"

def stop_audio():
    global state
    if state == 2:
        mixer.music.pause()
        state = 1 #the state is "paused"

def skip_forward():
    global current_song_index, state
    if playlist:
        current_song_index = (current_song_index + 1) % len(playlist)  # Increment index
        song = playlist[current_song_index]
        mixer.music.load(song)
        mixer.music.play()  # Automatically play the next song
        state = 2  # Update state to "Playing"


def skip_backward():
    global current_song_index, state
    if playlist:
        current_position = mixer.music.get_pos()
        if current_position > 3000:  # If more than 3 seconds into the song
            song = playlist[current_song_index]
            mixer.music.load(song)  # Reload the current song
            mixer.music.play()  # Restart the current song        e
        else:
            current_song_index = (current_song_index - 1) % len(playlist)  # Decrement index
            song = playlist[current_song_index]
            mixer.music.load(song)
            mixer.music.play()  # Automatically play the previous song
        state = 2  # Update state to "Playing"

def handle_shuffle():
    global shuffle, playlist
    shuffle = not shuffle
    playlist = random.sample(playlist, len(playlist)) if shuffle else get_songs()

def random_rgb_color():
    return random.choice(colors)


# Main loop
running = True
last_light_change = time.time()
random_interval = random.uniform(0.5, 2.0)
while running:

    #background color is white
    screen.fill(WHITE)
    pygame.mixer.music.set_volume(volume)


    #creates title
    font = pygame.font.Font(None, 48)
    title_text = font.render("Music Control System", True, GREEN)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30)) #positions text in top middle of application
    screen.blit(title_text, title_rect) #actually draw the text on the screen

    #creates shuffle button
    shuffle_color = GREEN if not shuffle else RED
    pygame.draw.rect(screen, shuffle_color, (shuffle_button_x - shuffle_button_width // 2, shuffle_button_y - shuffle_button_height // 2, shuffle_button_width, shuffle_button_height))  # Draw the rectangle
    font = pygame.font.Font(None, 36)  # Set the font size for the text
    shuffle_text = "Shuffle On" if shuffle else "Shuffle Off"
    text_surface = font.render(shuffle_text, True, BLACK)  # Render the text
    text_rect = text_surface.get_rect(center=(shuffle_button_x, shuffle_button_y))  # Position text at the center of the button
    screen.blit(text_surface, text_rect)  # Draw the text on the screen

    #Draw green circle for play button (depending on state)
    if state == 1: #(paused state, green play button)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), circle_radius)
        screen.blit(play_image, (play_button_x - circle_radius, play_button_y - circle_radius))
    elif state == 2:
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), circle_radius)
        screen.blit(pause_image, (play_button_x - circle_radius, play_button_y - circle_radius))
    pygame.draw.circle(screen, GREEN, circle_center_forward, circle_radius)
    screen.blit(forward_skip_image, (circle_center_forward[0] - circle_radius , circle_center_forward[1] - circle_radius))

    # Draw backward skip button
    pygame.draw.circle(screen, GREEN, circle_center_backward, circle_radius)
    screen.blit(backward_skip_image, (circle_center_backward[0] - circle_radius, circle_center_backward[1] - circle_radius))

    #Draw plus button
    pygame.draw.circle(screen, GREEN, plus_button_center, smaller_circle_radius)
    screen.blit(plus_image, (plus_button_center[0] - smaller_circle_radius //2 , plus_button_center[1] - smaller_circle_radius // 2))

    #Draw minus button
    pygame.draw.circle(screen, GREEN, minus_button_center, smaller_circle_radius)
    screen.blit(minus_image, (minus_button_center[0] - smaller_circle_radius //2, minus_button_center[1] - smaller_circle_radius// 2))

    #Draw Volume display
    font = pygame.font.Font(None, 48)
    volume_text = font.render(f"{volume}%", True, BLACK)  # Render volume percentage as text
    text_rect = volume_text.get_rect(center=(volume_square_x + volume_square_width // 2, volume_square_y + volume_square_height // 2))
    screen.blit(volume_text, text_rect)  # Draw the text on the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #if mouse clicks check to find at what position it clicked
            mouse_x, mouse_y = pygame.mouse.get_pos() #x and y coordinates for mouse

            #shuffle button clicked
            if (shuffle_button_x - shuffle_button_width // 2 <= mouse_x <= shuffle_button_x + shuffle_button_width // 2 and
                shuffle_button_y - shuffle_button_height // 2 <= mouse_y <= shuffle_button_y + shuffle_button_height // 2):
                toggle_shuffle()
            #pause/play button clicked
            if (play_button_x - circle_radius <= mouse_x <= play_button_x + circle_radius and
                play_button_y - circle_radius <= mouse_y <= play_button_y + circle_radius):
                if state == 1: #if button was clicked while paused run play audio function
                    play_audio()
                    state = 2
                else: #if button was clicked while playing run stop audio function
                    stop_audio()
                    state = 1
            #forward skip button clicked
            if (circle_center_forward[0] - circle_radius <= mouse_x <= circle_center_forward[0] + circle_radius and
                circle_center_forward[1] - circle_radius <= mouse_y <= circle_center_forward[1] + circle_radius):
                skip_forward() #if button clicked run skip function
            #Backward skip button clicked
            if (circle_center_backward[0] - circle_radius <= mouse_x <= circle_center_backward[0] + circle_radius and
                circle_center_backward[1] - circle_radius <= mouse_y <= circle_center_backward[1] + circle_radius):
                skip_backward() #if button clicked run backward skip function
            #Minus button clicked
            if (mouse_x - minus_button_center[0])**2 + (mouse_y - minus_button_center[1])**2 <= smaller_circle_radius**2:
               toggle_volume_down()

            #Plus button clicked
            if (mouse_x - plus_button_center[0])**2 + (mouse_y - plus_button_center[1])**2 <= smaller_circle_radius**2:
                toggle_volume_up()

            if state == 2 and time.time() - last_light_change > random_interval:
                r, g, b = random.choice(colors)
                set_color(red_pwm1, green_pwm1, blue_pwm1, r, g, b)
                set_color(red_pwm2, green_pwm2, blue_pwm2, r, g, b)
                last_light_change = time.time()
                random_interval = random.uniform(0.5, 2.0)





    pygame.display.flip()

turn_off()
pygame.quit()









