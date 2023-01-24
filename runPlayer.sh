#!/bin/bash

export GREEN='\033[0;32m'
export CYAN='\033[0;36m'
export NC='\033[0m'

printf "${GREEN}Updating and upgrading apt-get${NC}\n"
sudo apt-get update ; sudo apt-get upgrade

printf "${GREEN}Installing ffmpeg${NC}\n"
sudo apt install --assume-yes ffmpeg 

printf "${GREEN}Installing vlc${NC}\n"
sudo apt install -y vlc 

printf "${GREEN}Installing pip${NC}\n"
sudo apt install --assume-yes python3-pip 

printf "${GREEN}Installing requirements${NC}\n"
pip3 install pytube 

printf "${GREEN}Making videos directory${NC}\n"
mkdir ./videoDownloading/videos

printf  "${GREEN}Starting Server${NC}\n"
printf "${CYAN}running on https://$(ip addr | grep 192 | awk '{print $2}' | cut -d '/' -f 1):8080 ${NC}\n"
python3 server.py
