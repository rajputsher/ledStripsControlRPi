import sys
import time
import pigpio

options = {
  'off' : [0,0,0],
  'on' : [255,255,255],
  'red' : [255,0,0],
  'green' : [0,255,0],
  'blue' : [0,0,255],
  'yellow' : [255,128,0],
  'purple' : [255,0,255],
  'orange' : [255,32,0],
  'warm' : [255,64,16],
  'cool' : [128,128,255]
}

pi = pigpio.pi()

red = 17
green = 18
blue = 27

cmd = sys.argv[1]
print cmd

rgb = options[cmd]

pi.set_PWM_dutycycle(red,rgb[0])
pi.set_PWM_dutycycle(green,rgb[1])
pi.set_PWM_dutycycle(blue,rgb[2])

