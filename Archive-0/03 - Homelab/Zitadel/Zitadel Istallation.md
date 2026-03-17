---
tags: [CIAM,kubernetes,helm]
---

</br>

#### 1. Got to project directory

```bash ln:False
cd ./Zitadel
```


#### 2. Add Helm Repo

```bash ln:False
helm repo add zitadel https://charts.zitadel.com
```

#### 3. Create Namespace

```bash ln:False
kubectl create namespace zitadel
```

#### 4. Generate Master Key Secret

```bash ln:False
kubectl create secret generic zitadel-masterkey \
	--from-literal=masterkey="$(tr -dc A-Za-z0-9 </dev/urandom | head -c 32)" \
	-n zitadel
```

> [!info] Why annotate as generic?
> - It's a shorthand in `kubectl` to create a secret of type `Opaque`.
> - `Opaque` is the default, flexible type for arbitrary secrets (like passwords, tokens, keys).

***Print the raw secret (base64-encoded)***
```bash ln:False
kubectl get secret zitadel-masterkey \
	-n zitadel \
	-o yaml
```

#### 5. Add a PVC

```bash ln:False
kubectl apply -f zitadel-pvc.yaml
```

#### 6. Install Zitadel

Before using `values.yaml`, modify any required secrets and usernames

> [!note] 
> Refer the configs created in [[Postgres Installation]] and make sure the values match.
> 
> We are directly referring to the Postgres Instance by its internal FQDN as we have not and will not expose it.
> 
> The User section defines a user to be created with the given password if not already.

```bash ln:False
helm install my-zitadel zitadel/zitadel \
	--namespace zitadel \
	-f values.yaml
```

*This might take some time*

> Verify using
> ```bash ln:False
> kubectl -n zitadel get all
> ```

</br>

#### 7. Add Certs

```bash ln:False
kubectl apply -f zitadel-cert.yaml
```

> Verify using
> ```bash ln:False
> kubectl -n zitadel get certs
> ```

</br>

#### 8. Apply Ingress Route

```bash ln:False
kubectl apply -f zitadel-ingress.yaml
```

> Verify using
> ```bash ln:False
> kubectl -n zitadel get ingressroute
> ```

> [!note] 
> Do not forget to add the FQDN `zitadel.home.local` to your local DNS.