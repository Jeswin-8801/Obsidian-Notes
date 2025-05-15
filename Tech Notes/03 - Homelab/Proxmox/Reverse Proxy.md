---
tags: [proxmox,reverse-proxy]
---

</br>

- Install <mark style="background: #D2B3FFA6;">Nginx</mark>
```bash ln:False
sudo apt update
sudo apt install -y nginx
```

- Remove default config file
```bash ln:False
sudo rm -f /etc/nginx/sites-enabled/default
```

- Configure Nginx
```bash ln:False
sudo vim /etc/nginx/sites-available/proxmox.conf
```

> [!note] 
> The FQDN given below is as per what has been configured in my local DNS server.

```text
upstream proxmox {
    server "pve-home.proxmox.com";
}
 
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    rewrite ^(.*) https://$host$1 permanent;
}
 
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name _;
    ssl_certificate /etc/pve/local/pve-ssl.pem;
    ssl_certificate_key /etc/pve/local/pve-ssl.key;
    proxy_redirect off;
    location / {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass https://localhost:8006;
        proxy_buffering off;
        client_max_body_size 0;
        proxy_connect_timeout  3600s;
        proxy_read_timeout  3600s;
        proxy_send_timeout  3600s;
        send_timeout  3600s;
    }
}
```

- Check config file syntax
```bash ln:False
sudo nginx -t
```

- Restart Nginx
```bash ln:False
sudo systemctl restart nginx
```

- On bootup, ensure nginx starts only when the service <mark style="background: #D2B3FFA6;">pve-cluster.service</mark> has started
```bash ln:False
sudo systemctl edit nginx.service
```
add lines:
```text
[Unit]
Requires=pve-cluster.service
After=pve-cluster.service
```

**This is because the certificates that reside in `/pve/etc` is provided by this service.**

> [!error] 
> You might get the error:
> ```bash ln:False
> May 15 23:15:15 pve-hp nginx[49180]: 2025/05/15 23:15:15 [emerg] 49180#49180: host not found in upstream "pve-home.proxmox.com" in /etc/nginx/sites-enabled/proxmox.conf:LiBarChart2
> ```
> 
> You can easily verify this by:
> ```bash ln:False
> ping pve-home.proxmox.com
> ```
> 
> If this fails, it means that Nginx is unable to reach the local DNS server.

#### Solution

![[20250515233500_proxmox_node_dns_settings.png]]

> [!note] 
> Make sure your local DNS is made the primary DNS here over the gateway.