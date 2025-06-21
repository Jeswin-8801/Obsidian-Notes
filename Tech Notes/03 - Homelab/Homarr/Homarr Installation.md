---
tags: [dashboard,homelab]
---

> [!note] 
> This tutorial only goes through setting up and exposing through MetalLB. Refer [[Ingress Route Setup]] to expose using Traefik.

</br>

#### 1. Get `values.yaml`

```bash ln:False
mkdir -p Homarr
cd Homarr
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Homarr/values.yaml
```

#### 2. Create Namespace

```bash ln:False
kubectl create namespace homarr
```

#### 3. Setup `database-key` secret

> [!warning] 
> `database-key` variable must be set before bringing up this service.
> Refer: [Homarr - homarr Helm Charts](https://homarr-labs.github.io/charts/charts/homarr/#pvc)
> 
> ```bash ln:False
> kubectl create secret generic db-secret \
> --from-literal=db-encryption-key="$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 64
)" \
> --namespace homarr
> ```

- Expose IP through LB
```bash ln:False
kubectl expose deployment homarr --name homarr-lb --port=80 --target-port=7575 --type=LoadBalancer -n homarr homarr-lb exposed
```

#### 4. Install using Helm Chart

> [!note] If you do not want to expose this app using metalLB and use traefik ingress instead with/without SSO, refer [[Ingress Route Setup]] and [[Setup SSO]] before running `helm install`

```bash ln:False
helm install homarr oci://ghcr.io/homarr-labs/charts/homarr \
  --namespace homarr \
  --create-namespace \
  -f values.yaml
```

- Verify deployment
```bash ln:False
$ kubectl get deployments -n homarr
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
homarr   0/1     1            0           24s
```

> [!note] 
> Now you will be asked to create a new user. This will be the admin user internal to <mark style="background: #ADCCFFA6;">Homarr</mark>.

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
