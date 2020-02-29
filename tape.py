#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import time
from sys import exit
import numpy
from matrix11x7 import Matrix11x7

from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'YOUR_ADAFRUIT_KEY'
ADAFRUIT_IO_USERNAME = 'YOUR_ADAFRUIT_USERNAME'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
incoming = aio.feeds('moisture')

prev_read = "sausages"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

matrix11x7 = Matrix11x7()
matrix11x7.clear()
matrix11x7.set_brightness(0.3)

matrix = numpy.zeros((7, 11), dtype=numpy.int)

matrix[0] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[1] = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[2] = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[3] = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[4] = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[5] = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
matrix[6] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

matrix1 = numpy.zeros((7, 11), dtype=numpy.int)

matrix1[0] = [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[1] = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[2] = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[3] = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[4] = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[5] = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
matrix1[6] = [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

matrix2 = numpy.zeros((7, 11), dtype=numpy.int)

matrix2[0] = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
matrix2[1] = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
matrix2[2] = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
matrix2[3] = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
matrix2[4] = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
matrix2[5] = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
matrix2[6] = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]

matrix3 = numpy.zeros((7, 11), dtype=numpy.int)

matrix3[0] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
matrix3[1] = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
matrix3[2] = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
matrix3[3] = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
matrix3[4] = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
matrix3[5] = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
matrix3[6] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]

matrix4 = numpy.zeros((7, 11), dtype=numpy.int)

matrix4[0] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
matrix4[1] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
matrix4[2] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
matrix4[3] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
matrix4[4] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
matrix4[5] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
matrix4[6] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]

matrix5 = numpy.zeros((7, 11), dtype=numpy.int)

matrix5[0] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
matrix5[1] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
matrix5[2] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
matrix5[3] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
matrix5[4] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
matrix5[5] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
matrix5[6] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def buzz():

    GPIO.output(16,True)
    sleep(0.4)
    GPIO.output(16,False)
    sleep(0.1)
    GPIO.output(16,True)
    sleep(0.4)
    GPIO.output(16,False)

def scroll_message(message):
    matrix11x7.clear()                         # Clear the display and reset scrolling to (0, 0)
    length = matrix11x7.write_string(message)  # Write out your message
    matrix11x7.show()                          # Show the result
    time.sleep(0.5)                              # Initial delay before scrolling

    length -= matrix11x7.width

    # Now for the scrolling loop...
    while length > 0:
        matrix11x7.scroll(1)                   # Scroll the buffer one place to the left
        matrix11x7.show()                      # Show the result
        length -= 1
        time.sleep(0.02)                         # Delay for each scrolling step

    time.sleep(0.3)                              # Delay at the end of scrolling
    matrix11x7.clear() 

def tapewindow():

    matrix11x7.clear() 
    count = 0
    while (count < 5):

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix1[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix2[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix3[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix4[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix5[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix4[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix3[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix2[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        for y in range(0, 7): 
            for x in range(0, 11):
                matrix11x7.pixel(x, y, matrix1[y, x])

        matrix11x7.show()
        time.sleep(0.4)

        count = count +1
        matrix11x7.clear() 

buzz()
scroll_message(" Old Tech, New Spec    ")

while True:
    
    incoming_read = aio.receive(incoming.key)
    if incoming_read.value != prev_read:
        print(incoming_read.value)
        buzz()
        scroll_message(incoming_read.value)
        prev_read = incoming_read.value
        time.sleep(1)
    else:
        print("the same")
        tapewindow()    
    


