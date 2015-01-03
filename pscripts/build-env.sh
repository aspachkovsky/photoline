#!/bin/bash
apt-get install -y build-essential python-dev python-pip
pip install virtualenv
sudo mkdir -p /var/www/mysite
sudo chown -R aspachkovsky /var/www/mysite
cd /var/www/mysite
virtualenv .env --no-site-packages
source .env/bin/activate
pip install flask
pip install pymongo
pip install exifread
deactivate
apt-get install -y nginx uwsgi uwsgi-plugin-python
cd /tmp/
touch mysite.sock
chown www-data mysite.sock

