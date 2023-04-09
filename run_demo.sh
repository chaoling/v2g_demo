#!/bin/sh
echo "start demo app..."
cd /home/firekirin/Documents/prototype
echo $pwd
DISPLAY=:0 /usr/bin/xterm -fs 14 -fa DejaVuSansMono -hold -e /usr/bin/python3 demo1.py
echo "app started"
