from microbit import*

#start compass calibration
compass.calibrate()

#MAIN APP LOOP
while True:
	sleep(100)
	compassDir = compass.heading()
	if (compassDir > 315 and compassDir <= 360) or (compassDir >= 0 and compassDir <= 45):
		display.show('N')
	elif compassDir > 45 and compassDir <= 135:
		display.show('E')
	elif compassDir > 135 and compassDir <= 225:
		display.show('S')
	else:
		display.show('W')