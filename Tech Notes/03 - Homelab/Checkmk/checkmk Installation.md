---
tags: [kubernetes, monitoring, ]
---

#### 1. Go to Project Directory

```bash ln:False
cd ./Checkmk
```

#### 2. Add your password in `secrets.yaml`

> Replace `<your-super-secure-password>` with your password.

</br>

#### 3. Add root CA from cert-manager

> [!note] 
> Required if you are using self signed certs

```bash ln:False
sed -i "s/<BASE64_ENCODED_CERT>/$(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}')/g" root-ca-secret.yaml
```

#### 4. Apply all Configs

```bash ln:False
kubectl apply -k .
```

> [!note] 
> This may take some time if the image is getting pulled for the first time.
> ```bash ln:False
> Successfully pulled image "checkmk/check-mk-raw:2.3.0-2025.06.27" in 14m43.958s (14m43.958s including waiting). Image size: 696398088 bytes
> ```
