---
tags: [networking,homelab,reverse-proxy]
---

</br>

> using Helm
> [Traefik Installation Documentation - Traefik](https://doc.traefik.io/traefik/getting-started/install-traefik/#use-the-helm-chart)

</br>

- Add Traefik Labs chart repository to Helm:

```bash ln:False
helm repo add traefik https://traefik.github.io/charts
```

- update the chart:

```bash ln:False
helm repo update
```

- install:

```bash ln:False
helm install traefik traefik/traefik
```