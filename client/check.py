import datetime
import requests
import time

url = "http://10.0.1.1/"
arr = ['100.txt']
length = len(arr)

a = datetime.datetime.now()

for i in range(3):
	#time.sleep(1)
	f = arr[i%length]
	url1 = url + f
	try:
		r = requests.get(url1, timeout=200)
		r.raise_for_status()
		respTime = str(round(r.elapsed.total_seconds(),2))
		currDate = datetime.datetime.now()
		currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
		print(currDate + " " + respTime + " " + f)
	except requests.exceptions.HTTPError as err01:
		print ("HTTP error: ", err01)
	except requests.exceptions.ConnectionError as err02:
		print ("Error connecting: ", err02)
	except requests.exceptions.Timeout as err03:
		print ("Timeout error:", err03)
	except requests.exceptions.RequestException as err04:
		print ("Error: ", err04)

b = datetime.datetime.now()

c = b - a

#print ("Total time for execution")
#print c.total_seconds() * 1000
