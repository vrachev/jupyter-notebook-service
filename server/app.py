import logging
import os

from flask import Flask, Response
from prometheus_client import (
    CollectorRegistry,
    CONTENT_TYPE_LATEST,
    generate_latest,
    multiprocess,
)

from server import metrics

_format = "{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': '%(message)s'}"

logging.basicConfig(level="DEBUG", format=_format)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.before_request(metrics.before_request)
app.after_request(metrics.after_request)


@app.route("/log-some-info")
def log_some_info():
    logger.debug("Some info")
    return "Logged 'Some info'"


@app.route("/")
def index():
    text = "{}<br><br>Here's my secret: {}".format(
        os.getenv("APP_MESSAGE", "Hello, World!"), os.getenv("APP_SECRET", "not set")
    )
    return text


@app.route("/metrics")
def _metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
