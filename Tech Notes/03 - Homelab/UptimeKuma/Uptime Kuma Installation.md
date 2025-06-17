---
tags: [helm,homelab]
---

</br>

- Add Helm repo
```bash ln:False
helm repo add uptime-kuma https://helm.irsigler.cloud
```

- Go to the project directory
```bash ln:False
git clone https://github.com/Jeswin-8801/HomeLab.git
cd HomeLab/UptimeKuma
```

> [!important] 
> Add the required custom Root CA certs if being used for probing to work.
> Refer: [[Add Custom CA]]

- Install Uptime Kuma
```bash ln:False
helm install my-uptime-kuma uptime-kuma/uptime-kuma \
	--namespace monitoring \
	--create-namespace \
	-f values.yaml
```

- Create tls secret
```bash ln:False
kubectl apply -f uptime-kuma-cert.yaml
```

> Verify using
> ```bash ln:False
> kubectl -n monitoring get certs
> ```

- Apply Ingress Route
```bash ln:False
kubectl apply -f uptime-kuma-ingress.yaml
```

> Verify using
> ```bash ln:False
> kubectl -n monitoring get ingressroute
> ```

> [!note] 
> Do not forget to add the FQDN `uptime-kuma.home.local` to your local DNS.