#!/bin/bash
PROJECTNAME='AXF'
ENV='GP01'
p="/home/$USER/.virtualenvs/$ENV/bin/activate"
source $p
uwsgi --ini uwsgi.ini
sudo nginx -c nginx.conf
echo "Done!"