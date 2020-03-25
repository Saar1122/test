import os
import time
import click
import requests
import subprocess
#from learn import 


# url = 'http://demos.rele.ai'
# x = requests.post(url)
# print(x.text)
@click.command()
@click.option("--name", "-n", help="Your image name", prompt='your image name')
@click.option("--project", "-p", default="rele-saar", help="GCP project", prompt='your project name')
def start(name, project):
    # x = project, name
    build(name, project)
    run(name, project)
    get_ip_curl(name)

def build(name, project):
   '''
   build image
   '''
   make = "docker build . -t '" + name + "' "
   subprocess.run(make, shell=True)

def run(name, project):
   '''
   run docker
   '''
   run_docker = "docker run -p 3000:3000 -d '" + name + "'"
   subprocess.run(run_docker, shell=True)

def get_ip_curl(name):
    '''
    catch local ip and do curl
    '''
    time.sleep(3)
    get_ip_cmd = "docker ps | grep '" + name + "' | awk '{print $10}' | awk -F: '{print $1}'"
    ip = subprocess.run(get_ip_cmd, shell=True, capture_output=True)
    new_ip = ip.stdout.decode().strip().lower()
    port = ":3000"
    #curl to ip
    url = requests.post("http://" + new_ip + port)
    print("\nThe answer is:", url.text)
    if url.text:
        print("the Container is ok!\n")
    else:
        print("the Container is not ok\n")
