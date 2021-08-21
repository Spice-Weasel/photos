"""
This is a program that will cycle through a directory of
photos and display them on screen
"""

import os
from time import sleep
import tkinter as tk
from PIL import Image
from PIL import ImageTk

from typing import List
from typing import Tuple
from typing import NewType

from re import split

photos_directory = '/home/ingram/Pictures/waifus/'

class ImageStore:
    def __init__(self, directory):
        self.dir = directory
        self.image_paths, self.number_of_images = self.get_paths()
        self.index = 0

    def get_paths(self) -> Tuple[List[str], int]:
        images: List[str]
        images = os.listdir(self.dir)
        return images, len(images)

    def next(self, random: bool = False) -> str:
        if self.index >= (self.number_of_images - 1):
            self.index = 0
        else:
            self.index += 1

        return self.image_paths[self.index]

class Application:
    def __init__(self):
        """Setup the user interface here
        and initialize any dependent classes here
        """
        self.store = ImageStore(photos_directory)

        self.window = tk.Tk()
        self.window.title("Photos")
        self.window.attributes("-fullscreen", True)

        self.display = tk.Label(self.window)
        self.display.pack(fill=tk.BOTH)

        self.window.update()

    def increment_image(self):
        """Get the next image in the directory and
        update the display, call self again in 2000"""
        self.image = Image.open(photos_directory + self.store.next())
        self.scale_image(self.image)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.display.configure(image = self.photo_image)
        self.window.after(2000, self.increment_image)

    def scale_image(self, image) -> ImageTk:
        """Get the size of the tkinter window - this
        will allow opened images to be scaled accordingly
        """
        window_size_raw = self.window.geometry()
        print(window_size_raw)
        window_size = split("[x+]", window_size_raw)
        image_size = image.size

        self.image_scaling_factor = int(window_size[1])/image.size[1]

        print(window_size)
        print(image.size)
        print(self.image_scaling_factor)

        x_size = int(self.image_scaling_factor * image_size[0])
        y_size = int(self.image_scaling_factor * image_size[1])

        try:
            self.image = image.resize((x_size, y_size))
        except ValueError:
            pass



if __name__ == "__main__":
    app = Application()
    app.increment_image()
    app.window.mainloop()

