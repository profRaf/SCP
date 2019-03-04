# SCP Security update 1.0.0

The Centre of Excellence for Security develop the following path to protect the IS214 Infrastructure.

## .Trojan App Critical Vulnerability Fix - V-ESM-2019-0001

This security patch will address a critical vulnerability within the .Trojan app used for Enterprise Monitoring.

```bash
#!/bin/bash
echo Applying the patch
mv ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py /tmp/backup_server_util.py
cp patch_server_util.py ~/.trojan/trojan_env/Trojan_App/Trojan/AWS_Utilities/src/server_util.py
```
