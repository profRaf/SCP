# Security update for SCP Build 1.0.0

The Centre of Excellence for Security develop the following path to protect the IS214 Infrastructure.

## .Trojan App Critical Vulnerability Fix - EVE-2019-0001

This security patch will address a critical vulnerability within the .Trojan app used for Enterprise Monitoring.
This patch also removes the potentially malicious 'root' file located in the home directory of the ec2-user account.

## Requirement
Make sure patch.sh and patch_server_util.py is in the same directory before performing the patch.

## Quick Patch:
```bash
bash patch.sh
```

## Manual patch
```bash
#!/bin/bash
rm ~/root
mv ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py /tmp/backup_server_util.py
cp patch_server_util.py ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py
sudo bash -c "fuser -k 8999/tcp"
nohup bash /home/ec2-user/.trojan/trojan_env/Trojan_App/bin/start.sh &>/dev/null &
```
