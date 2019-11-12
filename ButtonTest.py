import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(15, GPIO.IN)


while True: # Run forever
    if GPIO.input(15) == GPIO.HIGH:
   # if GPIO.input(15):
        print("0")
    else:
        print("Button was pushed!")
    
                                                                        