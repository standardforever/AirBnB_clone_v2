#!/usr/bin/env bash
# It set up a web servers for the deployment of web_static
sudo apt -y update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo 'Hello World!' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
