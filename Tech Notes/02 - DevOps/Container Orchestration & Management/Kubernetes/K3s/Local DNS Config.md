---
tags: [DNS,kubernetes, ]
---

> Refer: [Add a local DNS zone to your k3s CoreDNS](https://blog.voltane.eu/k3s-local-dns/)

- save this file to all nodes
```yaml {22} title:/var/lib/rancher/k3s/server/manifests/coredns.override.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
        }
        hosts /etc/coredns/NodeHosts {
          ttl 60
          reload 15s
          fallthrough
        }
        prometheus :9153
        forward home.local 192.168.0.40
        forward . /etc/resolv.conf
        log
        cache 60
        loop
        reload
        loadbalance
    }
```