print("Hello World!") # type: ignore

import usb_hid # type: ignore
import time
from adafruit_hid.mouse import Mouse # type: ignore
from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from handling.Input import Input

kbd = Keyboard(usb_hid.devices)

kbd.send(Keycode.GUI)

class Command:

    typespeed = 0

    def rem(args):
        print(' '.join(args))

    def string(args):
        print('found string cmd')
        # str = ' '.join(args)
        # print(str)

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
                print('typespeed', Command.typespeed)
                Input.inputKeycode(kbd, char, Command.typespeed)
                # kbd.send(getattr(Keycode, char.upper()))

    def delay (args):
        time.sleep(int(args[0])/1000)

    def typespeed (args):
        print("command typespeed")
        print(int(args[0]))
        Command.typespeed = int(args[0])

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
                cmd = line[0]
                print('cmd', cmd.lower())
                try:
                    getattr(Command, cmd.lower())(line[1:])
                except:
                    print('error with ' + cmd) 
                line = file.readline()
