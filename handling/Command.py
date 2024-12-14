print("Hello World!") # type: ignore

import usb_hid # type: ignore
import time
from adafruit_hid.mouse import Mouse # type: ignore
from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from handling.Input import Input

kbd = Keyboard(usb_hid.devices)

# kbd.send(9)

class Command:
    speed = 0

    def rem(args):
        print(' '.join(args))

    def string(args):
        print('found string cmd')
        # str = ' '.join(args)
        # print(str)

        print(kbd.led_on(Keyboard.LED_CAPS_LOCK))

        if kbd.led_on(Keyboard.LED_CAPS_LOCK):
            Command.press(["CAPSLOCK"])

        for i in range(len(args)):
            word = args[i]

            # print(i)
            print(word)
            if i != 0:
                # print('insterting space')
                kbd.send(Keycode.SPACE)
                        
            for j, char in enumerate(word):
                print('char asdsad')
                # print(j);
                # print(getattr(Keycode, char.upper()))
                print('typespeed', Command.speed)
                Input.inputKeycode(kbd, char, Command.speed)
                # kbd.send(getattr(Keycode, char.upper()))

    def delay (args):
        time.sleep(int(args[0])/1000)

    def typespeed (args):
        print("command typespeed")
        print(int(args[0]))
        Command.speed = int(args[0])/1000
    
    def wait_for (args):
        print("waiting for " + args[0])
        ledName = "LED_" + args[0]
        print(kbd.led_on(getattr(Keyboard, ledName)))
        initState = kbd.led_on(getattr(Keyboard, ledName))
        while initState == kbd.led_on(getattr(Keyboard, ledName)):
            print(kbd.led_on(getattr(Keyboard, ledName)))
            time.sleep(0.1)

    def press (args):
        print("press command")
        for key in args:
            if len(key) == 1:
                key.lower()
            Input.pressKey(kbd, key)

    def release (args=[]):
        kbd.release_all()

    def hotkey (args):
        Command.press(args)
        Command.release()

    def execute (path):
        with open(path, "r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                line = line.strip().split()
                print(line)
                if (len(line) != 0):
                    cmd = line[0]
                    print('cmd', cmd.lower())
                    try:
                        getattr(Command, cmd.lower())(line[1:])
                    except:
                        print('error with ' + cmd) 
                line = file.readline()
                

