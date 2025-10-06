# H: Replace the "TODO" in the  imports section to import 
# the necessary modules and functions and uncomment the lines
# Hint: you can use previous code examples and the lab instructions for help

from netmiko import #TODO
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from #TODO import devices

# I: Replace the "TODO" with the missing pieces to complete each code 
# block to handle unexpected errors and uncomment the lines
# Hint: the first replacement deals with docstrings while the others deal with exception handling

def run_command(device, command):
    #TODO Connect to a device, run a command, and return the output.#TODO
    try:
        with ConnectHandler(**device) as connection:
            output = connection.send_command(command)
            return output
    #TODO NetMikoTimeoutException:
        return f"Error: Connection to {device['name']} ({device['host']}) timed out"
    #TODO NetMikoAuthenticationException:
        return f"Error: Authentication failed for {device['name']} ({device['host']})"
    #TODO Exception as e:
        return f"Unexpected error with {device['name']} ({device['host']}): {type(e).__name__}: {str(e)}"

# J: Replace the "TODO" to complete each code block in the for loop
# to loop through all the devices and run commands and uncomment the lines

for #TODO in devices:
    print(f"\n{'='*50}")
    print(f"Connecting to {#TODO['name']} ({#TODO['host']})...")
    
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