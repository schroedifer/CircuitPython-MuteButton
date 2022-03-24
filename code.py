# SPDX-FileCopyrightText: 2020 John Furcean
# SPDX-License-Identifier: MIT

import time
import board
from digitalio import DigitalInOut, Direction, Pull

import usb_hid
from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# from adafruit_hid.keycode import Keycode

import neopixel
from config import * # User settings in config.py
from profiles import profiles  # Import dictionary of buttons and lights

def button_pressed(button):
    return button.value

# def set_color(led, color):

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



change_button = False
mute = False  # Starting value

if PROFILE == 'choose':  # A known profile can be set
    PROFILE = select_profile(profiles, rgb_led, button)  # Get the desired chat app

while True:

    # retreive the active controller button
    controller_button = profiles[PROFILE]
    if DEBUG:
        print("Profile: " + controller_button['name'])
        print("Mute: " + str(mute))

    # set the color of the onboard neopixel to match the active controller button
    if not mute:
        rgb_led[0] = controller_button['color']  # Set the LED to the chat color
    else:
        rgb_led[0] = profiles['mute']['color']  # Turn the LED red


    # detect if the button has been released
    if button_pressed(button):

        if DEBUG:
            print("{} mute button press".format(controller_button['name']))

        try:
            kbd.send(controller_button['keycode'])  # Send a one key mute command
        except TypeError as e:
            kbd.send(*controller_button['keycode'])  # Send a multi key mute command

        mute = not mute  # Toggle the boolean
        if not mute:
            rgb_led[0] = controller_button['color']  # Set the LED to the chat color
        else:
            rgb_led[0] = profiles['mute']['color']  # Turn the LED red
        time.sleep(BUTTON_LATCH_TIME)  # Give time to remove finger


    if DEBUG:
        time.sleep(1)
        print("Button Pressed: " + str(button_pressed(button)))
    else:
        time.sleep(0.1)