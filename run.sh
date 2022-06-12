#!/bin/bash

CYCLE_PERIOD_MS=30000
IMAGE_DIRECTORY="/path/to/images" #Images go here
ON_TIME_HOUR=10
OFF_TIME_HOUR=20
BACKLIGHT=0

echo "Running tkinter raspberry pi slideshow application"

python3 photos.py $CYCLE_PERIOD_MS $IMAGE_DIRECTORY $ON_TIME_HOUR $OFF_TIME_HOUR $BACKLIGHT
