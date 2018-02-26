# coding:utf-8

import time


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return time.ctime()