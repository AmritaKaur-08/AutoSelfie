# AutoSelfie: Python-Powered Smart Selfie Automation

## Overview
This project is designed to automate the process of taking selfies and detecting faces and smiles using Python and OpenCV. The program utilizes Haar Cascade classifiers to detect human faces and smiles in real-time.

## Features
- Face Detection: Detects human faces using `haarcascade_frontalface_default.xml`.
- Cat Face Detection: Detects cat faces using `haarcascade_frontalcatface.xml`.
- Smile Detection: Detects smiles using `haarcascade_smile.xml`.
- Selfie Capture: Captures a selfie when a face and smile are detected.
- Sound Effect: Plays a camera click sound (`camera_click.wav`) when a selfie is captured.

## Getting Started

## Prerequisites
- Python 3.11: Ensure Python is installed on your system.
- Virtual Environment (optional but recommended): Set up a virtual environment to isolate project dependencies.
- OpenCV and Contrib Modules: Install OpenCV along with its contrib modules by running:
  ```bash
  pip install opencv-python opencv-contrib-python
  
## Installation
Clone the repository:
```bash
git clone https://github.com/AmritaKaur-08/AutoSelfie.git

Navigate to the project directory:
```bash
cd AutoSelfie

## Running the Project
To start the program, run the Selfie.py script:
```bash
python Selfie.py

This will activate your webcam and start detecting faces and smiles. When both a face and a smile are detected, the program will capture a selfie 
