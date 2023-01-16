#!/bin/bash

cd ./util

export GREEN='\033[0;32m'
export NC='\033[0m'

# echo "${GREEN}Installing ffmpeg${NC}"
# sudo apt install ffmpeg > /dev/null 2>&1

# echo "${GREEN}Installing vlc${NC}"
# sudo apt install -y vlc > /dev/null 2>&1

# echo "${GREEN}Installing pip${NC}"
# sudo apt install python3-pip > /dev/null 2>&1

# echo "${GREEN}Installing requirements${NC}"
# pip3 install -r requirements.txt > /dev/null 2>&1

echo "${GREEN}Making videos directory${NC}"

cd ../videoDownloading ; mkdir videos > /dev/null 2>&1 ; cd ../

export FLASK_APP=server.py

python3 -m flask run -p 5001 --host=0.0.0.0


