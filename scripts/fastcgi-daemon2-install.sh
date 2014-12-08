mkdir Fastcgi-Daemon-install
cd Fastcgi-Daemon-install
apt-get install -y build-essential git debhelper automake1.9 autotools-dev libboost-dev libboost-thread-dev libfcgi-dev libxml2-dev libboost-regex-dev libtool libssl-dev autoconf-archive
git clone https://github.com/lmovsesjan/Fastcgi-Daemon.git
cd Fastcgi-Daemon
dpkg-buildpackage -rfakeroot
cd ..
dpkg -i libfastcgi-daemon2-dev_2.10-26_amd64.deb libfastcgi-daemon2_2.10-26_amd64.deb fastcgi-daemon2-init_2.10-26_amd64.deb fastcgi-daemon2_2.10-26_amd64.deb libfastcgi2-syslog_2.10-26_amd64.deb
cd .. 
rm Fastcgi-Daemon-install -rf