from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from cisco_devices import devices

# Function to connect to a device and run a command
def run_command(device, command):
    """Connect to a device, run a command, and return the output."""
    try:
        with ConnectHandler(**device) as connection:
            output = connection.send_command(command)
            return output
    except NetMikoTimeoutException:
        return f"Error: Connection to {device['name']} ({device['host']}) timed out"
    except NetMikoAuthenticationException:
        return f"Error: Authentication failed for {device['name']} ({device['host']})"
    except Exception as e:
        return f"Unexpected error with {device['name']} ({device['host']}): {type(e).__name__}: {str(e)}"

# Loop through all devices and run commands
for device in devices:
    print(f"\n{'='*50}")
    print(f"Connecting to {device['name']} ({device['host']})...")
    
    # Show device uptime and version
    commands = [
        "show version | include uptime",
        "show version | include Version"
    ]
    
    for cmd in commands:
        print(f"\nRunning command: {cmd}")
        result = run_command(device, cmd)
        print(f"{device['name']}: {result}")
    
    print("="*50)