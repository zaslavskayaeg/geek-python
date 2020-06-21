# import time
from time import time as std_time, sleep as std_sleep

# start = time.time()
start = std_time()

print(f"Start at {start}")

# time.sleep(2)
# end = time.time()
std_sleep(2)
end = std_time() 

print(f"End at {end}")
