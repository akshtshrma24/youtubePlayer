FROM python:3.8-slim

WORKDIR ./youtubePlayer

COPY ./frontend ./youtubePlayer/frontend

COPY ./static ./youtubePlayer/static

COPY ./videos ./youtubePlayer/videos

COPY *.py .

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN export FLASK_APP=app.py

CMD ["flask", "run"]