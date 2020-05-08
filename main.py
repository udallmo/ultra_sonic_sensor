import serial
from vpython import *

arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)
measuringRod = cylinder( length = 6, color = color.yellow, radius= 0.1, pos= vector(-3, -2, 0))
lengthLabel = label(text = "Target Distance is: ", pos= vector(0, 3, 0), height = 30, box = False)
target = box( color = color.green, length = 0.2, width = 3,height = 3, pos= vector(0, -0.5, 0))

while (True):
    rate(20)

    if (arduinoSerialData.inWaiting() > 0):
        data = arduinoSerialData.readline().decode('utf-8')
        distance = float(data)
        print(distance)
        label = 'Target Distance is ' + data
        lengthLabel.text = label
        target.pos = vector(distance-3, -0.5, 0)
        measuringRod.length= distance
