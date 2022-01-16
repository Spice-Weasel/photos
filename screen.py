
import os

class Screen:
    def __init__(self):
        print("screen module initiailized")
        self.brightness_interface = "/sys/class/backlight/rpi_backlight/brightness"

    def change_brightness(self, value) -> bool:
        """write an uint8 value to brightness interface"""
        with open(self.brightness_interface, 'w') as f:
            f.seek(os.SEEK_END)
            pos = f.tell()
            f.truncate(pos)
            f.write(str(value))



if __name__ == "__main__":
    print("Running test on screen brightness")
    s = Screen()
    s.change_brightness(100)