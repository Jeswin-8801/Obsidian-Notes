
</br>


Used to query and view logs collected by [[Boot Process#5. Systemd|systemd]]’s logging service, known as the journal.

</br>

- **<mark style="background: #ABF7F7A6;">View All Logs</mark>**: To display all logs in chronological order:
```shell ln:False
journalctl
```

```shell ln:False
$ journalctl | grep -i error
Nov 13 06:09:08 ubuntu kernel: RAS: Correctable Errors collector initialized.
Nov 13 06:09:09 ubuntu multipathd[499]: uevent trigger error
Nov 13 06:09:19 ubuntu multipathd[499]: uevent trigger error
Nov 13 06:09:20 ubuntu systemd[1]: apport-autoreport.path - Process error reports when automatic reporting is enabled (file watch) was skipped because of an unmet condition check (ConditionPathExists=/var/lib/apport/autoreport).
Nov 13 06:09:20 ubuntu systemd[1]: apport-autoreport.timer - Process error reports when automatic reporting is enabled (timer based) was skipped because of an unmet condition check (ConditionPathExists=/var/lib/apport/autoreport).
Nov 13 06:09:22 ubuntu snapd[1077]: helpers.go:150: error trying to compare the snap system key: system-key missing on disk
Nov 13 06:09:29 ubuntu multipathd[499]: uevent trigger error
Nov 13 06:09:39 ubuntu multipathd[499]: uevent trigger error
```
    
- **<mark style="background: #ABF7F7A6;">Filter by Time</mark>**: To view logs from the last boot:
```shell ln:False
journalctl -b
```

- **<mark style="background: #ABF7F7A6;">Filter by Service</mark>**: To view logs for a specific service, such as `ssh`:
```bash ln:False
$ journalctl -u ssh
Nov 13 06:10:06 ubuntu systemd[1]: Starting ssh.service - OpenBSD Secure Shell server...
Nov 13 06:10:06 ubuntu sshd[1491]: Server listening on :: port 22.
Nov 13 06:10:06 ubuntu systemd[1]: Started ssh.service - OpenBSD Secure Shell server.
Nov 13 06:10:14 ubuntu sshd[1493]: Accepted password for jeswins from 192.168.182.1 port 57782 ssh2
Nov 13 06:10:14 ubuntu sshd[1493]: pam_unix(sshd:session): session opened for user jeswins(uid=1000) by jeswins(uid=0)
```
    
- **<mark style="background: #ABF7F7A6;">Real-Time Monitoring</mark>**: To follow new log entries as they appear:

```bash ln:False
journalctl -f
```