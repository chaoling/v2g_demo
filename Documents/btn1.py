from gpiozero import LED,Button
from time import sleep

#setup the button on GPIO pin 4

start_btn = Button(2)
v2g_btn = Button(3)
stop_btn = Button(17)
led_green = LED(4)
led_blue = LED(27)
led_red = LED (22)

#Define function to run when the button is pressed
def start_charging():
    led_green.on()
    led_red.off()
    led_blue.off()
    print("start charging...")
    
def start_v2g():
    led_blue.on()
    led_red.off()
    led_green.off()
    print("start v2g charging...")
    
def stop_charging():
    led_red.on()
    led_blue.off()
    led_green.off()
    print("Button pressed, stop charging...")
    
# Assign the function to the button's "when_pressed" event
start_btn.when_pressed = start_charging
v2g_btn.when_pressed = start_v2g
stop_btn.when_pressed = stop_charging

# Run the program until user kills it
led_red.off()
led_green.off()
led_blue.off()
while True:
    sleep(0.1)