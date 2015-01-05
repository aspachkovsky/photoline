#!/bin/bash
PWDIR=$(pwd)
BASEDIR="/var/www/photostorage"
USER="aspachkovsky"
ENVDIR=".env"
SRCDIR="$PWDIR/photostorage/src"
mkdir -p "$BASEDIR"
chown -R "$USER" "$BASEDIR"
cd "$BASEDIR"
virtualenv "$ENVDIR" --no-site-packages
source "$ENVDIR/bin/activate"
pip install flask
pip install pymongo  
deactivate
cd "$PWDIR"
ln -s $SRCDIR "$BASEDIR" 



