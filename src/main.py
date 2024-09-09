import screen_brightness_control as sbc
import time as time

while True:
    currentHour = time.localtime().tm_hour
    calculatedBrightness = (abs((1 - abs((1/12) * (12 - currentHour)))) * 100)
    print(calculatedBrightness)
    sbc.set_brightness(calculatedBrightness)
    time.sleep(3600)
