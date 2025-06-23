---
tags: [authentication, middleware, kubernetes, ]
---

#### 1. Go to Project Directory

```bash ln:False
cd ./TinyAuth
```

#### 2. Generate Secret and Place in `secrets.yaml`

```bash ln:False
sed -i "s|<your_base64_encoded_key>|$(openssl rand -base64 24 | tr -d '\n' | base64)|g" secrets.yaml
```

> [!note] We are giving 24 bytes as:
> - Base64 takes **every 3 bytes** (24 bits) and turns them into **4 characters**
> - So, for `24 bytes`:
> $$
> \frac{24 \text{ bytes}}{3} \times 4 = 32 \text{ characters}
> $$

</br>

#### 3. Place Client ID and Client Secret into `secrets.yaml`

> Refer: [[Zitadel Config]] to setup and obtain them.

**Add your `CLIENT_ID` and `CLIENT_SECRET` in the script below and execute it**

```bash
CLIENT_ID=""
CLIENT_SECRET=""
sed -i "s/<your_client_id>/$(echo -n ${CLIENT_ID} | base64)/g" secrets.yaml
sed -i "s/<your_client_secret>/$(echo -n ${CLIENT_SECRET} | base64 -w 0)/g" secrets.yaml
```


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