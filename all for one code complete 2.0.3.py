import machine
import utime

potentiometer = machine.ADC(26)
servo = machine.PWM(machine.Pin(15))
servo.freq(50)
value= potentiometer.read_u16()
button = machine.Pin(13, machine.Pin.IN)

# this function controls the interval and how far the wiper will go
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# this function uses the interval function to control the servo
def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)

# master loop that runs forever, it calls servo_write and uses if statements to measure voltage using the potentiometer
while True:
    # if statement that checks to see if the switch is turned on or off
    if button.value() == 1:
        #print("on button!")
        value= potentiometer.read_u16()
        if value > 64000:
            for angle in range(120):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            for angle in range(120,-1,-1):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            utime.sleep_ms(5000)
            print("slow",value)
        elif value < 11000:
            for angle in range(120):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            for angle in range(120,-1,-1):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            utime.sleep_ms(1000)
            print("high",value)
        else:
            for angle in range(120):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            for angle in range(120,-1,-1):
                servo_write(servo,angle)
                utime.sleep_ms(10)
            utime.sleep_ms(3000)
            print("mid",value)
        utime.sleep_ms(10)
