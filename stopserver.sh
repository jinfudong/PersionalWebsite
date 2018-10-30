#!/bin/bash
PROJECTNAME='AXF'
ENV='GP01'
p="/home/$USER/.virtualenvs/$ENV/bin/activate"
source $p
uwsgi --stop uwsgi.pid
sudo nginx -s quit
echo "Done!"