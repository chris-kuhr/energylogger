energylogger
============

Energenie Python Energylogger 

http://energenie.com/item.aspx?id=6736&lang=de

First, enter Ip address and Energenie password in energylogger.py.


Modify (the path you want to use) and register upstart script:

sudo update-rc.d energylogger.sh defaults


watch latest log entries:

tail -f energy.log

