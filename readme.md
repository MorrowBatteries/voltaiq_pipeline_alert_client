# Voltaiq Pipeline Alert Client

This simple script does a very specific job:
runs on the cyclers and sends info about cycler data to the server
The server will then check if this data has reached Voltaiq and send an alert if not.

## NOTE: This is a public repository

## Installation

- install the following:
  - python 3.12: `https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe`
  - git for windows: `https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe`
- open git bash or another shell
- create a directory for this script (for example d:\PIPELINE_ALERT) and cd to it
- clone the source code (be sure to include the last dot on the line below):
  - `git clone https://github.com/MorrowBatteries/voltaiq_pipeline_alert_client.git .`
- set up a virtual environement (venv)
  - `python -m venv .venv`
- activate the environment
  - bash: `source .venv/scripts/activate`
  - ps: `.venv/scripts/activate.ps1`
- make sure the command line prompt includes `(.venv)` or similar.
- run `pip install -r requirements.txt`.

## Configuration

Copy config_sample.json to config.json and modify to match your setup.

## How to run:

```bash
python pipeline_alert_client.py
```

### Note:

This script should be set up in cron / task scheduler to run at predefined intevals, either daily or hourly.
Make sure the interval fits with the config, as it tells the server when to expect data from this cycler.
