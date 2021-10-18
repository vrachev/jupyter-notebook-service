import time

from flask import request
from prometheus_client import Histogram


REQUEST_TIME = Histogram(
    "http_request_latency_seconds",
    "HTTP Request latency in seconds",
    ["app_name", "endpoint"],
)


def after_request(response):
    resp_time = time.time() - request.start_time
    REQUEST_TIME.labels(__name__, request.path).observe(resp_time)
    return response


def before_request():
    request.start_time = time.time()
