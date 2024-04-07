#Team The Futurists
#codement'24
#Battery Management System 
#This code is for Taking Sensor input and sending on the ThingSpeak Cloud

import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import urllib.request
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


# Notification function.
from pushbullet import Pushbullet


pb = Pushbullet('o.hMqZ4PGMttflGMTV8EWrfeTO4AoVFe1Q')  #API key of user-1.

ab =Pushbullet('o.HDCB9hz0Jz85TIoYbvUP0aL4cgNOUIdf')   #API key of user-2.



test_temp=35

#temp and humidity pin config
pin=2

#relay and their GPIO pin config
ok=11
GPIO.setup(ok,GPIO.OUT)

flag=0
eflag=0


ok2=8
emer=30
GPIO.setup(ok2,GPIO.OUT)

#ir pin config
irpin=18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN)

#gas sensor GPIO pin config
gas=37
GPIO.setup(gas,GPIO.IN)


volt=12.1
ampere=8
soc=80


	
while True:
	humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,pin)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C Humidity ={1:0.1f}%'.format(temperature,humidity))
	else:
		print('FAILED')
	time.sleep(2)
	
	
	#relay 1 for battery heat reducing i.e on the fan/cooling device
	if temperature>25:
		print('BMS and Battery Cooling System is ON ')
		flag=1
		GPIO.output(ok,1)
	else:
		print('BMS and Battery Cooling System is OFF')
		GPIO.output(ok,0)
		flag=0
	
	
	 #relay 3 for emergency stop
	if emer>50:
		print('Emergency stop')
		eflag=1
		GPIO.output(ok2,1)
	else:
		print('SYSTEM is ON')
		GPIO.output(ok2,0)
		eflag=0
		
	
	  #IR sensor for insects 
	irval=GPIO.input(18)
	if irval==1: print('No movement in the system')
	if irval==1: print(irval)
	
	
	#gas sensor for detection of harmful gaseous
	gval=GPIO.input(gas)
	if gval==0: print('GAS is DETECTED')
	if gval==0: print(gval)
	
	
	volt=volt-0.00007
	print('Voltage of battery is %s',volt)
	ampere=ampere-0.0005
	print('Ampere of battery is %s',ampere)
	soc=soc-0.0000005
	print('Current SoC is %s',soc)
	
	
	
	# All notifications for user-1
	push = pb.push_note("Temperature is"+str(temperature),"Humidity is"+str(humidity ))
	push = pb.push_note("Fan is"+str(flag ),"Emergency is"+str(eflag ))
	push = pb.push_note("IR Motion is"+str(irval ),"SOC is"+str(soc ))
	push = pb.push_note("Current Voltage is"+str(volt ),"Current Ampere Consumptionis"+str(ampere ))
	
	
	
	# Filtered notifications for user-2
	if eflag==1:
		push = ab.push_note(str('BMS AUTOMATICALY STOPPED'),".")
	
	if test_temp>45:
		push = ab.push_note(str('Battery is overheated'),".")
	
	
	if gval==0:
		push = ab.push_note(str('Gas is detected'),".")
	
	
	
	#This code is for taking the all sensors outputs and upload on the ThingSpeak Cloud 
    #and these all values save on the cloud & the .csv file obtained from it and we can train it on jupyter or tensorflow .
	#The .csv file can be easily trained .
	f=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=4WZJQVCOJB0J4A4Y&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s"%(temperature,humidity,flag,eflag,irval,gval))
	print (f.read())
	f.close()
	
	g=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=Y0CB4P7YJZAX16EB&field1=%s&field2=%s&field3=%s"%(volt,ampere,soc))
	print (g.read()) 
	g.close()
	
	print()
	print()
	
	if eflag==1: exit()
	
	
