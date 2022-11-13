# This is Junha's Development Blog

# Python Virtual Environment

## Enable

`sudo apt-get install python3-venv`

## Setup

`python3 -m venv .venv`

## Activate

`source .venv/bin/activate`

## Python Version

if you run `python` this will get you to Python2  
run `python3` as you use python 3.x version

# Access Localhost from the Internet

## Install

`sudo apt install nodejs`
`sudo apt install npm`
`sudo apt install npx`
`sudo apt install yarn`

## Localtunnel

`npx localtunnel --port <port_number>`

## Localhost.run

`ssh -R 80:localhost:[port-number] localhost.run`