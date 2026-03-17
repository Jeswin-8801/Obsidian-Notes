---
tags: [kubernetes, helm]
---

</br>

The command below is used to view the entire chart that will be deployed after applying `values.yaml`.

#### Example using Homarr

- go to the directory containing `values.yaml` and run:

```bash ln:False
helm template homarr oci://ghcr.io/homarr-labs/charts/homarr \
	-n homarr \
	-f values.yaml \
	| less
```
