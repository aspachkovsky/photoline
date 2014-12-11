grep -q -F 'deb http://ppa.launchpad.net/yandex-load/main/ubuntu trusty main' /etc/apt/sources.list || echo 'deb http://ppa.launchpad.net/yandex-load/main/ubuntu trusty main' >> /etc/apt/sources.list

grep -q -F 'deb-src http://ppa.launchpad.net/yandex-load/main/ubuntu trusty main' /etc/apt/sources.list || echo 'deb-src http://ppa.launchpad.net/yandex-load/main/ubuntu trusty main' >> /etc/apt/sources.list

apt-get install python-software-properties
apt-get install software-properties-common
add-apt-repository ppa:yandex-load/main
apt-get update
apt-get install yandex-load-tank-base

