'''
This computes the parameters

'''

from apsg import *

orientation = Pair(131.8, 67.6, 136.63, 77.12)
w=Group.kent_lin(orientation, 3, 10, 100, name="Kent1")
print (list(w))

s = StereoNet()
s.line(w)
s.show()

