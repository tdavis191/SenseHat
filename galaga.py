from sense_hat import SenseHat
from keyboard import *
sense = SenseHat()
sense.clear()
sense.set_pixel(4, 7, (255, 0, 0))
sense.set_pixel(3, 7, (255, 0, 0))

while True:
    try:
        if keyboard.is_pressed('w'):
            print('You Pressed A Key')
            break      
        else:
            skip
