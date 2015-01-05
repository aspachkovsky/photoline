#!/bin/bash
PWDIR=$(pwd)
BASEDIR="/var/www/photoline"
USER="aspachkovsky"
ENVDIR=".env"
SRCDIR="$PWDIR/photoline/src"
mkdir -p "$BASEDIR"
chown -R "$USER" "$BASEDIR"
cd "$BASEDIR"
virtualenv "$ENVDIR" --no-site-packages
source "$ENVDIR/bin/activate"
$ENVDIR/bin/pip install flask
$ENVDIR/bin/pip install pymongo 
deactivate
cd "$PWDIR"
ln -s $SRCDIR "$BASEDIR" 



