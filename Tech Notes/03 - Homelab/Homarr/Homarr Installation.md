---
tags: [dashboard,homelab]
---

</br>

- Get values.yml and use it in the command below
```bash ln:False
mkdir -p Homarr
cd Homarr
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Homarr/values.yaml
```

- Install through Helm Chart
```bash ln:False
helm install homarr oci://ghcr.io/homarr-labs/charts/homarr \
  --namespace homarr \
  --create-namespace \
  --set env.TZ="India/Kolkata" \
  -f values.yaml
```

- Verify deployment
```bash ln:False
$ kubectl get deployments -n homarr
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
homarr   0/1     1            0           24s
```

> [!warning] 
> `database-key` variable must be set before bringing up this service.
> Refer: [Homarr - homarr Helm Charts](https://homarr-labs.github.io/charts/charts/homarr/#pvc)
> 
> ```bash ln:False
> kubectl create secret generic db-secret \
> --from-literal=db-encryption-key='54150e41b3512bd451902b4c6ce179f732825b3b9facd18ce54c65b3741eb5d3' \
> --namespace homarr
> ```

- Expose IP through LB
```bash ln:False
kubectl expose deployment homarr --name homarr-lb --port=80 --target-port=7575 --type=LoadBalancer -n homarr homarr-lb exposed
```

</br>

## Debug

- Pod
```bash ln:False
kubectl get pods -A | grep homarr
```

```bash ln:False
kubectl describe pod $(kubectl get pods -A | grep homarr | awk -F' ' '{print$2}') -n homarr
```

- Service
```bash ln:False
kubectl get svc -n homarr
```

```bash ln:False
kubectl describe svc homarr-lb -n homarr
```
