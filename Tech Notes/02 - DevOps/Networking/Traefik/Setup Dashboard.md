---
tags: [traefik,ingress,kubernetes]
---

</br>

- Download required files
```bash ln:False
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Kubernetes/Traefik/traefik-dashboard-cert.yaml
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Kubernetes/Traefik/traefik-dashboard-ingress.yaml
```

- Apply cert config
```bash ln:False
kubectl apply -f traefik-dashboard-cert.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n homarr get certs
> ```

- Apply ingress route config
```bash ln:False
kubectl apply -f traefik-dashboard-ingress.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n traefik get ingressroute
> ```