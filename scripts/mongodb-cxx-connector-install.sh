#!/bin/bash
apt-get install git scons libboost-all-dev
git clone https://github.com/mongodb/mongo-cxx-driver.git
cd mongo-cxx-driver
git checkout 26compat
scons --full --use-system-boost --prefix=$HOME/dev/mcxxd install-mongoclient 

