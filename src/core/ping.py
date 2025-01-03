def ping_host(host, count=4):
    import subprocess
    import platform

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]

    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error pinging {host}: {e}"

def parse_ping_results(output):
    lines = output.splitlines()
    results = {}
    
    for line in lines:
        if "time=" in line:
            time_index = line.index("time=") + 5
            time_value = line[time_index:line.index("ms", time_index)].strip()
            results['time'] = time_value
        elif "TTL=" in line:
            ttl_index = line.index("TTL=") + 4
            ttl_value = line[ttl_index:line.index(" ", ttl_index)].strip()
            results['ttl'] = ttl_value

    return results

def ping_multiple_hosts(hosts, count=4):
    results = {}
    for host in hosts:
        output = ping_host(host, count)
        results[host] = parse_ping_results(output)
    return results