import pydirectinput
import time
import sys
import speech_recognition
import pyaudio
import pyautogui

class character_movement:
    # left to down for looking defines mouse relative positioning and where to move in pixels
    def look_left(self):
        pydirectinput.moveRel(-1500, 0, relative=True)

    def look_right(self):
        pydirectinput.moveRel(1500, 0, relative=True)

    def look_up(self):
        pydirectinput.moveRel(0, -450, relative=True)

    def look_down(self):
        pydirectinput.moveRel(0, 450, relative=True)

    #looks back 180 degrees
    def look_back(self):
        pydirectinput.moveRel(3250, 0, relative=True)

    def move_forward(self):
        pydirectinput.keyDown("w")
        time.sleep(1)
        pydirectinput.keyUp("w")

    def move_backward(self):
        pydirectinput.keyDown("s")
        time.sleep(1)
        pydirectinput.keyUp("s")

    def move_left(self):
        pydirectinput.keyDown("a")
        time.sleep(1)
        pydirectinput.keyUp("a")

    def move_right( self):
        pydirectinput.keyDown("d")
        time.sleep(1)
        pydirectinput.keyUp("d")

    #key press for crouching
    def shift(self):
        if not (self.player_crouched):
            pydirectinput.keyDown("shift")
            self.player_crouched = True
        else:
            pydirectinput.keyUp("shift")
            self.player_crouched = False

    # holds down walk key continously
    def walk(self,keys_pressed):
        pydirectinput.keyDown("w")
        self.keys_pressed.append("w")

    def run(self,keys_pressed):
        pydirectinput.keyDown("w")
        pydirectinput.keyDown("r")
        self.keys_pressed.append("w")
        self.keys_pressed.append("r")

    def jump(self,keys_pressed):
        pydirectinput.keyDown("space")
        self.keys_pressed.append("space")

    #press left mouse button and hold
    def left_click_hold(self):
        pyautogui.mouseDown()

    #press right mouse button and hold
    def right_click_hold(self):
        pyautogui.mouseDown(button="right")

    #press left mouse button once
    def left_click(self):
        pydirectinput.leftClick()

    #press right mouse button once
    def right_click(self):
        pydirectinput.rightClick()

    #opens up the players inventory with items they have
    def inventory(self):
        pydirectinput.press("e")

    #defines inventory number to switch to
    def press_number_key(self,command):
        pydirectinput.press(command)

    #drops  current hotkey item
    def drop(self):
        pydirectinput.press("q")

    #takes list of keys pressed and cancels it and unpresses the keys
    def stop(self,keys_pressed):
        for key in range(len(self.keys_pressed)):
            pydirectinput.keyUp(self.keys_pressed[key])
        self.keys_pressed.clear()
        pyautogui.mouseUp(button="right")
        pyautogui.mouseUp()

    def exit_program(self):
        sys.exit()

    #takes input from microphone and throws the audio source into googles speech api to text and calls for commands
    def voice_listener(self):
        while (True):
            with self.speech_recognition.Microphone() as source:                            #gets microphone device/input
                print("\nSay something!")
                recording = self.audio.record(source, duration=3)                           #records audio for duration of three seconds
            try:
                command = self.audio.recognize_google(recording, language="en-US").lower()  #throw the recording into google speech api and get text back
                print("User said: {}".format(command))
                if command in self.run_walk_jump:                                           #check if the command are in dictionaries take value and form/call function
                    self.run_walk_jump[command](self.keys_pressed)
                elif command in self.voice_commands:
                    self.voice_commands[command]()
                elif command in self.number_commands:
                    self.press_number_key(command)
            except self.speech_recognition.UnknownValueError:
                print("Google didnt get that try again")
            except self.speech_recognition.RequestError:
                print("Google services did not work try again")

    def start_program(self):
        for seconds in range(3, 0, -1):
            print("Starting program in {}".format(seconds))
            time.sleep(1)
        self.voice_listener()

    def __init__(self):
        self.player_crouched = False                                                        #checks to see if the player is crouched or not
        self.speech_recognition = speech_recognition
        self.audio = self.speech_recognition.Recognizer()                                   #sets up audio settings for recording
        self.number_commands = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]           #this is for inventory slot number in minecraft
        self.keys_pressed = []                                                              #records key input so that when stop is called all keys are unpressed
        self.run_walk_jump = { "walk": self.walk , "jump": self.jump , "run": self.run}     #these commands add to keys_pressed list which is seperated from voice_commands
        self.voice_commands = {"look left": self.look_left, "look right": self.look_right,
                               "look up": self.look_up, "look down": self.look_down,
                                "exit program": self.exit_program,"stop": self.stop,
                               "left-click": self.left_click,"inventory": self.inventory,
                               "right-click": self.right_click,"couch": self.shift,
                               "drop": self.drop, "look back": self.look_back,
                               "forward": self.move_forward,
                               "backward": self.move_backward, "left": self.move_left,
                               "right": self.move_right ,"left hold":self.left_click_hold,
                               "right hold":self.right_click_hold}
        self.start_program()

if __name__ == "__main__":
    player = character_movement()





