# SPDX-FileCopyrightText: 2020 John Furcean
# SPDX-License-Identifier: MIT

import time
import board  
from digitalio import DigitalInOut, Direction, Pull

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import neopixel

# time you want to hold the button down before it changes states
BUTTON_HOLD_TIME = 1
PLATFORM = "windows"  # Options: windows, linux, mac
# profile = "jitsi"
DEBUG = False
SELECTION_TIMEOUT = 1.5  # Value in seconds to choose a chat profile

def button_pressed(button):
    return button.value

def select_profile(profiles, led, button):
    all_profiles = list(profiles.keys())
    all_profiles.remove('mute')  # Can't select 'mute' as a profile

    selected_profile = False

    
    while not selected_profile:
        for profile in all_profiles:  # Iterate through chat applications
            if DEBUG:
                print(led)
                print(profiles[profile])
            start_time = time.monotonic() # Start the timer
            rgb_led[0] = profiles[profile]["color"]  # Display the application color
            
            while time.monotonic() - start_time < SELECTION_TIMEOUT:  # Has X time passed?
                
                if button.value == True:  # Button has been pressed
                    if DEBUG:
                        print("Profile Selected: " + profile)
                    time.sleep(0.5) # Give time to remove finger
                    return(profile)  # 
                
                time.sleep(0.1)
                
            


# initialize onboard neopixel
# this will be used to indiciate what application is enabled
rgb_led = neopixel.NeoPixel(board.NEOPIXEL, 1)
rgb_led.brightness = 1.0
rgb_led[0] = (0, 0, 0)

kbd = Keyboard(usb_hid.devices)

# Digital input with pulldown on Neokey
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False  # Starting with button not being pressed

# This will be used to indicate if muted or not
# please note that an individual will have to make sure it is synced with the application
# button_led = DigitalInOut(board.D0)
# button_led.direction = Direction.OUTPUT


# Defines what the different states of the buttons will do

# Note: in order for the code to work appropriately,
# the keys need to start at 0 and increment upwards.
# Single keycodes commands need to have a trailing comma (,)
# the below keycode commands are for Mac and will need to be
# modified for Windows or Linux

platform_keys = {
    "windows": Keycode.CONTROL,
    "linux": Keycode.CONTROL,
    "mac": Keycode.COMMAND
}

platform_key = platform_keys[PLATFORM]  # Sets platform key to either CMD or CTRL

profiles = {

    "mute" : {
            'name': 'Mute',
            'color':(255, 0, 0)
        },
    "zoom" : {
            'name': 'Zoom',
            'keycode': (Keycode.ALT, Keycode.A),
            'color':(0, 0, 205)
        },
    "teams" : {
            'name': 'MS Teams',
            'keycode': (platform_key, Keycode.SHIFT, Keycode.M),
            'color':(120, 0, 255)
        },
    "meet" : {
            'name': 'Google Meet',
            'keycode': (platform_key, Keycode.SHIFT, Keycode.D),
            'color':(12, 132, 0)
        },
    "slack" : {
            'name': 'Slack',
            'keycode': (Keycode.M),
            'color':(200, 80, 0)
        },
    "jitsi" : {
            'name': 'Jitsi',
            'keycode': (Keycode.M),
            'color':(65, 200, 190)
        }

}



# button_held_in = False
button_index = 0
change_button = False
mute = False  # Starting value 
profile = select_profile(profiles, rgb_led, button)  # Get the desired chat app

while True:

    # retreive the active controller button
    controller_button = profiles[profile]
    if DEBUG:
        print("Profile: " + controller_button['name'])
        print("Mute: " + str(mute))

    # set the color of the onboard neopixel to match the active controller button
    if not mute:
        rgb_led[0] = controller_button['color']  # Set the LED to the chat color
    else:
        rgb_led[0] = profiles['mute']['color']  # Turn the LED red


    # detect if the button is recently pressed in
    #if button_pressed(button) and not button_held_in:
    #    button_led.value = not button_led.value
    #    button_held_in = True
    #    start_hold = time.monotonic()

    # detect if the button is being held down
    #if button_pressed(button) and button_held_in:
    #    time_now = time.monotonic()

        # change the state of the button controller if
        # the button has been held down for BUTTON_HOLD_TIME or more seconds
        # if time_now - start_hold > BUTTON_HOLD_TIME and not change_button:
        #    print('Change State')
        #    button_index += 1
        #    start_hold = time.monotonic()
        #   button_led.value = False
        #   change_button = True


    # detect if the button has been released
    if button_pressed(button):

        # execute the keyboard commands for the active button controller
        # if state of button controller hasn't been changed
        #if not change_button:
        print("{} mute button press".format(controller_button['name']))
        
        try:
            kbd.send(controller_button['keycode'])  # Send a one key mute command
        except TypeError as e:
            kbd.send(*controller_button['keycode'])  # Send a multi key mute command

            
        #if len(controller_button['keycode']) > 1:  # Command uses multiple keys
        #    kbd.send(*controller_button['keycode'])  # Send the mute command
        #else:
        #    kbd.send(controller_button['keycode'])  # Send the mute command
        mute = not mute  # Toggle the boolean    
        if not mute:
            rgb_led[0] = controller_button['color']  # Set the LED to the chat color
        else:
            rgb_led[0] = profiles['mute']['color']  # Turn the LED red
        time.sleep(0.5)  # Give time to remove fingermm
        # reset the change_button boolean if the state has been changed
        #else:
        #    change_button = False

        # update the state of the my_button_held_in Boolean         
        # button_held_in = False

    if DEBUG:
        time.sleep(1)
        print("Button Pressed: " + str(button_pressed(button)))
    else:
        time.sleep(0.1)
