---
tags: [homelab,helm,kubernetes]
---

</br>

> [!note]
> This sections follows through the tutorial in [Install/Upgrade Rancher on a Kubernetes Cluster | Rancher](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster#1-add-the-helm-chart-repository)

** Run the following sections of code on the separate VM that was created to setup the HA cluster in [[K3s Setup#Configuring VMs as a HA Kubernetes cluster]] **

## Installing from script

> This is as specified in the official website [Helm | Installing Helm](https://helm.sh/docs/intro/install/)

```bash ln:False
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

</br>

## Initialize a Helm Chart Repository

> Refer: [Rancher | Add Helm Chart Repository](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster#1-add-the-helm-chart-repository)

```bash ln:False
helm repo add rancher-stable https://releases.rancher.com/server-charts/stable
```

