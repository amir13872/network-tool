def get_network_config():
    import platform
    import subprocess

    system = platform.system()
    if system == "Windows":
        command = "ipconfig"
    elif system == "Linux" or system == "Darwin":  # Darwin is for macOS
        command = "ifconfig"
    else:
        raise NotImplementedError("Unsupported operating system")

    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}"

def configure_static_ip(ip_address, subnet_mask, gateway):
    import platform
    import subprocess

    system = platform.system()
    if system == "Windows":
        command = f"netsh interface ip set address name=\"Local Area Connection\" static {ip_address} {subnet_mask} {gateway}"
    elif system == "Linux":
        command = f"sudo ifconfig eth0 {ip_address} netmask {subnet_mask} gateway {gateway}"
    else:
        raise NotImplementedError("Unsupported operating system")

    try:
        subprocess.check_output(command, shell=True, text=True)
        return "Static IP configured successfully."
    except subprocess.CalledProcessError as e:
        return f"Error configuring static IP: {e}"