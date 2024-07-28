# Home Alarm System

## Overview
This project provides a simple home alarm system implemented on a Raspberry Pi. It uses a motion detection sensor to detect any movements in the environment. When motion is detected, the system can either trigger a buzzer and LED light or send a notification to a mobile device via Pushbullet, depending on the set mode.

## Features
  - **Motion Detection**: Utilizes GPIO input to detect motion through a sensor connected to a Raspberry Pi.
  - **Alert System**: Offers two modes of alerts:
    - **Buzzer Mode**: Activates a buzzer and an LED light when motion is detected.
    - **Silent Mode**: Sends a notification to a linked device via Pushbullet without making a physical alert.
  - **Configurable Notification**: Users can set up the system to send alerts to specific devices through Pushbullet.

## Usage
To run this project:
  - Download the `home_alarm_system.py` script directly to your Raspberry Pi using the following command:
     ```
     curl -o home_alarm_system.py [URL to home_alarm_system.py file]
     ```
  - Install the necessary dependencies by running `pip install pushbullet.py RPi.GPIO`.
  - Create a Pushbullet account at [Pushbullet](https://www.pushbullet.com/).
  - Navigate to Settings -> Account -> Create Access Token on the Pushbullet website to obtain your access token.
  - Open `home_alarm_system.py` with a text editor.
  - Update the `PUSHBULLET_TOKEN` in `home_alarm_system.py` with your Pushbullet access token.
  - Execute the script by navigating to its directory and typing `home_alarm_system.py` in the terminal.

## Prerequisites
- **Hardware**:
  - Raspberry Pi (any model with GPIO pins)
  - Motion sensor (compatible with GPIO)
  - Buzzer
  - LED light
- **Software**:
  - Python 3.x
  - Raspberry Pi OS
  - `pushbullet.py` Python library
  - `RPi.GPIO` Python library

## Input
The main input to this program comes from the motion sensor connected to the GPIO pins of the Raspberry Pi.

## Output
  - **Console Output**: Prints the status of the system (`Idle` or `Motion has been detected...`).
  - **Physical Output**: Engages a buzzer and LED light depending on the mode set when motion is detected.
  - **Notification Output**: Sends a push notification to a linked device via Pushbullet in Silent Mode.

## Notes
  - Ensure all hardware components are correctly connected to the Raspberry Pi GPIO pins as per their respective specifications.
  - This script runs in an infinite loop, constantly checking for motion unless manually stopped.
  - Always test the system in a controlled environment to ensure it works as expected before deploying it in a real scenario.