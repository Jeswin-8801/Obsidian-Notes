
Execute a command periodically and show output in full screen

```
watch uptime
```
⬇️
```
Every 2.0s:uptime                           ubuntu-server: Sun Sep 29 14:21:48 2024

 14:21:48 up 57 min,  1 user,  load average: 0.08, 0.04, 0.00
```
> Executes every 2 secs (default)

```
watch -n 5 uptime
```
> Executes every 5 seconds