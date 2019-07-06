
# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *
import servomotorcontrol
import sunfounderservomotorcontrol


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
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
            f_return= sunfounderservomotorcontrol.movetosafe () # reset servos to safe zone
            #f_return= sunfounderservomotorcontrol.moveservos (data)
        else:
            print ("run servos")
            f_return= sunfounderservomotorcontrol.moveservos (data) #run the servos to postion in data package
          
       # print("received [%s]" % data)

        #f_return= servomotorcontrol.funcServoMotorControl (data)
       
        #print(f_return)
    
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("Service Stopped, Press button on Device to Restart Bluetooth Connection Service")

