from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        # pin.toggle()
        state = led.value()
        print(state)
        state = not state
        print(state)
        led.value(state)
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
led.off()
print("Finished.")
