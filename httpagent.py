# -*- coding: utf-8 -*-
import json
import threading
import urllib.request, urllib.parse
class httpagent:
    def __init__(self):
        pass

    def get_async(self, url, data=None, callback=None):
        self.request_async(url, data, self.get, callback)


    def post_async(self, url, data=None, callback=None):
        self.request_async(url, data, self.post, callback)


    def request_async(self, url, data, method, callback):
        event = threading.Event()
        runner = threading.Thread(target=self.run,
                                  args=(event, url, data, method, callback))
        runner.start()
        event.wait()


    def run(self, event, url, data, method, callback):
        event.set()
        result = method(url, data)
        if callback:
            callback(result)


    def get(self, url, data):
        if data:
            params = urllib.parse.urlencode(data)
            url = '?'.join(url, params)
        return urllib.request.urlopen(url).read()


    def post(self, url, data):
        if data:
            params = urllib.parse.urlencode(data)
            return urllib.request.urlopen(url, params).read()
        else:
            return urllib.request.urlopen(url).read()


if __name__ == '__main__':
    def print_response(response):
        print((response))

    s=httpagent()
    s.post_async('http://localhost:8000',None, callback=print_response)
    print('done.')
b

