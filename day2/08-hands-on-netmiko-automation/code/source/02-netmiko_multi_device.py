from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# D - fill in the blank to complete the name of the device type and credentials
# of the routers you are connecting to
devices = [
    {
        "device_type": "_________",
        "host": "172.27.12.1",  # R1's IP address
        "username": "________", # Login username
        "password": "________", # Login password
    },
    {
        "device_type": "_________",
        "host": "172.27.13.3",  # R3's IP address
        "username": "________", # Login username
        "password": "________", # Login password
    },
]

# Loop through devices
for device in devices:
    host = device['host']
    print(f"\n{'='*50}")
    print(f"Attempting to connect to {host}...")
    print(f"{'='*50}")
    
    try:
        # E - fill in the blank with the name of the function to
        # attempt to establish connection to the devices
        connection = ____________(**device)
        print(f"Successfully connected to {host}!")
        
        try:
            # Send command and get output
            output = connection.send_command("show version", read_timeout=30)
            print(f"\nOutput from {host}:\n{output}")
            
        except Exception as cmd_error:
            print(f"Error executing command on {host}: {str(cmd_error)}")
            
        finally:
            # E - fill in the blank with the name of method of the connection object
            # to close the connection to the devices
            connection.__________()
            print(f"Disconnected from {host}")
    # F - fill in the blanks with the names of the exceptions to handle (Hint: you imported them)       
    except ______________________________:
        print(f"Connection to {host} timed out. Device may be unreachable.")
    except ______________________________:
        print(f"Authentication failed for {host}. Please check credentials.")
    except Exception as e:
        print(f"An error occurred while connecting to {host}: {str(e)}")

print("\nDevice connection attempts completed.")