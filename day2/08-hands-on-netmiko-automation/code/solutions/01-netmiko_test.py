from netmiko import ConnectHandler  # Import Netmiko's connection handler
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Define connection details for the target device
# These values tell Netmiko how to connect
device = {
    "device_type": "cisco_ios",   # Platform type (Cisco IOS in this case)
    "host": "172.27.12.2",        # Device IP address (R2)
    "username": USERNAME,         # Login username
    "password": PASSWORD,         # Login password
}

try:
    # Establish SSH connection to the device using provided details
    connection = ConnectHandler(**device)
    print("✅ Successfully connected to the router!")

    # Send a command and capture its output
    # "show ip interface brief" displays interface status and IPs
    output = connection.send_command("show ip interface brief")
    print(output)

    # Always disconnect cleanly once you're done
    connection.disconnect()

except Exception as e:
    # Handle any errors (e.g., authentication failure, timeout, unreachable device)
    print(f"❌ Failed to connect: {str(e)}")
