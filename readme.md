# Voltaiq Pipeline Alert Client

runs on the cyclers and sends info about cycler data to the server

## Python environment

- set up a virtual environement (venv)
- see if the command line prompt includes `(.venv)` or similar.
  - if not, run 
    - `source .venv/Scripts/activate` on Linux
    - `.venv/Scripts/activate.ps1` on windows
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
