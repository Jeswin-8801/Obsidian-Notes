---
tags: [database, kubernetes, helm]
---

</br>

#### 1. Go to Project directory

```bash ln:False
cd ./PostgreSQL/pgAdmin4
```

#### 2. Add Helm Chart

```bash ln:False
helm repo add runix https://helm.runix.net
```

#### 3. Install pgAdmin4

> [!note] 
> The namespace has been created in [[Postgres Installation]]
> Also, remember to update the required secrets in `values.yaml`

```bash ln:False
helm install pgadmin4 runix/pgadmin4 \
  --namespace postgres \
  -f values.yaml
```


#### 4. Add TLS Certs
```bash ln:False
kubectl apply -f pgadmin-cert.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n postgres get certs
> ```

</br>

#### 5. Apply ingress route config
```bash ln:False
kubectl apply -f pgadmin-ingress.yaml
```

> Verify using:
> ```bash ln:False
> kubectl -n postgres get ingressroute
> ```

</br>

#### 6. Add FQDN to local DNS
Add `pgadmin4.home.local` to local DNS and map it to [[What is Traefik]] IP.

</br>

---

</br>

> [!danger] 
> To completely uninstall the app, run:
> ```bash ln:False
> helm uninstall pgadmin4 --namespace postgres
> ```
