#!/bin/bash

if [ "$(whoami)" != 'root' ]; then
    echo "Please run with sudo"
    exit 1;
fi


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ -d "$SCRIPT_DIR" ]; then
    cp "$SCRIPT_DIR"/rebooter.py /usr/bin/rebooter.py
    chmod +x /usr/bin/rebooter.py

    cp "$SCRIPT_DIR"/rebooter.service /lib/systemd/system/rebooter.service

    systemctl daemon-reload
    systemctl enable rebooter
    systemctl start rebooter
else
    echo "hm something wrong here"
    echo "$SCRIPT_DIR doesn't exist or something"
fi
