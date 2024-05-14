#!/usr/bin/python3

from gpiozero import Button
from time import sleep
from os import system, getuid
from sys import stdout, exit


stopPin = 22
stopButton = Button(stopPin) # defines the button as an object and chooses GPIO pin


def isRoot():
    if getuid() != 0:
        return False
    else:
        return True


def main():
    print("\nMonitoring pin {} for reboot signal.".format(stopPin))
    print("Ctrl-C to quit.\n")

    pressCounter = 0
    
    try:
        while (True):
            if stopButton.is_pressed:
                pressCounter += 1
            else:
                pressCounter = 0
                
            if pressCounter > 10:
                system("shutdown now -r")
                
            sleep(0.1)

    except KeyboardInterrupt:
        print('\n\nKeyboard interrupt.')

    finally:
        pass

    return


if __name__ == "__main__":
    if not (isRoot()):
        print("\nScript must be run as root.")
        exit(1)
    else:
        main()
        exit(0)