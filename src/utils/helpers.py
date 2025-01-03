def execute_command(command):
    import subprocess

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def format_results(results):
    formatted = results.strip().split('\n')
    return formatted

def is_valid_ip(ip):
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None

def is_valid_hostname(hostname):
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None