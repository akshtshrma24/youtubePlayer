#!/bin/bash

export GREEN='\033[0;32m'
export NC='\033[0m'

echo "${GREEN}Installing pip${NC}"
sudo apt install python3-pip

echo "${GREEN}Upgrading pip${NC}"
pip3 install --upgrade pip

echo "${GREEN}Installing requirements${NC}"
pip3 install -r requirements.txt

export FLASK_APP=app.py

echo "${GREEN}Making videos directory${NC}"
mkdir videos

flask run --host=0.0.0.0