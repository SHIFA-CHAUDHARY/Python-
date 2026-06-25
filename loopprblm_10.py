import time
wait_time = 1
maxretries = 5
attempts = 0

while attempts<maxretries:
    print("attempt",attempts+ 1,"wait_time",wait_time, )
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
    
     