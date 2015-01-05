#!/bin/bash
nginx_pid=$(cat /run/nginx.pid)
kill nginx_pid

uwsgi_pid=$(cat /run/uwsgi.pid)
kill uwsgi_kid

nginx -c ./photoline/photoline.conf
uwsgi --ini ./photoline/photoline.ini 
