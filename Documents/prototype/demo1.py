from gpiozero import LED,Button
import os
from time import sleep
import pygame

#setup the button on GPIO pin 4

start_btn = Button(2)
v2g_btn = Button(3)
stop_btn = Button(17)
led_green = LED(4)
led_blue = LED(27)
led_red = LED (22)


# Set up Pygame
pygame.init()
os.environ["DISPLAY"] = ":0"
pygame.display.init()
width=1600
height=960
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)

# Load images

splash_image = pygame.image.load("battery.png")
charge1_image = pygame.image.load("charge1.png")
charge2_image = pygame.image.load("charge2.png")
splash_image = pygame.transform.scale(splash_image, (width, height))
charge1_image = pygame.transform.scale(charge1_image, (width, height))
charge2_image = pygame.transform.scale(charge2_image, (width, height))
bg_color=(255,255,255)
stop_count = 0

#Define function to run when the button is pressed
def show_splash_screen():
    screen.fill(bg_color)
    screen.blit(splash_image, (0, 0))
    pygame.display.flip()
    led_red.off()
    led_green.off()
    led_blue.off()
    

def img_transition(image1, image2, transition_time = 200, transition_steps = 10, bg_color=(255,255,255)):
    #show transition from image1 to image2

    # Blit image1 to screen
    if image1:
        screen.blit(image1, (0, 0))

    # Get image dimensions
    img_width, img_height = image1.get_size() if image1 else image2.get_size()

    # Calculate step size for transition
    step_size = img_height // transition_steps

    # Start transition
    for i in range(transition_steps):
        # Fill screen with background color
        screen.fill(bg_color)
        
        # Calculate new y position for image2
        y_pos = img_height - step_size * i
        
        # Blit image1 and image2 to screen
        if image1:
            screen.blit(image1, (0, 0))
        screen.blit(image2, (0, y_pos))
        
        # Update display
        pygame.display.flip()
        
        # Wait for transition time / steps
        pygame.time.wait(transition_time // transition_steps)


def start_charging():
    led_green.on()
    led_red.off()
    led_blue.off()
    print("start charging...")
    img_transition(splash_image,charge1_image)
    #screen.blit(charge1_image, (0, 0))
    #pygame.display.flip()
    

def start_v2g():
    led_blue.on()
    led_red.off()
    led_green.off()
    print("start v2g charging...")
    img_transition(splash_image,charge2_image)
    #screen.blit(charge2_image, (0, 0))
    #pygame.display.flip()
    

def stop_charging():
    global stop_count
    stop_count += 1
    led_red.on()
    led_blue.off()
    led_green.off()
    print(f"Button pressed, stop charging {stop_count=}...")
    if stop_count == 1:
       img_transition(None,splash_image,transition_time = 100, transition_steps = 5)
    else:
        led_red.off()
        print(f"Button pressed twice, exit program")
        exit(0)
        
    
# Assign the function to the button's "when_pressed" event
start_btn.when_pressed = start_charging
v2g_btn.when_pressed = start_v2g
stop_btn.when_pressed = stop_charging

# Run the program until user kills it
show_splash_screen()
while True:
    sleep(0.1)
