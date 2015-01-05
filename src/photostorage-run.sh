#!/bin/bash
kill -QUIT $(cat /run/nginx.pid)
kill -QUIT $(cat /run/uwsgi.pid)

nginx -c $PWD/photostorage/photostorage.conf
uwsgi --ini $PWD/photostorage/photostorage.ini 
