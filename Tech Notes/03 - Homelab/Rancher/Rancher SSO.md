---
tags: [OIDC, SSO, Zitadel]
---

#### 1. Add custom CA

```bash ln:False
kubectl -n cattle-system create secret generic tls-ca-additional --from-literal=ca-additional.pem="$(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode)"
```

#### 2. Upgrade

```bash ln:False
cd Kubernetes/Rancher
helm upgrade rancher rancher-stable/rancher \
	-n cattle-system \
	-f values.yam
```

#### 3. Setup App in [[Zitadel Istallation|Zitadel]]

- Select <mark style="background: #CACFD9A6;">WEB</mark>
- Select auth as <mark style="background: #CACFD9A6;">CODE</mark>
- Redirect URI: `https://rancher.home.local/verify-auth`
- Post Logout URI: `https://rancher.home.local/dashboard/auth/logout`

#### 4. Setup OIDC in Rancher

- select <mark style="background: #D2B3FFA6;">Generic OIDC</mark>

![[20250626001442_Rancher_OIDC.png]]

- enter configurations including <mark style="background: #ABF7F7A6;">Client ID</mark> and <mark style="background: #ABF7F7A6;">Client Secret</mark>

![[20250626003607_rancher_oidc_config.png]]