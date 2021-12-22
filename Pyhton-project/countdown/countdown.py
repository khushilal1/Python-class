
print("Author:Khushilal Mahato\n")
import time
n=int(input("Enter the value from which you wanto countdown\n"))

def Time(time_sec):
    while(time_sec<60):

        min,sec=divmod(time_sec,60)
        print(f"{min}:{sec}")
        time.sleep(1)
        time_sec=time_sec-1
Time(n)
print("stop")