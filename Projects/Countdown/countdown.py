import time

current_time = int(input("How many seconds: "))

while current_time > 0:
    print(current_time)
    time.sleep(1)
    current_time -= 1
    
print("Time is up !\n")
