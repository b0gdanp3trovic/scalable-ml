import requests
import threading


def http_test():
    result = requests.post('http://newapp-lb-1997872629.eu-west-2.elb.amazonaws.com', json = {'LSTAT' : 10, 'RM' : 30})
    print(result.status_code)

threads = []
for i in range(100000):
    t = threading.Thread(target=http_test)
    t.start()