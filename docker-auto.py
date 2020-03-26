import os
import time
import requests
import subprocess

def start():
    build()
    run()
    get_ip_curl()
    get_curl()

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
    port = ":3000"
    time.sleep(3)
    get_ip_cmd = "docker ps | grep saar | awk '{print $10}' | awk -F: '{print $1}'"
    id1 = "docker ps -a | grep seco | awk '{print $1}'"
    ip = subprocess.run(get_ip_cmd, shell=True, capture_output=True)
    get_id = subprocess.run(id1, shell=True, capture_output=True)
    new_ip = ip.stdout.decode().strip().lower()
    new_id = get_id.stdout.decode().strip().lower()
    exec1 = "docker exec -it new_id curl ip + port"
    get_exec = subprocess.run(docker exec -it new_id curl ip + port )
    #curl to ip
    url = requests.post("http://" + new_ip + port)
    #print("container id", get_id)
    print("\nThe answer is:", url.text)
    print("The container id is:", new_id)
    if url.text:
        print("the Container is ok!\n")
    else:
        print("the Container is not ok\n")
        
 def get_curl():
    port = ":3000"
    id1 = "docker ps | grep hour | awk '{print $1}'"
    get_ip_cmd = "docker ps | grep saar | awk '{print $10}' | awk -F: '{print $1}'"
    ip = subprocess.run(get_ip_cmd, shell=True, capture_output=True)
    new_ip = ip.stdout.decode().strip().lower()
    get_id = subprocess.run(id1, shell=True, capture_output=True)
    new_id = get_id.stdout.decode().strip().lower()
    ip_port = new_ip + ":3000"
    exec1 = "docker exec -it '" + new_id + "' curl '" + ip_port + "'"
    get_exec = subprocess.run(exec1, shell=True)
