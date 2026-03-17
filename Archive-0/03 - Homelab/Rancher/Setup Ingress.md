---
tags: [ingress,traefik,kubernetes,rancher]
---

</br>

- remove current ingress
```bash ln:False
kubectl delete certificate tls-rancher-ingress -n cattle-system
kubectl delete secret tls-rancher-ingress -n cattle-system
```

- delete any LB service if any
```bash ln:False
kubectl delete svc rancher-lb -n cattle-system
```

- Download files
```bash ln:False
mkdir Rancher && cd Rancher
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/Kubernetes/Traefik/rancher-cert.yaml
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/Kubernetes/Traefik/rancher-ingress.yaml
```

- Apply cert config
```bash ln:False
kubectl apply -f rancher-cert.yaml
```

> Verify it has been created successfully
> ```bash ln:False
> kubectl -n cattle-system get certs
> ```
> Confirm by checking for `Ready: True`
>
> If not, debug using:
> ```bash ln:False
> kubectl describe certificaterequest rancher-custom-cert-1 -n cattle-system
> ```

- Apply Ingress Config
```bash ln:False
kubectl apply -f rancher-ingress.yaml
```