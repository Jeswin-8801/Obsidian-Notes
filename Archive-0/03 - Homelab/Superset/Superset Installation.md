---
tags: [metrics, helm, kubernetes, ]
---

#### 1. Go to Project Folder

```bash ln:False
cd ./Superset
```

#### 2. Add secrets to `superset-secrets.yaml`

> Refer: [[Zitadel Configuration]] to setup and obtain <mark style="background: #D2B3FFA6;">Client Id</mark> and <mark style="background: #D2B3FFA6;">Client Secret
</mark>
**Add your `CLIENT_ID` and `CLIENT_SECRET` in the script below and execute it**

```bash
CLIENT_ID=""
CLIENT_SECRET=""
sed -i "s|<your_base64_encoded_key>|$(openssl rand -base64 42 | tr -d '\n' | base64)|g" secrets.yaml
sed -i "s/<your_client_id>/$(echo -n ${CLIENT_ID} | base64)/g" secrets.yaml
sed -i "s/<your_client_secret>/$(echo -n ${CLIENT_SECRET} | base64 -w 0)/g" secrets.yaml
```

#### 3. Create Database in Postgres

- Login into [[pgAdmin4 Installation|pgAdmin4]]
- Create a new database called <mark style="background: #D2B3FFA6;">superset</mark>

#### 4. Add root CA from cert-manager

> [!note] 
> Required if you are using self signed certs

```bash ln:False
sed -i "s/<BASE64_ENCODED_CERT>/$(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}')/g" root-ca-secret.yaml
```

#### 5. Apply configs

```bash ln:False
kubectl apply -k .
```

#### 6. Add Helm Repo

```bash ln:False
helm repo add superset http://apache.github.io/superset/
```

#### 7. Install Superset

```bash ln:False
helm install my-superset superset/superset \
	--version 0.14.2 \
	-n superset \
	-f values.yaml
```
