"""
cisco_devices.py
================

This module contains device configurations for all network devices in the topology.
It includes device details such as device type, host address, and credentials.

The device credentials are loaded from environment variables to ensure sensitive information
is not hardcoded in the script.
"""

import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

devices = [
    {
        "name": "R1",
        "device_type": "cisco_ios",
        "host": "172.27.12.1",
        "username": USERNAME,
        "password": PASSWORD,
    },
    {
        "name": "R2",
        "device_type": "cisco_ios",
        "host": "172.27.12.2",
        "username": USERNAME,
        "password": PASSWORD,
    },
    {
        "name": "R3",
        "device_type": "cisco_ios",
        "host": "172.27.13.3",
        "username": USERNAME,
        "password": PASSWORD,
    }
]