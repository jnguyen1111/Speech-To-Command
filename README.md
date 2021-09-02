# SpeechToMovementMinecraft

# Table of Contents:
 - [Installation](#Installation)
 - [Description](#Description)
 - [Commands](#Commands)
 - [License](#Liscense)
 
# Installation
In order for the program to  work, the following requirements are needed below
   * extra modules (pydirectinput, time, sys, speech_recognition, pyaudio, pyautogui)
   * a microphone to detect speech, needs to be configured to elimate background noise to make google's speech api more percise

# Description
 movement based controlled by speech based on minecrafts keyboard input and mouse movement
 
# Commands
The program features these keyboard and mouse input commands by speech
   * "look left": turns the player's camera to the left using the mouse input
 * "look right": turns the player's camera to the right using the mouse input
 * "look down": turns the player's camera down using mouse input
 * "look up": turns the player's camera up using mouse input
 * "look back": turns the player's camera 180 degrees using mouse input
 * "move forward": holds down the w key on the keyboard for 1 second and then releases the w key
 * "move backward": holds down the s key on the keyboard for 1 second and then releases the s key
 * "move left": holds down the a key on the keyboard for 1 second and then releases the a key
 * "move right": holds down the d key on the keyboard for 1 second and then releases the d key
 * "crouch": holds down the shift key, if the command is called again, the it releases the shift key
 * "walk": holds down the w key
 * "run": holds down the w key and the r key which should be binded as run
 * "jump": holds the spacebar key down
 * "left hold": hold down the left click of the mouse input
 * "right hold": hold down the right click of the mosue input
 * "left click": left click from the mouse input
 * "right click": right click from the mouse input
 * "inventory": presses the e key to open inventory. Note that the user should bind inventory to e
 * "0/1/2/3/4/5/6/7/8/9": accesses the hotkey slot that the player has
 * "drop": presses the q key on the keyboard to drop current hotkey slot
 * "stop": releases all the keys / mouse input and resets to having no keyboard or mouse buttons clicked
 
# License
Released under the Mit License

