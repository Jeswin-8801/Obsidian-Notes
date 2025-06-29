---
tags: [database, helm]
---

#### 1. Go to Project Directory

```bash ln:False
cd ./ClickHouse
```

#### 2. Add your secret

- below script adds the admin password as base 64 encoded string in `clickhouse-secret.yaml`

```bash ln:False
PASSWORD=""
sed -i "s/<base64-encoded-password>/$(echo -n ${PASSWORD} | base64)/g" clickhouse-secret.yaml
```

#### 3. Apply Configs

```bash ln:False
kubectl apply -k .
```

#### 4. Install ClickHouse

```bash ln:False
helm install clickhouse oci://registry-1.docker.io/bitnamicharts/clickhouse \
	--version 4.1.12 \
	-n clickhouse \
	-f values.yaml
```

