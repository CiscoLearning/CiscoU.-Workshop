from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# D: Replace "TODO"  with the correct device type and credentials
# of the routers you are connecting to and uncomment the lines
# Remember: we don't want to hardcode credentials in scripts
devices = [
    {
        "device_type": "#TODO",
        "host": "172.27.12.1",  # R1's IP address
        "username": "#TODO", # Login username
        "password": "#TODO", # Login password
    },
    {
        "device_type": "#TODO",
        "host": "172.27.13.3",  # R3's IP address
        "username": "#TODO", # Login username
        "password": "#TODO", # Login password
    },
]

# Loop through devices
for device in devices:
    host = device['host']
    print(f"\n{'='*50}")
    print(f"Attempting to connect to {host}...")
    print(f"{'='*50}")
    
    try:
        # E: Replace "TODO" with the name of the function to
        # attempt to establish connection to the devices and uncomment the line
        connection = #TODO(**device)
        print(f"Successfully connected to {host}!")
        
        try:
            # Send command and get output
            output = connection.send_command("show version", read_timeout=30)
            print(f"\nOutput from {host}:\n{output}")
            
        except Exception as cmd_error:
            print(f"Error executing command on {host}: {str(cmd_error)}")
            
        finally:
            # F: Replace "TODO" with the name of method of the connection object
            # to close the connection to the devices and uncomment the line
            connection.#TODO()
            print(f"Disconnected from {host}")
    # G: Replace "TODO" withh the names of the exceptions to handle (Hint: you imported them)
    # and uncomment the lines
    except #TODO:
        print(f"Connection to {host} timed out. Device may be unreachable.")
    except #TODO:
        print(f"Authentication failed for {host}. Please check credentials.")
    except Exception as e:
        print(f"An error occurred while connecting to {host}: {str(e)}")

print("\nDevice connection attempts completed.")