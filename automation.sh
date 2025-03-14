#!/bin/bash

LOG_FILE="/var/log/ids_alerts.log"

# Function to check for multiple failed connections
check_intrusions() {
    tail -n 100 /var/log/syslog | grep "Failed password" > $LOG_FILE
    COUNT=$(wc -l < $LOG_FILE)
    
    if [ "$COUNT" -gt 5 ]; then
        echo "[ALERT] Multiple failed attempts detected!" | mail -s "IDS Alert" admin@example.com
    fi
}

while true; do
    check_intrusions
    sleep 60
done
