# -*- coding: utf-8 -*-

import threading
import urllib


def get_async(url, data=None, callback=None):
    request_async(url, data, get, callback)


def post_async(url, data=None, callback=None):
    request_async(url, data, post, callback)


def request_async(url, data, method, callback):
    event = threading.Event()
    runner = threading.Thread(target=run,
                              args=(event, url, data, method, callback))
    runner.start()
    event.wait()


def run(event, url, data, method, callback):
    event.set()
    result = method(url, data)
    if callback:
        callback(result)


def get(url, data):
    if data:
        params = urllib.urlencode(data)
        url = '?'.join(url, params)
    return urllib.urlopen(url).read()


def post(url, data):
    if data:
        params = urllib.urlencode(data)
        return urllib.urlopen(url, params).read()
    else:
        return urllib.urlopen(url).read()


if __name__ == '__main__':
    def print_response(response):
        print(response)

    get_async('http://localhost:8080', callback=print_response)
    print('done.')
