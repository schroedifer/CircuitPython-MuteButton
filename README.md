# Microphone MuteButton for Adafruit NeoKey Trinkey

## Overview

This project utilizes the [Adafruit NeoKey Trinkey](https://www.adafruit.com/product/5020) to mute your computer's microphone.  Simply plug the USB into the computer, and press the button to mute your microphone!  No more hurriedly mousing to the mute/unmute button or trying to remember the hotkey for a specific chat applicaton.  

There's two ways that this program can be setup:

1.  Application hot-key pusher
2.  System level microphone toggle

The project originally started as just a way to select a specific chat application, and push its specific microphone hotkey, but evolved to instead utilize a system level control over the microphone.  

## Compatibility

### OS
* Windows
* MacOS
* Linux



### Chat Applications
* Zoom
* MS Teams
* Google Meet
* Slack
* Jitsi

It'll basically act as a hotkey specific to those applications.

**Note**: That window must be active, otherwise nothing will happen.

## Setup as a system hotkey pusher

You can also enable a global microphone toggle in your computer.  This will let you toggle at the system level instead of the application level.  Basically, you don't have to be looking at the chat to mute/unmute yourself.  

### Guides for enabling a system hotkey

* [Windows](https://simplernerd.com/toggle-mute-microphone-on-windows/)
* [MacOS](https://simplernerd.com/toggle-mute-microphone-on-macos/)
* [Ubuntu](https://nikhilwanpal.in/blog/mute-mic-with-keyboard-shortcut-on-ubuntu-or-linux-mint/)

The keycombo used in this code is `WIN+SHIFT+A`, like the MS PowerToys default.  It can be changed in `profiles.py`

## Project Source

Project originally forked from `https://github.com/jfurcean/CircuitPython-MuteButton`

I wanted to have to have th functionality of jfurcean's Zoom mute button, but on the NeoKey Trinkey, and with some more chat profiles and on Windows.  

With the Trinkey there's no need to 3d print an enclosure.

I also realized that there were some limitations in just using one chat application's hotkeys (ie, `CTRL+D`), since the window has to be active, and you have to reconfigure if you switch to a different program.  If you're looking at a different tab or window, then you don't actually mute yourself.  So I found some quick and accessible ways to disable the system microphone instead, which is the recommended way to use this program.  

## Usage

### Make the NeoKey Trinkey

### Configure the program

### Load the program
