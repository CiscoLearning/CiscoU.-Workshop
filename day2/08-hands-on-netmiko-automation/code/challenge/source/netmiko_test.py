from netmiko import ConnectHandler  # Import Netmiko's connection handler
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# A: Replace "TODO" with a variable name to define the connection and uncomment the line
# Hint: this can't be arbitrary, but references are found in the code
#TODO = {
    "device_type": "cisco_ios",   # Platform type (Cisco IOS in this case)
    "host": "172.27.12.2",        # Device IP address (R2)
    "username": USERNAME,       # Login username
    "password": PASSWORD,       # Login password
}

try:
    # B: Replace "TODO" with the correct Python function to establish an SSH connection
    # to the device using the details above and uncomment the line
    connection = #TODO(**device)
    print("✅ Successfully connected to the router!")

    # C: Replace "TODO" with the name of the object / instance of the Netmiko class
    # to send a command and capture its output and uncomment the line
    output = #TODO.send_command("show ip interface brief")
    print(output)

    # Always disconnect cleanly once you're done
    connection.disconnect()

except Exception as e:
    # Handle any errors (e.g., authentication failure, timeout, unreachable device)
    print(f"❌ Failed to connect: {str(e)}")