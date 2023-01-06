#!/bin/bash

export GREEN='\033[0;32m'
export NC='\033[0m'

echo "${GREEN}Reinstalling libqt5svg5${NC}"
sudo apt install --reinstall libqt5svg5

echo "${GREEN}Installing ffmpeg${NC}"
sudo apt install ffmpeg

echo "${GREEN}Installing vlc${NC}"
sudo apt install -y vlc

echo "${GREEN}Installing pip${NC}"
sudo apt install python3-pip

echo "${GREEN}Installing requirements${NC}"
pip3 install -r requirements.txt

export FLASK_APP=app.py

echo "${GREEN}Making videos directory${NC}"
mkdir videos

python3 -m flask run --host=0.0.0.0