#!/bin/bash

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
pip3 install pytube 

echo "${GREEN}Making videos directory${NC}"

python3 server.py
