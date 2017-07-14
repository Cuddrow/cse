import os
import time
import glob
import csv
import datetime as dt
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')	# Starts interfacing with probe
os.system('modprobe w1-therm')	# Starts interfacing with probe

initial_time = time.time()
initial_time_write = time.time()

Linput = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Linput, GPIO.IN)

timearray = []
temparray = []
lightarray = []

base_directory = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_directory + '28*')[0]
device_file = device_folder + '/w1_slave'

today_file = dt.datetime.today()
today_file = today_file.strftime('%Y %m %d')

read_interval = input('input read frequency: ')
write_interval = input('input write frequency: ')

def tempreader():
	f = open(device_file, 'r')
	lines = f.read().split()
	f.close()
	temp = lines[21]
	finaltemp = temp[2:7]
	finaltemp = (float(finaltemp))/1000
	finaltime = time.time()
	return finaltemp, finaltime

def lightreader():
	
	GPIO.setup(Linput, GPIO.OUT)
	GPIO.output(Linput, GPIO.LOW)

	lightsum = []
	light_read_interval = 0.2
        light_initial_time = time.time()

        for i in range (3):
                reading = 0
                GPIO.setup(Linput, GPIO.OUT)
                GPIO.output(Linput, GPIO.LOW)
                light_initial_time = time.time()
                light_current_time = time.time()
                while light_current_time >= (light_initial_time + 0.2):
                        light_current_time = time.time()

                
                GPIO.setup(Linput, GPIO.IN)
                while (GPIO.input(Linput) == GPIO.LOW):
                        reading += 1
                lightsum.append(reading)
                i += 1
	                       
                
        summed_readings = (sum(lightsum))/len(lightsum)
        print 'Summed light readings: ' + str(summed_readings)
        return summed_readings
	
while True:
	current_time = time.time()
	write_time = time.time()
	if current_time >= (initial_time + read_interval):
		temperature, measured_time = tempreader()
		#light = lightreader()
		#print 'temperature in degrees celcius: ' + str(temperature)
		#print 'measured at time: ' + str(measured_time)
		timearray.append(measured_time)
		temparray.append(temperature)
		#lightarray.append(light)
		initial_time = time.time()
		#print timearray
		#print temparray
		
	if write_time >= (initial_time_write + write_interval):
		writer_time = csv.writer(open('timearray' + today_file + '.csv', 'wr'), delimiter=' ')
		myrows_time = zip(timearray)
		for row in myrows_time:
			writer_time.writerows([row])
			
		writer_temp = csv.writer(open('temparray' + today_file + '.csv', 'wr'), delimiter=' ')
		myrows_temp = zip(temparray)
		for row in myrows_temp:
			writer_temp.writerows([row])

		#writer_light = csv.writer(open('lightarray' + today_file + '.csv', 'wr'), delimiter=' ')
		#myrows_light = zip(lightarray)
		#for row in myrows_light:
		#	writer_light.writerows([row])
		
		initial_time_write = time.time()
		today = dt.datetime.today()
		print 'Files written ' + today.strftime('%Y-%m-%d %H:%M:%S')
		
	
	
