# Python Environment Setup Instructions

## Update Python Installation

First, update and upgrade system's packages:
```bash
sudo apt-get update
sudo apt-get upgrade
```

## Install Required Python Packages

Install the necessary Python packages:
```bash
sudo apt install python3-requests
sudo apt install python3-pyaudio
```

## Identify Microphone Devices

To identify the microphone devices available on your RaspberryPi, run:
```bash
python3 getdevices.py
```
If you see output like `bcm2835 Headphones: - (hw:2,0)`, set the `dev_index = 2` on line 9 of `record.py`.

## Record Audio

To record audio, execute:
```bash
python3 record.py
```

## Identify Audio

To analyze the recorded audio file, use:
```bash
python3 identify.py test1.wav
```

## Start the Localhost

To start a simple HTTP server on localhost:
```bash
python3 -m http.server 8000
```

## Loop Execution

To run the main loop of the application, do:
```bash
python3 main.py
```
This will run the recording, identify, also setting up the server and open the localhost in the device. If you want to run the whole system, just run this after Identify Microphone Devices Step.
