---
tags: [dns]
---

#### Check how DNS is managed

```bash ln:False
readlink /etc/resolv.conf
```

If it returns `/run/systemd/resolve/stub-resolv.conf`
✅ You're using `systemd-resolved`

#### Go to all VMs and Run:

- Create the config directory if needed:
```bash ln:False
sudo mkdir -p /etc/systemd/resolved.conf.d
```

- Create the drop-in file and paste the following contents
```bash ln:False title:/etc/systemd/resolved.conf.d/custom-dns.conf
[Resolve]
DNS=192.168.0.40
FallbackDNS=1.1.1.1 8.8.8.8
```

- Restart service
```bash ln:False
sudo systemctl restart systemd-resolved
```

- Verify
```bash ln:False
resolvectl status
```
