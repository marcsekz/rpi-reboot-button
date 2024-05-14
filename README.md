# rpi-reboot-button
Reboot  button for Raspberry Pi

## Install
1. Set the pin you want to use in line 9 of `rebooter.py` (stopPin)
2. Run `install.sh`

## Uninstall
Run the following as root or with sudo:
```bash
systemctl stop rebooter
systemctl disable rebooter
rm /lib/systemd/system/rebooter.service
rm /usr/bin/rebooter.py
```