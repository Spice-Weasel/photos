
import os

class Screen:
    def __init__(self):
        print("screen module initiailized")
        self.brightness_interface = "/sys/class/backlight/rpi_backlight/brightness"
        self.is_on = True

    def change_brightness(self, value) -> bool:
        """write an uint8 value to brightness interface"""
        with open(self.brightness_interface, 'w') as f:
            f.seek(os.SEEK_END)
            pos = f.tell()
            f.truncate(pos)
            f.write(str(value))
            return True

    @property
    def is_on(self) -> bool:
        return self.__is_on

    @is_on.setter
    def is_on(self, value : bool) -> bool:
        if type(value) is not bool:
            raise TypeError
        self.__is_on = value
        return self.__is_on
        



if __name__ == "__main__":
    print("Running test on screen brightness")
    s = Screen()
    s.change_brightness(100)