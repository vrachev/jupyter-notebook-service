import logging
import os

from flask import Flask, Response, request, render_template
import subprocess

from server import metrics

_format = "{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': '%(message)s'}"

logging.basicConfig(level="DEBUG", format=_format)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.before_request(metrics.before_request)
app.after_request(metrics.after_request)


# @app.route("/log-some-info")
# def log_some_info():
#     logger.debug("Some info")
#     return "Logged 'Some info'"
#
#
# @app.route("/")
# def index():
#     text = "{}<br><br>Here's my secret: {}".format(
#         os.getenv("APP_MESSAGE", "Hello, World!"), os.getenv("APP_SECRET", "not set")
#     )
#     return text
#
#
# @app.route("/metrics")
# def _metrics():
#     registry = CollectorRegistry()
#     multiprocess.MultiProcessCollector(registry)
#     return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)


@app.route("/intra_run_data_notebook/")
def intra_run_data_notebook():
    args = request.args
    task_id = args.get("task_id")
    metric_name = args.get("metric_name")
    subprocess.check_call(
        f"papermill -p task_id {task_id} -p metric_name {metric_name} ./simple_ftdc.ipynb ./{metric_name}.ipynb",
        shell=True,
    )
    subprocess.check_call(
        f"jupyter nbconvert --to html --execute ./{metric_name}.ipynb --output ./templates/{metric_name}.html",
        shell=True,
    )
    return render_template(f"{metric_name}.html")
    return args


if __name__ == "__main__":
    app.run(host="0.0.0.0")
