---
tags: [traefik, certmgr]
---

</br>

> [!note] 
> You must have cert manager setup with the required custom certs and keys. (Refer [[CertMgr Installation with Self Signed Certs]])

1. Copy the contents of <mark style="background: #ABF7F7A6;">tls.crt</mark> to a file in you local PC.

```bash ln:False
kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode
```

2. Import the cert

> Refer: [[Valid Self Signed Certificate#Import CA cert to device]]


On opening <mark style="background: #FFB86CA6;">cert mgr</mark> on windows, you will find it under Root Certs named as the secret name you configured the key and certs with.
