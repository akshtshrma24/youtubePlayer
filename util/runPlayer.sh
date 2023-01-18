#!/bin/bash

cd ./util

export GREEN='\033[0;32m'
export NC='\033[0m'

echo "${GREEN}Updating and upgrading apt-get${NC}"
sudo apt-get update ; sudo apt-get upgrade

echo "${GREEN}Installing ffmpeg${NC}"
sudo apt install --assume-yes ffmpeg 

echo "${GREEN}Installing vlc${NC}"
sudo apt install -y vlc 

echo "${GREEN}Installing pip${NC}"
sudo apt install --assume-yes python3-pip 

echo "${GREEN}Installing requirements${NC}"
pip3 install -r requirements.txt 

echo "${GREEN}Making videos directory${NC}"

cd ../videoDownloading ; mkdir videos  ; cd ../

export FLASK_APP=server.py

python3 -m flask run -p 5001 --host=0.0.0.0


