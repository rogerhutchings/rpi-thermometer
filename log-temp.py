#!/usr/bin/python

import LM75
import logging
import os
import requests
import yaml

import setup_logging

# logging.basicConfig(filename="thermometer.log", level=logging.INFO)

# os.chdir(os.path.dirname(__file__))

def loadConfig():
  logger = logging.getLogger(__name__)
  try: 
    with open("config.yml", "r") as ymlfile:
      return yaml.load(ymlfile)
  except OSError as e:
    logger.error(e)

def postData(config, temp):
  ts_config = config['thingspeak']
  payload = {'api_key': ts_config['api_key'], 'field1': str(temp)}
  r = requests.post(ts_config['url'] + '.json', data=payload)
  print(r.json())

def main():
  setup_logging.setup_logging()
  logger = logging.getLogger(__name__)

  logger.info('Thermometer logger started')
  config = loadConfig()
  sensor = LM75.LM75()
  temp = sensor.getTemp()
  # postData(config, temp)

if __name__=="__main__":
   main()


