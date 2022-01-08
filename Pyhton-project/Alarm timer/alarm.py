import time 
import datetime
import winsound


alarm_hour=int(input("Ente hour to wae up\n"))
alarm_minute=int(input("Enter minute to wake up\n"))
ampm=input("Enter am or pm\n")
if(ampm=="pm"):
    alarm_hour=alarm_hour+12

while True:
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    if(hour==alarm_hour and minute==alarm_minute):
        print("Wake up")
        break
print("exited")