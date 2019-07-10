# Bluetooth connection Function:
from bluetooth import *
import sunfounderservomotorcontrol
import time
servo0_currentposition=0
def managebtconnection():
    # file: bt_server_motor_control.py
    # auth: John Zawodniak
    # desc: a server app that uses RFCOMM socket
    # to communicate serially
    server_sock=BluetoothSocket(RFCOMM)
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

    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0: break # test to see if data package is empty

            if data .startswith( b'sz' ):
                print ("move to save zone")
                f_return= movetosafe () # reset servos to safe zone
                #f_return= sunfounderservomotorcontrol.moveservos (data)
            else:
                print ("run servos")
                f_return= getangleadjustment (data) #run the servos to postion in data package

           # print("received [%s]" % data)

            #f_return= servomotorcontrol.funcServoMotorControl (data)

            #print(f_return)

    except IOError:
        pass

    print("disconnected")

    client_sock.close()
    server_sock.close()
    print("Service Stopped, Press button on Device to Restart Bluetooth Connection Service")


def getangleadjustment(n):
    # reset the variables
    dataIn = None; last_s = None; servo_num = None; rawAngle = None; corrected_angle = None

    dataIn = str(n, 'utf-8')
    last_s = dataIn.rfind('s') + 1#find position of last 's' in string
    servo_num = dataIn[int(last_s - 1) : int(last_s + 1)] #extract the servo num
    rawAngle = dataIn[int((last_s + 2) - 1) : ]# extract the raw angle number
    corrected_angle = int(float(rawAngle)) # clean the angle
    f_return=moveservos (servo_num,corrected_angle)




def movetosafe():
    sunfounderservomotorcontrol.Servo(0).write(90)
    time.sleep(1)
    servo0_currentposition=90

def moveservos(servo_num, corrected_angle):
    '''Servo driver test on channel 1'''



    a = sunfounderservomotorcontrol.Servo(0)
    a.setup()
    speed=0.06
    movementsize=1
    currentposition = servo0_currentposition
    #desiredposition = 0
    desiredposition = corrected_angle

    if desiredposition > currentposition:
        for i in range(currentposition, desiredposition+1, movementsize):
            print (i)
            a.write(i)
            time.sleep(speed)

    if desiredposition < currentposition:
       for i in range(currentposition, desiredposition, -movementsize):
            print (i)
            a.write(i)
            time.sleep(speed)

    servo0currentpostion=desiredposition
    print (servo0currentpostion)
    #print (i)




if __name__ == '__main__':
        managebtconnection()


