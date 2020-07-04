#!/bin/sh
### BEGIN INIT INFO
# Provides:          Agent
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Source:            Youtube EddyCarra
# Short-Description: Python Agent Service
# Description:       Starts up the environment for MonitorApp
### END INIT INFO

MAIN_PATH=<MAIN/PATH/TO/WORKINGDIR>
PYTHON=$MAIN_PATH/venv/bin/python3
DAEMON=<PATH/TO/PYTHON_CODE.py>
DAEMON_NAME=monitor_agent

DAEMON_USER=<USER NAME>

PIDFILE=/run/$DAEMON_NAME.pid
. /lib/lsb/init-functions

do_start () {
    log_daemon_msg "Starting system $DAEMON_NAME daemon"
    start-stop-daemon --start --quiet --background --make-pidfile --pidfile $PIDFILE \
    --exec $DAEMON || log_failure_msg " already running"
    log_end_msg $?
}
do_stop () {
    log_daemon_msg "Stopping system $DAEMON_NAME daemon"
    start-stop-daemon --stop --oknodo --user $DAEMON_USER \
    --pidfile $PIDFILE --retry 5
    log_end_msg $?
}
case "$1" in
    start|stop)
        do_${1}
        ;;
    restart|reload|force-reload)
        do_stop
        do_start
        ;;
    status)
        status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
        ;;
    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
        exit 1
        ;;
esac
exit 0