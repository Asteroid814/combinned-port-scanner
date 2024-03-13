#!/bin/bash

sudo apt install nmap -y
sudo wget https://github.com/RustScan/RustScan/releases/download/1.10.0/rustscan_1.10.0_amd64.deb 

sudo chmod +x rustscan_1.10.0_amd64.deb 
sudo dpkg -i rustscan_1.10.0_amd64.deb 
