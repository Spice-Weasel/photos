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

        self.image = NewType('image', ImageTk.Image)
        self.image = ImageTk.PhotoImage(Image.open(photos_directory + self.store.next()))
        
        self.display = tk.Label(self.window)
        self.display.pack(fill=tk.BOTH)
        self.display.configure(image = self.image)

    def increment_image(self):
        """Get the next image in the directory and
        update the display, call self again in 2000"""
        self.image = ImageTk.PhotoImage(Image.open(photos_directory + self.store.next()))
        self.display.configure(image = self.image)
        self.window.after(2000, self.increment_image)



if __name__ == "__main__":
    app = Application()
    app.increment_image()
    app.window.mainloop()

