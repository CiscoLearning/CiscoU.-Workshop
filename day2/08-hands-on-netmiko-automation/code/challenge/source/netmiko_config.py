# K: Replace the "TODO" the imports section
# to import the necessary modules and functions and uncomment the lines

from netmiko import #TODO
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from #TODO import devices
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("USERNAME or PASSWORD environment variables not set.")

# Function to apply configuration changes to a device
def apply_config(device, config_commands):
    """Connect to a device and apply configuration commands."""
    try:
        with ConnectHandler(**device) as connection:
            print(f"Connected to {device['name']} ({device['host']})")
            
            # L: Replace the "TODO" with the method to send configuration commands
            # This method is different from send_command() - it's specifically for config changes
            # Hint: this can be determined from the function definition above

            output = connection.send_config_set(#TODO)
            print(f"Configuration applied to {device['name']}:")
            print(output)
            
            # Save configuration to NVRAM
            save_output = connection.send_command("write memory")
            print(f"Configuration saved to {device['name']}: {save_output}")
            
            return True
            
    except NetMikoTimeoutException:
        print(f"Error: Connection to {device['name']} ({device['host']}) timed out")
        return False
    except NetMikoAuthenticationException:
        print(f"Error: Authentication failed for {device['name']} ({device['host']})")
        return False
    except Exception as e:
        print(f"Unexpected error with {device['name']} ({device['host']}): {type(e).__name__}: {str(e)}")
        return False

# Main execution
print("Starting configuration changes on all routers...")
print("="*60)

# M: Replace "TODO" with the code to complete the configuration for each device
# Each router will get a MOTD banner with unique hostname - Don't forget to add your own name!
for device in devices:
    print(f"\nConfiguring {device['name']}...")
    
    # Define configuration commands for this device
    # to change the hostname to include the device name
    config_commands = [
        f"hostname {device['name']}",
        "banner motd ^",
        "Welcome to the Netmiko and CML Automation Lab!",
        "This router has been configured by #TODO using Python and Netmiko!",
        "^"
    ]
    
    # Apply the configuration
    success = apply_config(device, config_commands)
    
    if success:
        print(f"✅ Successfully configured {device['name']}")
    else:
        print(f"❌ Failed to configure {device['name']}")
    
    print("-" * 40)

print("\nConfiguration changes completed!")
print("You can now connect to each router to verify the changes:")
print("- Check hostname with: show running-config | include hostname")
print("- Check banner with: show running-config | include banner")