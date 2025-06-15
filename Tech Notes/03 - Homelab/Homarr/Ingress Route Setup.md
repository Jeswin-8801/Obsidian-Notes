---
tags: [ingress,kubernetes,traefik]
---

</br>

> [!note] 
> Make sure Homarr is up and running (Refer [[Homarr Installation]])
> Also Traefik (Refer [[Traefik Installation|Traefik Installation]])

- Download necessary files
```bash ln:False
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Homarr/homarr-cert.yaml
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Homarr/homarr-ingress.yaml
```

- Apply cert config
```bash ln:False
kubectl apply -f homarr-cert.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n homarr get certs
> ```

- Apply ingress route config
```bash ln:False
kubectl apply -f homarr-ingress.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n homarr get ingressroute
> ```

</br>

> [!note] 
> Incase you want to revert the applied config, run:
> ```bash ln:False
> kubectl delete -f homarr-ingress.yaml
> ```