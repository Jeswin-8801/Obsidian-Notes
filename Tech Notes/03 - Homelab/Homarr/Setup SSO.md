---
tags: [SSO, OIDC, Zitadel, kubernetes, ]
---

> [!important] 
> - Complete [[Homarr Installation]] and [[Zitadel Istallation]] before continuing with the steps below.
> - The group name on initial setup `admin` must be different from other groups `default` which we will be creating later in [[Zitadel Istallation|Zitadel]]:
> 	![[20250621231943_homarr_group_name_setup.png]]

</br>

#### 1. Go to Project Dir

```bash ln:False
cd ./Homarr
```

> Modify required Params in `values_sso.yaml`
> Refer: [values.yaml · homarr-labs/charts](https://github.com/homarr-labs/charts/blob/dev/charts/homarr/values.yaml)

</br>

#### 2. Configure Application in Zitadel

> Refer: [[Zitadel Application Setup]]

</br>

#### 3. Create Secret

```bash ln:False
kubectl create secret generic auth-oidc-secret \
  --from-literal=oidc-client-id=<your-client-id> \
  --from-literal=oidc-client-secret=<your-client-secret> \
  -n homarr
```

> Verify using
> ```bash ln:False
> kubectl get secret auth-oidc-secret \
> 	-n homarr \
> 	-o yaml
> ```

</br>

#### 4. Add root CA from cert-mgr

> [!note] 
> Add this only if you are using self signed certs

```bash ln:False
kubectl create secret generic my-root-ca-secret \
	--from-literal=tls.crt="$(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode)" \
	-n homarr
```

> Verify using:
> ```bash ln:False
> kubectl -n homarr get secrets
> ```

</br>

#### 5. Bring down Pods

```bash ln:False
kubectl -n homarr scale deploy --all --replicas=0
```

#### 6. Upgrade with new Values file

```bash ln:False
helm upgrade homarr oci://ghcr.io/homarr-labs/charts/homarr \
  --namespace homarr \
  -f values_sso.yaml
```

</br>

---

> [!bug] 
> <mark style="background: #ABF7F7A6;">Temporary</mark>
> Quick fix for issue [bug: Issue #123 · homarr-labs/charts](https://github.com/homarr-labs/charts/issues/123)
> ```bash ln:False
> kubectl exec -i -n homarr deploy/homarr -- sh -c 'cat > /appdata/trusted-certificates/tls.crt' <<< "$(kubectl -n homarr get secret my-root-ca-secret -o yaml | grep -oP "tls\.crt: \K.*$" | base64 --decode)"
> ```