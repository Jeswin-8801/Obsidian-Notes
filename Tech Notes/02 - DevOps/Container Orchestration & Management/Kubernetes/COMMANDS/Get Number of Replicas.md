---
tags: [kubernetes, ]
---

</br>

```bash ln:False
kubectl -n <your-namespace> get deployment -o custom-columns=NAME:.metadata.name,REPLICAS:.spec.replicas
```
