---
tags: [networking, homelab]
---

</br>

==Traefik== is a modern HTTP reverse **proxy** and load balancer.

Similar known tools: ==Nginx==, ==Apache web server==

|Role|Description|
|---|---|
|🔁 **Reverse Proxy**|Routes external traffic to internal services|
|🌐 **Ingress Controller**|Acts as the entry point in Kubernetes for HTTP/HTTPS|
|🔐 **TLS Termination**|Handles SSL certs (often via cert-manager)|
|🛣️ **Routing / Load Balancing**|Path-based or host-based routing to services|
|🔒 **Security Middleware**|Can integrate auth, rate limiting, headers|
|📈 **Observability**|Metrics, tracing, logging for traffic flows|

> [!info] 
> Checkout installation at [[Traefik Installation]]