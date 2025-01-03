def view_arp_table():
    import subprocess
    import platform

    if platform.system() == "Windows":
        command = "arp -a"
    else:
        command = "arp -n"

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error retrieving ARP table: {e}"

def send_arp_request(ip_address):
    import subprocess
    import platform

    if platform.system() == "Windows":
        command = f"arp -d {ip_address} && ping -n 1 {ip_address}"
    else:
        command = f"arp -d {ip_address} && ping -c 1 {ip_address}"

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error sending ARP request: {e}"