---
tags: [statistics, metrics, kubernetes, ]
---

#### 1. Go to Project Directory

```bash ln:False
cd ./Metabase
```

#### 2. Create DB in Postgres

> Create the database `metabase` (as configured in `configmap.yaml`)

</br>

#### 3. Modify Secrets and Env Variables

Modify the following files:

- `secrets.yaml` ([[Postgres Installation|Postgresql]] username and password)
- `configmap.yaml` (Postgres config variables)

#### 4. Install Metabase

```bash ln:False
kubectl apply -k .
```

#### 5. Setup [[ClickHouse Installation|ClickHouse]]

- Add database <mark style="background: #D2B3FFA6;">ClickHouse</mark>

Set the following details:


| Field                                            | Value                                                      |
| ------------------------------------------------ | ---------------------------------------------------------- |
| <mark style="background: #CACFD9A6;">Host</mark> | `clickhouse.clickhouse.svc.cluster.local`                  |
| Port                                             | 8123                                                       |
| Username                                         | admin                                                      |
| Password                                         | [[ClickHouse Installation\|Password set in Installation]]  |
| Database                                         | default                                                    |


