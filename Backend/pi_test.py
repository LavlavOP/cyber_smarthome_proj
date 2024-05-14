# region ------------------   ABOUT   -----------------------------

# region ----------   IMPORTS   -----------------------------
from itertools import count
import threading
import socket
import sys
import os
from Crypto.Cipher import AES
import random
#import encription
#import RPi.GPIO as GPIO
import time
#import data_move_firebase

# class motor():
# #motor setup pin
# #motor = GPIO17,27,22
#     def __init__(self , step_count , direction):
#         self.step_count = step_count # 5.625*(1/64) per step, 4096 steps is 360°
#         self.direction = direction # True for clockwise, False for counter-clockwise
#         self.in1 = 17 #pin1
#         self.in2 = 18 #pin2
#         self.in3 = 27 #pin3
#         self.in4 = 22 #pin4
#         self.step_sleep = 0.002 # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
#         step_sequence = [[1,0,0,1], # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
#                          [1,0,0,0],
#                          [1,1,0,0],
#                          [0,1,0,0],
#                          [0,1,1,0],
#                          [0,0,1,0],
#                          [0,0,1,1],
#                          [0,0,0,1]]
#     def motor_setup(self):
#         # setting up
#         GPIO.setmode( GPIO.BCM )
#         GPIO.setup( self.in1, GPIO.OUT )
#         GPIO.setup( self.in2, GPIO.OUT )
#         GPIO.setup( self.in3, GPIO.OUT )
#         GPIO.setup( self.in4, GPIO.OUT )

#         # initializing
#         GPIO.output( self.in1, GPIO.LOW )
#         GPIO.output( self.in2, GPIO.LOW )
#         GPIO.output( self.in3, GPIO.LOW )
#         GPIO.output( self.in4, GPIO.LOW )

#         motor_pins = [self.in1,self.in2,self.in3,self.in4]
#         motor_step_counter = 0

#     def cleanup(self):
#         GPIO.output( self.in1, GPIO.LOW )
#         GPIO.output( self.in2, GPIO.LOW )
#         GPIO.output( self.in3, GPIO.LOW )
#         GPIO.output( self.in4, GPIO.LOW )
#         GPIO.cleanup()

#     def move_motor(self):
#         try:
#             i = 0
#             for i in range(self.step_count):
#                 for pin in range(0, len(self.motor_pins)):
#                     GPIO.output( self.motor_pins[pin], self.step_sequence[motor_step_counter][pin] )
#                 if self.direction==True:
#                     motor_step_counter = (motor_step_counter - 1) % 8
#                 elif self.direction==False:
#                     motor_step_counter = (motor_step_counter + 1) % 8
#                 else: # defensive programming
#                     print( "uh oh... direction should *always* be either True or False" )
#                     motor.cleanup()
#                     exit( 1 )
#                 time.sleep( self.step_sleep )

#         except KeyboardInterrupt:
#             motor.cleanup()
#             exit( 1 )

#         motor.cleanup()
#         exit( 0 )

# class ralay():
# #3 ralay setip pin
# #ralay1 = GPIO12
# #ralay2 = GPIO16
# #ralay3 = GPIO20
# #ralay4 = GPIO21
#     def __init__(self):
#         self.PIN_RELAY_1 = 12 # GPIO12
#         self.PIN_RELAY_2 = 16 # GPIO16
#         self.PIN_RELAY_3 = 20 # GPIO20
#         self.PIN_RELAY_4 = 21 # GPIO21
#     def ralay_setup(self):  
#         GPIO.setmode(GPIO.BCM)

#         GPIO.setup(self.PIN_RELAY_1, GPIO.OUT)
#         GPIO.setup(self.PIN_RELAY_2, GPIO.OUT)
#         GPIO.setup(self.PIN_RELAY_3, GPIO.OUT)
#         GPIO.setup(self.PIN_RELAY_4, GPIO.OUT)

#     #on ralay1
#     def ralay_on1(self):
        
#         print("Turn on relay 1")
#         GPIO.output(self.PIN_RELAY_1, GPIO.HIGH)
#         time.sleep(0.5)
#         GPIO.cleanup()

#     #off ralay1
#     def ralay_off1(self):
#         print("Turn off relay 1")
#         GPIO.output(self.PIN_RELAY_1, GPIO.LOW)
#         time.sleep(1)
#         GPIO.cleanup()
    
#     #on ralay2
#     def ralay_on2(self):
#         print("Turn on relay 2")
#         GPIO.output(self.PIN_RELAY_1, GPIO.HIGH)
#         time.sleep(1)
#         GPIO.cleanup()

#     #off ralay2
#     def ralay_off2(self):
#         print("Turn off relay 2")
#         GPIO.output(self.PIN_RELAY_1, GPIO.LOW)
#         time.sleep(1)
#         GPIO.cleanup()
    
#     #on ralay3
#     def ralay_on3(self):
        
#         print("Turn on relay 3")
#         GPIO.output(self.PIN_RELAY_1, GPIO.HIGH)
#         time.sleep(1)
#         GPIO.cleanup()

#     #off ralay3
#     def ralay_off3(self):
#         print("Turn off relay 3")
#         GPIO.output(self.PIN_RELAY_1, GPIO.LOW)
#         time.sleep(1)
#         GPIO.cleanup()
    
#     #on ralay4
#     def ralay_on4(self):
#         print("Turn on relay 4")
#         GPIO.output(self.PIN_RELAY_1, GPIO.HIGH)
#         time.sleep(1)
#         GPIO.cleanup()

#     #off ralay4
#     def ralay_off4(self):
#         print("Turn off relay 4")
#         GPIO.output(self.PIN_RELAY_1, GPIO.LOW)
#         time.sleep(1)
#         GPIO.cleanup()

# endregion

# # region -----  CONSTANTS  -----
# # For every client to been thread
# SERVER_PORT = 1234
# SERVER_ABORT = "Aborting the server..."  # Message if server error


# # endregion


# # region -------------------------------  Python CLASS  --------------------
# class SessionForClient():
#     def __init__(self):
#         pass

#     # def get_messag(self):
#     #     data = data_move_firebase.receive_messages("pi")
#     #     return data[-1]

#     def run(self):
#         count = 0
#         data = ""
#         # while True:
#         #     while data != SessionForClient.get_messag(self):
#         #         data = SessionForClient.get_messag(self)

#                 if count == 0:
#                     count +=1
#                     #ralay.ralay_off1()
#                     print("light 1 off from pi")

#                     #ralay.ralay_off2()
#                     print("light 2 off from pi")

#                     #ralay.ralay_off3()
#                     print("light 3 off from pi")

#                     #ralay.ralay_off4()
#                     print("light 4 off from pi")
#                     break
                
                
#                 if data == "Light 1 turned on":
#                     #ralay.ralay_on1()
#                     print("light 1 on from pi")
                    
#                 elif data == "Light 2 turned on":
#                     #ralay.ralay_on2()
#                     print("light 2 on from pi")
                    
#                 elif data == "Light 3 turned on":
#                     #ralay.ralay_on3()
#                     print("light 3 on from pi")
                    
#                 elif data == "Light 4 turned on": #garage open
#                     #motor(4096 , False).move_motor()
#                     print("garage open from pi")
                    

#                 elif data == "Light 1 turned off":
#                     #ralay.ralay_off1()
#                     print("light 1 off from pi")
                    
#                 elif data == "Light 2 turned off":
#                     #ralay.ralay_off2()
#                     print("light 2 off from pi")
                    
#                 elif data == "Light 3 turned off":
#                     #ralay.ralay_off3()
#                     print("light 3 off from pi")
                    
#                 elif data == "Light 4 turned off": #garage close
#                     #motor(4096 , True).move_motor()
#                     print("garage close from pi")
        

# # region ------------------------------------   MAIN   ---------------------------------------------

# SessionForClient().run()

# # -------------------------------------------------------------------------------------------------


# # endregion