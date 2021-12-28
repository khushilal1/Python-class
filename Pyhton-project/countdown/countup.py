
print("Author:Khushilal Mahato\n")
import time
def Time(time_sec):
    print("Your time is going up now:")
    n=int(input("Enter the number p to which you want to stop\n"))
    time.sleep(1)
    while(time_sec<n+1):
        min,sec=divmod(time_sec,60)
        print(f"{min}:{sec}")
        time.sleep(1)
        time_sec=time_sec+1
Time(0)
print("stops")

