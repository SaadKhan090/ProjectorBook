import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
#normally open switch, falling=when pushed down, rising=when released
GPIO.add_event_detect(15,GPIO.FALLING,callback=button_callback)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
