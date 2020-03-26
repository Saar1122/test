import os
import time
import requests
import subprocess

def start():
    build()
    run()
    get_ip_curl()

def build():
   '''
   build image
   '''
   make = "docker build . -t saar"
   subprocess.run(make, shell=True)

def run(name, project):
   '''
   run docker
   '''
   run_docker = "docker run -p 3000:3000 -d saar"
   subprocess.run(run_docker, shell=True)

def get_ip_curl():
    '''
    catch local ip and do curl
    '''
    time.sleep(3)
    get_ip_cmd = "docker ps | grep saar | awk '{print $10}' | awk -F: '{print $1}'"
    id = "docker ps -a | grep seco | awk '{print $1}'"
    ip = subprocess.run(get_ip_cmd, shell=True, capture_output=True)
    get_id = subprocess.run(id, shell=True, capture_output=True)
    new_ip = ip.stdout.decode().strip().lower()
    new_id = get_id.stdout.decode().strip().lower()
    port = ":3000"
    #curl to ip
    url = requests.post("http://" + new_ip + port)
    #print("container id", get_id)
    print("\nThe answer is:", url.text)
    print("The container id is:", new_id)
    if url.text:
        print("the Container is ok!\n")
    else:
        print("the Container is not ok\n")

