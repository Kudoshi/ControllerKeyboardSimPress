import pygame
import time
import ctypes
from ctypes import wintypes
import keyboard
from pynput.mouse import Button, Controller
# region Simulate key press

user32 = ctypes.WinDLL('user32', use_last_error=True)
INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
MAPVK_VK_TO_VSC = 0

wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg", wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))

    _anonymous_ = ("_input",)
    _fields_ = (("type", wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    return time.time()


def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    return time.time()

def pressKey(key, timeDelay):
    firstSec = PressKey(key)
    time.sleep(timeDelay)
    secSec = ReleaseKey(key)
    latency = secSec - firstSec
    if runLatency:
        print("      > Latency: ", latency)
    # you can change 0x30 to any key you want. For more info look at :
    # msdn.microsoft.com/en-us/library/dd375731
# endregion

'''
A simple program to use controller to simulate keyboard key press. Can bypass some games' anti-simulate key press.

Default Start/pause program: Ctrl+q

Replace the '0x44' with the appropriate hexadecimal 
Format: '0x' 
Look below for the keycode https://www.csee.umbc.edu/portal/help/theory/ascii.txt

Check documentation/readme for the appropriate button value/event
'''



#region CONFIG
releaseDelay = 0.008 #Press-release key delay. Some game needs higher delay to work.

runLatency = False #Latency check test. From key press to release key latency
#endregion CONFIG

playMode = False
pygame.init()
print("_"*70,"\n")

#INITIALIZE JOYSTICK
if pygame.joystick.get_count() == 0:
    print("[ERROR JOYSTICK] Joystick not found. Please try again")
    quit()
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("[JOYSTICK INIT] Joystick initialized")

#MAIN LOOP
while True:
    events = pygame.event.get()

    #Start/Pause program. Change if needed.
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
        playMode = not playMode
        if playMode:
            print("[PROGRAM STARTED] Program start.")
        else:
            print("[PROGRAM PAUSED] Program paused.")
        time.sleep(0.3)

    for event in events:
        if playMode:

            #CHANGE KEYCODE OVER HERE.

            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(10): #<-- change button value
                    print("Pressed L1")
                    #Change 0x46 to relevent hexadecimal keycode of the key
                    pressKey(0x46, releaseDelay) #<-------
                if joystick.get_button(9):
                    print("Pressed R1")
                    pressKey(0x44, releaseDelay)
                if joystick.get_button(2):
                    print("Pressed square")
                    pressKey(0x44, releaseDelay)

                if joystick.get_button(1):
                    print("Pressed O")
                    pressKey(0x46, releaseDelay)





