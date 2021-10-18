FROM python:3.7.12-slim

EXPOSE 5000

ADD . /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
RUN mkdir /tmp/prometheus_multiproc
RUN pip3 install .

ENTRYPOINT ["gunicorn"]
CMD ["wsgi"]
