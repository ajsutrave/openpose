from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
import tkinter
from time import sleep

pin_factory=PiGPIOFactory(host='192.168.1.216')

class RemoteFingerServo(AngularServo):
    def __init__(self, gpio, pin_factory, min_angle=0, max_angle=100,):
        super(RemoteFingerServo,self).__init__(gpio,
                                               pin_factory=pin_factory,
                                               min_angle=min_angle,
                                               max_angle=max_angle)
    def set_angle(self, val, debug=False):
        self.angle = int(val)
        if debug: print( "Servo angle: ", servo1.angle, "Val:", val)



servos = [
    RemoteFingerServo(18, pin_factory=pin_factory), #ring, orange
    RemoteFingerServo(17, pin_factory=pin_factory), #thumb, yellow (inverted)
    # RemoteFingerServo(27, pin_factory=pin_factory), #middle, green
    # RemoteFingerServo(12, pin_factory=pin_factory), #
    # RemoteFingerServo(13, pin_factory=pin_factory),
]

root = tkinter.Tk()
for servo in servos:
    scale = tkinter.Scale(orient='horizontal',
                          from_=servo.min_angle, to=servo.max_angle,
                          command=servo.set_angle)
    scale.set(servo.max_angle)
    scale.pack()

root.mainloop()

for servo in servos: servo.detach()
