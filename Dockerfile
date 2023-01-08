FROM python:3.8.9-slim-buster

#make working directory
WORKDIR /youtubePlayer


# Copies Directories
COPY /frontend /youtubePlayer/frontend
COPY /static /youtubePlayer/static


# Copies python
COPY /handlers/* /youtubePlayer/
COPY /util/* /youtubePlayer/
COPY /videoffmpeg/* /youtubePlayer/
COPY /vlcHandling/* /youtubePlayer/
COPY app.py /youtubePlayer/

# Setting up directory

#Installing dependencies
RUN apt-get --assume-yes update

RUN apt-get --assume-yes install ffmpeg 

RUN apt-get --assume-yes install vlc 

RUN apt-get --assume-yes install python3-pip 

RUN pip3 install -r requirements.txt 

# Setting up directory for flask and making directory for videos
RUN export FLASK_APP=app.py 

RUN mkdir videos 

# start flask web server on all addresses
CMD ["python3", "-m", "flask", "run", "-p", "5001","--host=0.0.0.0"]





