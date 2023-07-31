import os, digitalocean

TOKEN = os.getenv('droplet')
manager = digitalocean.Manager(token=TOKEN)

# my_droplets = manager.get_all_droplets()
# for droplet in my_droplets:
#     print(droplet.load())

def all_droplets(manager):
    droplets = []
    all_droplets = manager.get_all_droplets()
    for droplet in all_droplets:
        print(str(droplet).split(' '))
        droplets.append({"id": (str(droplet).split(' '))[1]})
        droplets.append({"name": (str(droplet).split(' '))[2][:-1]})
    return droplets

def get_sshkeys(manager):
    keys = manager.get_all_sshkeys()
    ssh_keys = []
    for key in keys:
        ssh_keys.append({"id": (str(key).split(' '))[1], "name": (str(key).split(' '))[2][:-1]})
    return ssh_keys


def create_droplet(token, name, region, image, size, ssh_key, user_data):
    for key in get_sshkeys(manager=manager):
        if key['name'] == ssh_key:
            ssh_key_id = key['id']


    droplet = digitalocean.Droplet(
        token=token,
        name=name,
        region=region, 
        image=image, 
        size_slug=size,
        ssh_keys=[user_ssh],
        user_data=user_data
    )
    resp = droplet.create()
    return resp

create_droplet(
    token=TOKEN,
    name='NewDroplet',
    region='nyc1', 
    image='debian-12-x64', 
    size_slug='512mb',
    ssh_key='Linux'
    user_data="""

#!/bin/bash

sudo yum install epel-release -y
sudo yum install httpd -y
echo "This is my web-server" > /var/www/html/index.html
"""
)