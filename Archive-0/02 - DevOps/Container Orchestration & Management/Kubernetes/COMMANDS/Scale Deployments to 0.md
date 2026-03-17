---
tags: [kubernetes,How-To]
---

</br>

```bash ln:False
kubectl -n <your-namespace> scale deploy --all --replicas=0
```

> Verify

```bash ln:False
watch kubectl -n <your-namespace> get pods
```