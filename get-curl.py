import os
import time
import click
import requests
import subprocess

def get_curl():
    port = ":3000"
    id1 = "docker ps | grep seco | awk '{print $1}'"
    get_ip_cmd = "docker ps | grep saar | awk '{print $10}' | awk -F: '{print $1}'"
    ip = subprocess.run(get_ip_cmd, shell=True, capture_output=True)
    new_ip = ip.stdout.decode().strip().lower()
    get_id = subprocess.run(id1, shell=True, capture_output=True)
    new_id = get_id.stdout.decode().strip().lower()
    ip_port = new_ip + ":3000"
    exec1 = "docker exec -it '" + new_id + "' curl '" + ip_port + "'"
    get_exec = subprocess.run(exec1, shell=True)

# if __name__ == "__main__":
#     get_curl()
