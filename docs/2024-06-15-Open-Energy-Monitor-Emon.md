---
date: "2024-06-15"
title: "Open-Energy-Monitor-Emon"
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

## Links

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->
