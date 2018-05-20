import keyboard
import time
import sys


def main():
    hook_id = keyboard.hook(print_real_time_input)
    time.sleep(30)
    keyboard.unhook(hook_id)


def print_real_time_input(event):
    print(event.name)


if __name__ == "__main__":
    main()
