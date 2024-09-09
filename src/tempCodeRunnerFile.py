while True:
    currentHour = 100


    calculatedBrightness = (int)(abs((1 - abs((1/12) * (12 - currentHour)))))
    print(calculatedBrightness)
    sbc.set_brightness(calculatedBrightness)
    time.sleep(1)