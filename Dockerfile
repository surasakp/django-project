FROM python:3
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN ls -l
RUN pip install -r reqs.txt