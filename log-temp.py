#!/usr/bin/python

import LM75
import logging
import os
import requests
import yaml

import setup_logging

setup_logging.setup_logging()

def loadConfig():
    logger = logging.getLogger(__name__)
    logger.debug("Trying to load config...")
    try:
        with open("config.yml", "r") as ymlfile:
            logger.debug("Config loaded")
            return yaml.load(ymlfile)
    except OSError as e:
        logger.error(e)

def postDataToThingSpeak(config, field, value, label):
    logger = logging.getLogger(__name__)
    ts_config = config["thingspeak"]
    url = ts_config["url"] + ".json"

    payload = {"api_key": ts_config["api_key"], field: str(value)}

    logger.info("Posting %s to %s", label, url)
    r = requests.post(url, data=payload)
    if r.ok:
        logger.info("Successfully posted %s", label)
    else:
        r.raise_for_status()

def main():
    logger = logging.getLogger(__name__)
    sensor = LM75.LM75()

    logger.info("Thermometer logger started")
    config = loadConfig()

    temp = "field1", sensor.getTemp(), "temperature"
    logger.info("Current %s is %s", temp[2], temp[1])
    postDataToThingSpeak(config, *temp)

if __name__=="__main__":
    main()
