# G - Fill in the blanks in the imports section
# to import the necessary modules and functions

from netmiko import ______________
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from _____________ import devices

# H - Fill in the blanks to complete each code block of the function
# for handling unexpected behavior
def run_command(device, command):
    ___Connect to a device, run a command, and return the output.___
    try:
        # Create a copy of device dict without the 'name' key for ConnectHandler
        device_config = {k: v for k, v in device.items() if k != 'name'}
        with ConnectHandler(**device_config) as connection:
            output = connection.send_command(command)
            return output
    ______ NetMikoTimeoutException:
        return f"Error: Connection to {device['name']} ({device['host']}) timed out"
    ______ NetMikoAuthenticationException:
        return f"Error: Authentication failed for {device['name']} ({device['host']})"
    ______ Exception as e:
        return f"Unexpected error with {device['name']} ({device['host']}): {type(e).__name__}: {str(e)}"

# I - Fill in the blanks to complete each code block in the for loop
# to loop through all the devices and run commands
for ______ in devices:
    print(f"\n{'='*50}")
    print(f"Connecting to {______['name']} ({______['host']})...")
    
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