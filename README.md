# Raspberry Pi Temperature Logger

Reads out the temperature from an LM75 temperature sensor, and publishes it to ThingSpeak for visualisation, sharing and whatnot.

## Installation

1. Clone the repo.
1. Install the following dependencies:

        sudo apt-get install python-yaml python-requests

    (Annoyingly, `pip` doesn't seem to install things properly on my RPi, so I'm using the system packages instead.)

## Configuration

A `config.yml` file containing the channel credentials for ThingSpeak is expected:

```YAML
thingspeak:
  api_key: RANDOMAPIKEYSTRING
  url: https://api.thingspeak.com/update
```

## Usage

This is designed to be used as a regular task in conjunction with `cron`. For example, we can add the following by running `crontab -e` to run the job every hour:

```
0 * * * * (cd /home/pi/thermometer || exit 1; /usr/bin/python3 ./log-temp.py)
```
