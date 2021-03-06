try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")



GPIO.setmode(GPIO.BOARD)
"""
It is possible that you have more than one script/circuit on the GPIO of your Raspberry Pi. As a result of this, if RPi.GPIO detects that a pin has been configured to something other than the default (input), you get a warning when you try to configure a script. To disable these warnings:
"""
GPIO.setwarnings(False)
#numbers of pin used pin number
channel_in=4
channel_out=3
channels=[channel_in,channel_out]


def setup():
    GPIO.setup(channel_in, GPIO.IN)
    GPIO.setup(channel_out, GPIO.OUT)
    #GPIO.setup(channel_out, GPIO.OUT, initial=GPIO.HIGH)
    pass

def clean():
    for c in channels:
        GPIO.cleanup(channels)

def handle(data,status): 
    #if GPIO.input(channel_in)==GPIO.HIGH: 
    if GPIO.input(channel_in)==GPIO.LOW:
        GPIO.output(channel, GPIO.HIGH)
        pass
    #GPIO.output(channel, GPIO.HIGH)
    #GPIO.output(channel, GPIO.LOW)
    pass


