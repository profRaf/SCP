#!/bin/bash
echo Applying the patch
rm ~/root
mv ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py /tmp/backup_server_util.py
cp patch_server_util.py ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py
sudo bash -c "fuser -k 8999/tcp"
nohup bash /home/ec2-user/.trojan/trojan_env/Trojan_App/bin/start.sh &>/dev/null &