import time


class Application(object):
    """"""
    urls = [
        ("/", "say_time"),
        ("/hi", "say_hi"),
        ("/time", "say_time")
    ]

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")
        handler = self._match(path)
        if handler:
            handler = globals()[handler]
            return handler(environ, start_response)
        else:
            start_response("404 Not Found", [])
            return "sorry, not found"

    def _match(self, path):
        if path.startswith("/static/"):
            pass
            # return self.static_file_handler
        else:
            for url, handler in self.urls:
                if path == url:
                    return handler


def say_hi(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return "hi"


def say_time(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return time.ctime()
