---
tags: [kubernetes, ]
---

> This taints all longhorn nodes as non-schedulable so that they as used only for storage and not for scheduling pods.


```bash ln:False
kubectl taint nodes longhorn-01 node-role.kubernetes.io/longhorn=only:NoSchedule
kubectl taint nodes longhorn-02 node-role.kubernetes.io/longhorn=only:NoSchedule
kubectl taint nodes longhorn-03 node-role.kubernetes.io/longhorn=only:NoSchedule
```


- show all labels and roles
```bash ln:False
kubectl get nodes -o wide --show-labels
```

- Label them
```bash ln:False
kubectl label node longhorn-01 node-role.kubernetes.io/longhorn=true
kubectl label node longhorn-02 node-role.kubernetes.io/longhorn=true
kubectl label node longhorn-03 node-role.kubernetes.io/longhorn=true

kubectl label node k3s-w-01 node-role.kubernetes.io/longhorn=false
kubectl label node k3s-w-02 node-role.kubernetes.io/longhorn=false

kubectl label node k3s-w-01 node-role.kubernetes.io/worker=true
kubectl label node k3s-w-02 node-role.kubernetes.io/worker=true
```