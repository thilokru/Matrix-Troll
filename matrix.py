from random import random
from time import sleep
import os

coolstuff = list(line.rstrip() for line in os.popen("ipconfig"))
coolstuff = [x for x in coolstuff if x]

active_columns = [False]*180
for i in range(len(active_columns)):
	active_columns[i] = (random() < 0.02)

while(True):
	string = ""
	if(random() < 0.9):
		for activity in active_columns:
			if(activity):
				string = string + str(int(random() * 10))
			else:
				string = string + " "
	else:
		string = coolstuff[int(random()*len(coolstuff))]
	print(string)
	
	for i in range(len(active_columns)):
		if(active_columns[i]):
			if(random() < 0.1):
				active_columns[i] = False
		else:
			if(random() < 0.02):
				active_columns[i] = True
	
	sleep(0.1)