
# print("Author:Khushilal Mahato\n")
# import time
# # n=int(input("Enter the value from which you wanto cou\n"))

# def Time(time_sec):
#     while(time_sec<60):
#         min,sec=divmod(time_sec,60)
#         print(f"{min}:{sec}")
#         if(min<60):
#             hr,min=divmod(min,60)
#             print(f"{hr}:{min}")

#         time.sleep(1)
#         time_sec=time_sec+1
# Time(0)
# print("stop")

# a,c=divmod(4,3)
# print(c)

import time
# n=int(input("Enter the value from which you wanto cou\n"))

def Time(time_sec):
    while(time_sec<60):
        min,sec=divmod(time_sec,60)
        print(f"{min}:{sec}")
        time.sleep(1)
        time_sec=time_sec+1
Time(0)
print("stop")

