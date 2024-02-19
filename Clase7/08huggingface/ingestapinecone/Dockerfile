FROM python:3.11
WORKDIR /usr/src/app
RUN cd /usr/src/app
COPY requirements.txt /usr/src/app
COPY app.py /usr/src/app
RUN pip3 install -r /usr/src/app/requirements.txt
CMD python3 /usr/src/app/app.py