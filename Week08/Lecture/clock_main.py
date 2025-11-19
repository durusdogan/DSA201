import clock as c
import time

clock1 = c.Clock(4, 18, 9)
print(clock1)

clock2 = c.Clock(23, 59, 55)
print(clock2)
for i in range(100):
    time.sleep(1)
    clock2.tick()
    print(clock2)