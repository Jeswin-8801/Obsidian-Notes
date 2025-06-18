---
tags: [database,homelab,kubernetes,]
---

</br>

> Referring tutorial [How to Deploy Postgres to Kubernetes Cluster | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-deploy-postgres-to-kubernetes-cluster)

</br>

#### 1. Go to project directory
```bash ln:False
cd ./PostgreSQL/PostgreSQL
```

</br>

#### 2. Create Namespace
```bash ln:False
kubectl create namespace postgres
```

</br>

#### 3. Apply ConfigMap

> [!attention] 
> Update the file `psql-configmap.yaml` with the required secrets before proceeding.

```bash ln:False
kubectl apply -f psql-configmap.yaml
```

Verify using:
```bash ln:False
kubectl -n postgres get configmap
```

</br>

#### 4. Apply PersistantVolumeClaim
```bash ln:False
kubectl apply -f psql-pvc.yaml
```

Verify using:
```bash ln:False
kubectl -n postgres get pvc
```
***Refer: [[PV and PVC]]***

> [!note] 
> We do not need to create a PersistantVolume as [[Longhorn Installation|Longhorn]] handles it for us

</br>

#### 5. Apply Deployment Config
```bash ln:False
kubectl apply -f psql-deployment.yaml
```

Verify using:
```bash ln:False
kubectl -n postgres get deployments
```

Debug:
```bash ln:False
kubectl -n postgres describe pod $(kubectl -n postgres get pods | grep "postgres" | awk -F" " '{ printf $1 }')
```

Get Pod Logs:
```bash ln:False
kubectl -n postgres logs $(kubectl -n postgres get pods | grep "postgres" | awk -F" " '{ printf $1 }')
```

Incase you get Mount Failed, try installing `nfs-commn` in all longhorn nodes:
```bash ln:False
sudo apt install -y nfs-common
```

</br>

#### 6. Create a service
```bash ln:False
kubectl apply -f psql-service.yaml
```

Verify using:
```bash ln:False
kubectl -n postgres get svc
```

> [!note] 
> We are not exposing this service but are using it as is internally by the fqdn `<service-name>.<namespace>.svc.cluster.local`





