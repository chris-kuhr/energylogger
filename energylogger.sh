#! /bin/sh

### BEGIN INIT INFO
# Provides:          energylogger.py
# Required-Start:    $network $local_fs $remote_fs
# Required-Stop:     $network $local_fs $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Should-Start:      python
# Should-Stop:       python
# Short-Description: start energylogger
### END INIT INFO

cd /home/pi/energylogger
python /home/pi/energylogger.py &
cd ~
