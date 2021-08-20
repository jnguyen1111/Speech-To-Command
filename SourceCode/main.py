import pydirectinput
import speech_recognition
import time
import pyaudio
import sys
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

def command_left(keys_pressed):
    pydirectinput.moveRel(-325 , 0 , relative=True)

def command_right(keys_pressed):
    pydirectinput.moveRel(325 , 0 , relative=True)

def command_up(keys_pressed):
    pydirectinput.moveRel(0 , -150 , relative=True)

def command_down(keys_pressed):
    pydirectinput.moveRel(0, 150 , relative=True)

#make some for movement keys

def walk(keys_pressed):
    pydirectinput.keyDown("w")
    keys_pressed.append("w")

def jump(keys_pressed):
    pydirectinput.keyDown("space")
    keys_pressed.append("space")

def look_back(keys_pressed):
    pydirectinput.moveRel(600 , 0 , relative=True)

def drop(keys_pressed):
    pydirectinput.press("q")

def shift(key_pressed):
    #to do add a flag variable for this
    pydirectinput.keyDown("shift")

    # if(not (player_crouched)):
    #     pydirectinput.keyDown("shift")
    #     player_crouched = True
    # else:
    #     pydirectinput.keyUp("shift")
    #     player_crouched = False

def stop(keys_pressed):
    for key in range(len(keys_pressed)):
        pydirectinput.keyUp(keys_pressed[key])
    keys_pressed.clear()

def left_click(keys_pressed):
    pydirectinput.leftClick()

def right_click(keys_pressed):
    pydirectinput.rightClick()

def teabag(keys_pressed):
    for times in range(0,2):
        pydirectinput.press("f5")

    for times in range(0,3):
        pydirectinput.keyDown("shift")
        time.sleep(.3)
        pydirectinput.keyUp("shift")

    time.sleep(.3)
    pydirectinput.press("f5")

def run(keys_pressed):
    pydirectinput.keyDown("w")
    pydirectinput.keyDown("r")
    keys_pressed.append("w")
    keys_pressed.append("r")

def inventory(keys_pressed):
    pydirectinput.press("e")

def quit_program(keys_pressed):
    sys.exit()

def press_number_key(command):
    pydirectinput.press(command)

def move_forward(keys_pressed):
    pydirectinput.keyDown("w")
    time.sleep(1)
    pydirectinput.keyUp("w")

def move_backward(keys_pressed):
    pydirectinput.keyDown("s")
    time.sleep(1)
    pydirectinput.keyUp("s")

def move_left(keys_pressed):
    pydirectinput.keyDown("a")
    time.sleep(1)
    pydirectinput.keyUp("a")

def move_right(keys_pressed):
    pydirectinput.keyDown("d")
    time.sleep(1)
    pydirectinput.keyUp("d")

number_commands = ["1","2","3","4","5","6","7","8","9","0"]

voice_commands = {"look left":command_left , "look right":command_right , "look up": command_up , "look down": command_down ,
                  "walk":walk , "quit":quit_program , "run":run , "stop":stop , "jump":jump , "left-click":left_click,
                  "inventory":inventory , "right-click":right_click , "sneak":shift,"drop":drop,"look back":look_back,
                  "tea bag":teabag, "move forward":move_forward,"move backward":move_backward , "move left": move_left,
                  "move right": move_right}
keys_pressed = []

#slow down your speech for more accurate detection

def voice_listener():
    while(True):
        with sr.Microphone() as source:
            print("\nSay something!")
            audio = r.listen(source, phrase_time_limit = 1.80)
        try:
            command = r.recognize_google(audio ,language="en-US").lower()
            print("User said: {}".format(command))
            if command in voice_commands:
                voice_commands[command](keys_pressed)
            elif command in number_commands:
                press_number_key(command)
        except speech_recognition.UnknownValueError:
            print("Google didnt get that try again")
        except speech_recognition.RequestError:
            print("Google services did not work try again")

if __name__ == "__main__":
    player_crouched = False
    voice_listener()





