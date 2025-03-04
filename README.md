# Microphone MuteButton for Adafruit NeoKey Trinkey

## Overview
This project utilizes the [Adafruit NeoKey Trinkey](https://www.adafruit.com/product/5020) to mute your computer's microphone.  Simply plug the USB into the computer, and press the button to mute or unmute yourself!  No more hurriedly mousing to the mute/unmute button or trying to remember the hotkey for a specific chat applicaton.  

There's two ways that this program can be setup:

1.  System level microphone toggle (Recommended)
2.  Application hot-key pusher

The project originally started as just a way to select a specific chat application, and push its specific microphone hotkey, but evolved to instead utilize a system level control over the microphone.  

## Compatibility

### OS
* Windows
* MacOS
* Linux


## Setup as a system hotkey pusher

You can also enable a global microphone toggle in your computer.  This will let you toggle at the system level instead of the application level.  Basically, you don't have to be looking at the chat to mute/unmute yourself.  

### Guides for enabling a system hotkey

* [Windows](https://simplernerd.com/toggle-mute-microphone-on-windows/)
* [MacOS](https://simplernerd.com/toggle-mute-microphone-on-macos/)
* [Ubuntu / KDE Desktops](https://nikhilwanpal.in/blog/mute-mic-with-keyboard-shortcut-on-ubuntu-or-linux-mint/)

The keycombo used in this code is `WIN+SHIFT+A`, like the MS PowerToys default.  It can be changed in `profiles.py`

## Application HotKey Pusher

### Chat Applications 
* Zoom
* MS Teams
* Google Meet
* Slack
* Jitsi

It'll basically act as a hotkey specific to those applications.

**Note**: That window must be active, otherwise nothing will happen, and you will not actually be muted.

## Project Source

Project originally forked from `https://github.com/jfurcean/CircuitPython-MuteButton`

I wanted to have to have the functionality of jfurcean's Zoom mute button, but on the NeoKey Trinkey, and with some more chat profiles and on Windows.  

With the Trinkey there's no need to 3d print an enclosure.

Then I also realized that there were some limitations in just using one chat application's hotkeys (ie, `CTRL+D`), since the window has to be active, and you have to reconfigure the hotkey if you switch to a different program.  If you're looking at a different tab or window, then you don't actually mute yourself.  So I found some quick and accessible ways to disable the system microphone instead, which is the recommended way to use this program.  

## Usage

### Make the NeoKey Trinkey

#### Parts

* 1x [NeoKey Trinkey](https://www.adafruit.com/product/5020)
* 1x [Kalih Mechanical Key](https://www.adafruit.com/product/5123)
  * You can pick a different type of key if you want
* 1x [Keycap](https://www.adafruit.com/product/5068)
  * You can pick a different keycap as well.  

#### Assembly

All that's required is soldering the two pins on the mechanical key to the corresponding holes on the NeoKey Trinkey and putting on the keycap.  


#### Load Circuit Python onto the NeoKey

I recommend following the steps in the [NeoKey Learning Guide](https://learn.adafruit.com/adafruit-neokey-trinkey/overview).  There's a nice overview of the hardware, and simple instructions on where to download the correct UF2 file from as well.  Once you have a working `CIRCUITPY` drive then you are ready to move on!

### Configuring the program

There are three files from this repo that will need to be downloaded.  

1. `code.py`
2. `config.py`
3. `profiles.py`

They can be configured before or after you load them onto the NeoKey.


#### Configuring the program

As mentioned previously, you can configure this software to be used in two main different ways.  Be default, it's going to try to push a system level hot key.

In `config.py` you can select which type of OS the NeoKey is plugged into, what profile(s) the button will be using, and whether to `DEBUG` the code.  Be default, it's assuming a Windows device, and not to debug.  Debugging will display information to a REPL and drastically slow down the main loop.  

In `profiles.py` you can change the hotkeys (system or specific chat application), modify the active/mute colors, or add new profiles.  

### Load the program onto the NeoKey

Drag and drop `code.py`, `config.py` and `profiles.py` onto the `CIRCUITPY` drive.  The program should automatically start running and display the profile color listed in `config.py`.  
