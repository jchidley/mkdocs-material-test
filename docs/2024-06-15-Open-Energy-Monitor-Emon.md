---
date: "2024-06-15"
title: "Open Energy Monitor (Emon)"
tags:
  - energy-monitoring
  - home-automation
  - raspberry-pi
  - iot
---
<!-- markdownlint-disable MD025 -->
# Open Energy Monitor Emon
<!-- markdownlint-enable MD025 -->

## Backup

[Python based Emoncms backup utility](https://community.openenergymonitor.org/t/python-based-emoncms-backup-utility/19526/1)

Download and install Python for Windows

```shell
cd "$env:USERPROFILE\AppData\Local\Programs\Python\Python312\Scripts"
pip install requests
z temp # zoxide
curl -L https://github.com/emoncms/usefulscripts/archive/refs/heads/master.zip -o master.zip
mkdir useful
cd useful
7z x ..\master.zip # 7-Zip
hx .\usefulscripts-master\backup_py\data_downloader.py # Helix editor
# address is "http://10.0.1.111" # doesn't work with http://emonpi.local
# change username and password
python .\usefulscripts-master\backup_py\data_downloader.py
hx .\usefulscripts-master\backup_py\convert_to_csv.py # change username
python .\usefulscripts-master\backup_py\convert_to_csv.py
```

Data file location: `/var/opt/emoncms`

files can be found in the "username" directory

## Data input, emonhub

The inspiration for some of emon's logging, from Jeelabs [The logic of data logging](https://web.archive.org/web/20170730145913/http://jeelabs.org/2009/03/22/the-logic-of-data-logging/index.html)

[EmonHubMqttInterfacer.py](https://github.com/openenergymonitor/emonhub/blob/master/src/interfacers/EmonHubMqttInterfacer.py)
[MQTT JSON Input with timestamp](https://community.openenergymonitor.org/t/mqtt-json-input-with-timestamp/6082) and [suggestion to use in-built processing rather than input methods #788](https://github.com/emoncms/emoncms/pull/788/files)
[Read smart meters (SML interface) with ESP and Tasmota and send data to emoncms](https://community.openenergymonitor.org/t/read-smart-meters-sml-interface-with-esp-and-tasmota-and-send-data-to-emoncms/23642)
[Posting data - HTTP or MQTT](https://docs.openenergymonitor.org/emoncms/postingdata.html)
[API for MinimalModbus](https://minimalmodbus.readthedocs.io/en/stable/apiminimalmodbus.html) and [EmonHubMinimalModbusInterfacer.py](https://github.com/openenergymonitor/emonhub/blob/master/src/interfacers/EmonHubMinimalModbusInterfacer.py)

Interface to Vaillant Arotherm ebus via ESP [ebus](https://github.com/john30/ebusd)
[Receive zigbee sensor data on emonPi](https://community.openenergymonitor.org/t/receive-zigbee-sensor-data-on-emonpi/26311/53) and [MQTT JSON subscribe #198](https://github.com/openenergymonitor/emonhub/pull/198/files#)

## Heat Monitor

### Heat Meter

[Kamstrup temperature sensor "TemperatureSensor 63"](https://www.kamstrup.com/en-en/heat-solutions/meters-devices/temperature-sensors/temperaturesensor_63/documents) data sheet and handbook are the most useful
[Kamstrup, Temperature Sensors](https://uk-metering.net/products/2-wire-pocket-temperature-sensors)
[Kamstrup, Nipples and Pockets](https://uk-metering.net/products/nipples-and-pockets)
Cheaper source of thermowells from [automation24](https://www.automation24.co.uk/thermowells?msclkid=a2f41dcad24d17271b897a82b4b10d1c&utm_source=bing&utm_medium=cpc&utm_campaign=BING%20%7C%20UK%20%7C%20SEA%20%7C%2001.02.00%20%7C%20Process%20Sensors&utm_term=thermowell&utm_content=BING%20%7C%20UK%20%7C%20SEA%20%7C%2001.02.19%20%7C%20Thermowells_spezifisch)

There are 2 kinds, pt100 and pt1000. pt1000 seems slightly cheaper.

[Adafruit PT1000 RTD Temperature Sensor Amplifier - MAX31865](https://thepihut.com/products/adafruit-pt100-rtd-temperature-sensor-amplifier-max31865)
[Pt1000 immersion probe](https://www.automation24.co.uk/pt1000-immersion-probe-titec-kbtf-pt1000-2-0-p-4l)
[Compression fitting TiTEC KVG1/2-VA-VA-6.0](https://www.automation24.co.uk/compression-fitting-titec-kvg1-2-va-va-6-0) this is the 1/2 version, there's a 1/4 version
[ISO and IEC standards at reasonable prices](https://www.evs.ee/en/buying-options)

## Firmware

[AVR-DB Firmware](https://github.com/openenergymonitor/avrdb_firmware/)


