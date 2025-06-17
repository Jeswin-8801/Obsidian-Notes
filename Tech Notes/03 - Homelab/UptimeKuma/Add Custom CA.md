---
tags: [monitoring,networking]
---

> [!note] 
> <mark style="background: #ABF7F7A6;">Uptime Kuma</mark> will not be able to send requests to web services through REST endpoints due to untrusted cert.
> 
> Although we have imported the Root CA to our system and configured cert-manager to use it, Uptime Kuma internally cannot have access to it, therefore the requests fail.

</br>

1. Create `tls.crt` referring Root CA by using the commands in:
> [[CertMgr Installation with Self Signed Certs#Access Certs and Keys]]

</br>

2. Create configmap
```bash ln:False
kubectl create configmap kuma-custom-ca \
  --from-file=custom-ca.crt=./tls.crt \
  -n monitoring
```

> Verify using:
> ```bash ln:False
> kubectl -n monitoring get configmap kuma-custom-ca -o yaml
> ```

*Continue following the setup steps in [[Uptime Kuma Installation]]*

</br>

3. Update deployment
> Incase you are updating from a previous installation, run:

```bash ln:False
helm upgrade --install my-uptime-kuma uptime-kuma/uptime-kuma \
  -n monitoring \
  -f values.yaml
```

</br>

4. Verify Mount

```bash ln:False
kubectl -n monitoring exec -it deployment.apps/my-uptime-kuma -- cat /etc/ssl/certs/custom-ca.crt
```