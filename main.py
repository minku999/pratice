for i in range(1,11):
    print(2*i)
import time
print(time.time())

start = time.time()
for i in range(10000):
    pass
end = time.time()
print(end-start)