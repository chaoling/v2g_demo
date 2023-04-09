# v2g_demo
a v2g demo project using rpi
the script is located in Document folder
and prototype folder.
the shell script run_demo.sh is used by
systemd file demo.service to start the 
app automatically upon boot of rpi.
place it in /lib/systemd/system/demo.service
make sure it is also linked in /etc/systemd/system/...
and /usr/bin/run_demo.sh
copy the pyton script to ~/Documents/prototype/demo1.py
