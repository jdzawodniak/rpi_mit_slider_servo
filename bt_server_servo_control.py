# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *
import ServerMotorControl
import time
from adafruit_servokit import ServoKit


def funct_parse_BT_comm (n):
        # only accepts numbers from control app. strip out string chars.
    # x= str(n, 'utf-8')  # converts bytes to string
    c = None
    i = None
    desiredposition = None
    servonum = None
    c = int(n)  # converts bytes to int
    for i in range(1, 10):
        if c >= i * 1000 and c <= i * 1000 + 180:
            desiredposition = c - i * 1000
            print(''.join([str(x) for x in [c, ' is between ', i * 1000, ' and ', i * 1000 + 180]]))
            print('The desired angle is: ')
            print(desiredposition)
            servonum = i
            print('The servo number is: ')
            print(i)
            break

    return(servonum, desiredposition)

def funcServoMotorControl (servonum, desiredposition, movementsize,currentposition):
    #do something with motor
    # initialize servocurrent positions.
    #set servo 1 initial position
    kit = ServoKit(channels=8)

    print ("motor function open")
    stepsrequired = abs(desiredposition-currentposition)
    adjustedsteps = stepsrequired // movementsize
    for count in range(int(adjustedsteps)):
        if currentposition < desiredposition:
            currentposition = currentposition + movementsize
        else:
            currentposition = currentposition - movementsize

        kit.servo[0].angle = currentposition
        time.sleep(.04)
        print(currentposition)
    return (currentposition)



#################################################
# start Bluetooth connection and monitor for data
#################################################
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                    )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)
kit = ServoKit(channels=8)
servo1currentposition = 90
#kit.servo[0].angle = servo1currentposition


try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
        #parse out incoming data into individual parts
        servonum,f_desiredposition=funct_parse_BT_comm (data)
        movementsize = 2
        print(servonum)
        if servonum == 1:
            currentposition = servo1currentposition
        print(f_desiredposition)
        print(servo1currentposition)



        # call motor control for movement
        f_return=funcServoMotorControl (servonum, f_desiredposition, movementsize, currentposition)
            #f_return= ServerMotorControl.funcServoMotorControl (data)
        #print(f_return)
        print(f_return)
        print(currentposition)

        if servonum == 1:
            servo1currentposition = f_return
            print (servo1currentposition)
        if servonum == 2:
            servo2currentposition = currentposition
        if servonum == 3:
            servo3currentposition = currentposition
        if servonum == 4:
            servo4currentposition = currentposition
        if servonum == 5:
            servo5currentposition = currentposition
        if servonum == 6:
            servo6currentposition = currentposition



except IOError:
    pass
print("disconnected")

client_sock.close()
server_sock.close()
print("Service Stopped, Press button on Device to Restart Bluetooth Connection Service")
