import os
import platform
import json
import requests
from datetime import datetime
from fnmatch import fnmatch

try:
    # Load the configuration file
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    print('config.json not found')
    print('A sample config file is provided in the repository (config_sample.json), please copy it to config.json and modify it.')
    exit(1)

"""
Sample config file:
{
    "data_source_name": "Cycler X",
    "data_directory": "c:/wrk/tmp",
    "data_files": "*.ycd",
    "api_endpoint": "http://localhost:8001/api/v1/directory-info",
    "update_alert_delay": 180,
    "uptime_alert_delay": 5,
    "uptime_alert_scheme": "daily",
    "uptime_alert_GMT_hour": "10",
    "uptime_alert_GMT_minute": 0
}
"""

# check that the required fields are present in the config file
required_fields = ['data_directory', 'data_files', 'api_endpoint', 'update_alert_delay', 'uptime_alert_delay', 'uptime_alert_scheme', 'uptime_alert_GMT_hour', 'uptime_alert_GMT_minute']
error = False
for field in required_fields:
    if field not in config:
        print(f'Error: {field} not found in config file')
        error = True

if error:
    exit(1)

data_source_name = config['data_source_name']
data_directory = config['data_directory']
data_files = config['data_files']
api_endpoint = config['api_endpoint']
update_alert_delay = config['update_alert_delay'] # not used here, but used by the server to determine how long to wait for an update before sending an alert
uptime_alert_delay = config['uptime_alert_delay'] # not used here, but used by the server to determine how long the server should wait for this script to send an update before sending an alert that the server may be down

# Initialize an empty list to hold the file information
file_info = []

# Walk through the directory
for path, dirs, files in os.walk(data_directory):
    for name in files:
        if fnmatch(name, data_files):
            full_path = os.path.abspath(os.path.join(path, name))
            size = os.path.getsize(full_path)
            last_updated = os.path.getmtime(full_path)
            last_updated -= datetime.now().astimezone().utcoffset().total_seconds() # convert from local time to GMT
            last_updated = datetime.fromtimestamp(last_updated).isoformat() # convert to ISO 8601 format
            file_info.append({'path': full_path, 'size': size, 'last_updated': last_updated})

# collect some info about the computer/user
source_info = {
    'name': data_source_name,
    'os': os.name,
    'platform': platform.uname().system,
    'release': platform.uname().release,
    'version': platform.uname().version,
    'architecture': platform.uname().machine,
    'processor': platform.uname().processor,
    'computer_name': platform.uname().node,
    'username': os.getlogin(),
    'home_directory': os.path.expanduser('~')
}

json_request = {
    'config': config,
    'file_info': file_info,
    'source_info': source_info
}

# Send the file information to the API
try:
    response = requests.post(api_endpoint, json=json_request)

    # Check the response
    if response.status_code == 200:
        print('Data sent successfully')
    else:
        print(f'Failed to send data, response status code {response.status_code} - {response.text}')
except requests.exceptions.RequestException as e:
    print(f'Failed to send data, error: {e}')