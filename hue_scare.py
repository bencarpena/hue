#20200613 : Scary Hue
#By: @bencarpena

import os
import time

i = 0

while i <= 5:
	ExecOn = 'python3 /home/pi/Scripts/hue/hue_on.py'
	os.system(ExecOn)
	time.sleep(1.5)

	ExecOff = 'python3 /home/pi/Scripts/hue/hue_off.py'
	os.system(ExecOff)
	time.sleep(1)


	os.system(ExecOn)
	time.sleep(2)

	os.system(ExecOff)
	time.sleep(1)

	i += 1

