import requests
import threading
import time
import json


latencies = []

def http_test():
    result = requests.post('http://34.120.253.15/', json = {'LSTAT' : 10, 'RM' : 30})
    print(result.elapsed.total_seconds())
    latencies.append(result.elapsed.total_seconds())

threads = []
for i in range(10000):
    t = threading.Thread(target=http_test)
    threads.append(t)
    t.start()


[t.join() for t in threads]