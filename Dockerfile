FROM alpine:3.10

RUN apk add --no-cache build-essential \
    cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev \
    python python-dev python-pip python3 python3-dev python3-pip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]