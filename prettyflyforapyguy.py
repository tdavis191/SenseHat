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
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, w]
    ]
rtmstfr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rtmstfr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rtmstfr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rtmstfr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rtmstfr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rtmstfr7= [
    [r, r, r, r, r, r, r, g],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w]
    ]


rt2fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]


rt2fr7= [
    [r, r, r, r, r, r, g, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r]
    ]





most_recent = bg
while True:
    for event in sense.stick.get_events():
        if event.direction == "right":
            if most_recent == rightmost:
                pass
            elif most_recent == right2:
                most_recent = rightmost
            elif most_recent == right3:
                most_recent = right2
            elif most_recent == right4:
                most_recent = right3
            elif most_recent == left4:
                most_recent = right4
            elif most_recent == left3:
                most_recent = left4
            elif most_recent == left2:
                most_recent = left3
            elif most_recent == leftmost:
                most_recent = left2
        if event.direction == "left":
            if most_recent == leftmost:
                pass
            elif most_recent == left2:
                most_recent = leftmost
            elif most_recent == left3:
                most_recent = left2
            elif most_recent == left4:
                most_recent = left3
            elif most_recent == right4:
                most_recent = left4
            elif most_recent == right3:
                most_recent = right4
            elif most_recent == right2:
                most_recent = right3
            elif most_recent == rightmost:
                most_recent = right2
        if event.direction == "up":
            if most_recent == rightmost:
                pass
            elif most_recent == right2:
                most_recent = rightmost
            elif most_recent == right3:
                most_recent = right2
            elif most_recent == right4:
                most_recent = right3
            elif most_recent == left4:
                most_recent = right4
            elif most_recent == left3:
                most_recent = left4
            elif most_recent == left2:
                most_recent = left3
            elif most_recent == leftmost:
                most_recent = left2
        
    sense.set_pixels(sum(most_recent,[]))






















































































































