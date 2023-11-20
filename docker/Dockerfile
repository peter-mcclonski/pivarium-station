#FROM balenalib/raspberry-pi-debian-python:latest
FROM python:latest
WORKDIR /usr/src/app

COPY ./dist/*.whl .
RUN pip install *.whl

ENTRYPOINT python -m pivarium-station