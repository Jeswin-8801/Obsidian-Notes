---
tags: [monitoring]
---

> [!important] 
> If you are using Self Signed Certs, ass the custom Root CA cert to the Uptime Kuma Instance. (Refer: [[Add Custom CA]])

</br>

## Pi-Hole 

#### DNS

- Add the following config:
```yaml ln:False
Monitor Type: DNS
Hostname: x.home.local # (hostname to resolve, preferably a local service)
Resolver Server: 192.168.0.40 # (your pi-hole IP address)
Port: 53
Resource Record Type: A # (might vary based on the hostname you want to resolve)
```

#### Dashboard

> Checkout [[PiHole Installation|Pi-Hole]] docs at [Pi-hole API documentation](https://pi-hole.home.local/api/docs/)
> ***(Must have pihole hosted at the given URL)***

> Negation of
> https://pi-hole.home.local/api/auth


</br>

## Rancher

> https://rancher.home.local/healthz


</br>

## Traefik

> https://traefik.home.local/ping

</br>

## Homarr

> https://homarr.home.local/api/health/live