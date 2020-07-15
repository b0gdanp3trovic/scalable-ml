import requests
import threading
import time


latencies = []

def http_test():
    result = requests.post('http://ml-cluster-lb-fargate-1733395476.eu-central-1.elb.amazonaws.com', json = {'LSTAT' : 10, 'RM' : 30})
    print(result.elapsed.total_seconds())
    latencies.append(result.elapsed.total_seconds())

threads = []
for i in range(1000000):
    t = threading.Thread(target=http_test)
    threads.append(t)
    t.start()
    time.sleep(0.009)


[t.join() for t in threads]

print(sum(latencies)/len(latencies))