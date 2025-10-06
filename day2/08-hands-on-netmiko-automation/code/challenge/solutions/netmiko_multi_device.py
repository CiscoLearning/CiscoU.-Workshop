from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# List of devices (dictionary for each device)
devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.27.12.1",  # R1's IP address
        "username": USERNAME,   # Login username
        "password": PASSWORD,   # Login password
    },
    {
        "device_type": "cisco_ios",
        "host": "172.27.13.3",  # R3's IP address
        "username": USERNAME,   # Login username
        "password": PASSWORD,   # Login password
    },
]

# Loop through devices
for device in devices:
    host = device['host']
    print(f"\n{'='*50}")
    print(f"Attempting to connect to {host}...")
    print(f"{'='*50}")
    
    try:
        # Attempt to establish connection
        connection = ConnectHandler(**device)
        print(f"Successfully connected to {host}!")
        
        try:
            # Send command and get output
            output = connection.send_command("show version", read_timeout=30)
            print(f"\nOutput from {host}:\n{output}")
            
        except Exception as cmd_error:
            print(f"Error executing command on {host}: {str(cmd_error)}")
            
        finally:
            # Always close the connection
            connection.disconnect()
            print(f"Disconnected from {host}")
            
    except NetMikoTimeoutException:
        print(f"Connection to {host} timed out. Device may be unreachable.")
    except NetMikoAuthenticationException:
        print(f"Authentication failed for {host}. Please check credentials.")
    except Exception as e:
        print(f"An error occurred while connecting to {host}: {str(e)}")

print("\nDevice connection attempts completed.")