FROM python:3.9
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY . .
RUN apt-get update
RUN apt-get install -y gcc libavdevice-dev libavfilter-dev libopus-dev libvpx-dev pkg-config
RUN apt-get install -y locales
RUN pip install -r ./requirements.txt