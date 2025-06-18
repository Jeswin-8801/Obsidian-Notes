---
tags: [kubernetes]
---

</br>

## Get PersistentVolume

> [!note] 
> A ==PV== is accessible cluster wide.

```bash ln:False
kubectl get pv
```

## Get PersistentVolumeClaim

```bash ln:False
kubectl -n <namespace> get pvc
```


</br>

---

</br>

| Feature               | <mark style="background: #ABF7F7A6;">PV</mark> | <mark style="background: #ABF7F7A6;">PVC</mark> |
| --------------------- | ---------------------------------------------- | ----------------------------------------------- |
| Represents            | Actual physical/logical volume                 | A request for storage                           |
| Created by            | Admin or provisioner                           | Developer/User                                  |
| Scope                 | Cluster-wide                                   | Namespace-scoped                                |
| Can be shared         | Yes (depending on access mode)                 | No (bound to one PV)                            |
| Dynamic provisioning? | Not directly                                   | Yes, via StorageClass                           |
