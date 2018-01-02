### controller-reader.py -- Andrew R Gross -- 2017-11-12

import serial
import pygame
import time

serialPort = '/dev/ttyUSB0' 
baudRate = 9600

### Gets joystick data and prints it
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' % j.get_name()

### Open Serial Connection to Arduino Board
ser = serial.Serial(serialPort, baudRate, timeout=1);

axis_check_list = [1,3]
axis_history =  ['0','0']

try:
    while True:
        pygame.event.pump()
        for h in range(0,2):
            i = axis_check_list[h]

            if j.get_axis(i) != 0.00:
                print 'Axis %i reads %.2f' % (i, j.get_axis(i))
            new_value = str(int(round(j.get_axis(i)*100,2)+100))
            axis_history[h] = new_value
            serialOutput = ','.join(axis_history) + ';'
            print(serialOutput)
            ser.write(serialOutput)
        time.sleep(0.2)

except KeyboardInterrupt:
    j.quit()
