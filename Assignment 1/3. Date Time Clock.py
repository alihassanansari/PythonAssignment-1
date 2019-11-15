#############################
#--- 3. Date Time Clock  ---#
#############################

import time
import datetime

while True:
    
    date_now = "Date : " + datetime.datetime.now().strftime("%A, %d-%B-%Y")
    time_now = "Time : " + datetime.datetime.now().strftime("%I:%M:%S %p")
    
    print(date_now + "\t --- " + time_now, end="\r", flush=True)
    
    time.sleep(1)