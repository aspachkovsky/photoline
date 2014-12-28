#!/bin/bash
apt-key adv --fetch-keys http://repos.codelite.org/CodeLite.asc
apt-add-repository 'deb http://repos.codelite.org/ubuntu/ trusty universe'
apt-get update
apt-get install codelite wxcrafter
