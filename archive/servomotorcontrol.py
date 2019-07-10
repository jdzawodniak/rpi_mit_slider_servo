import time
from adafruit_servokit import ServoKit

# Motor control function
# Button control value passed in. Pins set high or low depending on value.
# Action complete status passed back to calling module
kit = ServoKit(channels=16)
# motor control function
def funcServoMotorControl (n):
     # only accepts numbers from control app. strip out string chars.
     
     
     dataIn = None
     last_s = None
     servo_num = None
     rawAngle = None
     corrected_angle = None
     
     dataIn = str(n, 'utf-8')
     last_s = dataIn.rfind('s') + 1
     servo_num = dataIn[int(last_s - 1) : int(last_s + 1)]
     rawAngle = dataIn[int((last_s + 2) - 1) : ]
     
     corrected_angle = int(float(rawAngle))

     c = corrected_angle 
     print(servo_num) 
     if servo_num == 's6':
        kit.servo[6].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
     if servo_num == 's5':
        kit.servo[5].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
     if servo_num == 's4':
        kit.servo[4].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
     if servo_num == 's3':
        kit.servo[3].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
     if servo_num == 's2':
        kit.servo[2].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
     if servo_num == 's1':
        kit.servo[1].angle = corrected_angle
        kit.continuous_servo[1].throttle = 1
        time.sleep(1) 
        print ("grip")
        print(corrected_angle)
           
          
           
      
 

               

     
     #kit.servo[0].angle = 180
     #kit.continuous_servo[1].throttle = 1
     #time.sleep(1)
     #kit.continuous_servo[1].throttle = -1
    # time.sleep(1)
   #  kit.servo[0].angle = 0
  #   kit.continuous_servo[1].throttle = 0
     return (c)     




     

     
    

    