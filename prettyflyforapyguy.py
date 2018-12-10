from sense_hat import SenseHat
from time import *
sense = SenseHat()
sense.clear()
sense.set_pixel(4, 7, (255, 0, 0))
sense.set_pixel(3, 7, (255, 0, 0))

r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)


bg= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r]
    ]

sense.set_pixels(sum(bg,[]))


start= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
leftmost = [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
left2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
left3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
left4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
right4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
right3 = [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
right2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]
rightmost= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]
rtmstfr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w],
    [r, r, r, r, r, r, r, w]
    ]


most_recent = bg
while True:
    for event in sense.stick.get_events():
        if event.direction == "right":
            print('Working')
        most_recent == right3
    sense.set_pixels(sum(most_recent,[]))
