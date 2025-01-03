def scan_netbios_names():
    import os
    import platform
    import subprocess

    netbios_names = []

    # Determine the command based on the operating system
    if platform.system() == "Windows":
        command = "nbtstat -n"
    else:
        command = "nmblookup -M -- "

    try:
        # Execute the command
        output = subprocess.check_output(command, shell=True, text=True)
        netbios_names = parse_netbios_output(output)
    except Exception as e:
        print(f"Error scanning NetBIOS names: {e}")

    return netbios_names

def parse_netbios_output(output):
    netbios_names = []
    lines = output.splitlines()

    for line in lines:
        if "UNIQUE" in line or "GROUP" in line:
            netbios_names.append(line.strip())

    return netbios_names

def display_netbios_names(names):
    if names:
        print("NetBIOS Names:")
        for name in names:
            print(name)
    else:
        print("No NetBIOS names found.")