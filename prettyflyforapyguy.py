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
rtmost= [
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
rt3fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt3fr7= [
    [r, r, r, r, r, g, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r]
    ]
rt4fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
rt4fr7= [
    [r, r, r, r, g, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, w, r, r, r]
    ]
lft4fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft4fr7= [
    [r, r, r, g, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, w, r, r, r, r]
    ]
lft3fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr6= [
    [r, r, r, r, r, r, r, r],
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft3fr7= [
    [r, r, g, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, w, r, r, r, r, r]
    ]
lft2fr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr6= [
    [r, r, r, r, r, r, r, r],
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lft2fr7= [
    [r, g, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, w, r, r, r, r, r, r]
    ]
lftmstfr1= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr2= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr3= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr4= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr5= [
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr6= [
    [r, r, r, r, r, r, r, r],
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
lftmstfr7= [
    [g, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, r],
    [w, r, r, r, r, r, r, r]
    ]
most_recent = start
while True:
    for event in sense.stick.get_events():
        if event.direction == "right":
            if most_recent == rtmost:
                pass
            elif most_recent == right2:
                most_recent = rtmost
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
            if most_recent == rtmost:
                most_recent = rtmstfr1
                most_recent = rtmstfr2
                most_recent = rtmstfr3
                most_recent = rtmstfr4
                most_recent = rtmstfr5
                most_recent = rtmstfr6
                most_recent = rtmstfr7
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






















































































































