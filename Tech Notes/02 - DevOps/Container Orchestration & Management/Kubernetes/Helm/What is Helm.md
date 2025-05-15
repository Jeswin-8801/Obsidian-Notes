---
tags: [helm,kubernetes]
---

</br>

<mark style="background: #D2B3FFA6;">**Helm**</mark> is a <mark style="background: #D2B3FFA6;">**package manager for Kubernetes**</mark> that simplifies the deployment and management of applications within Kubernetes clusters.

It allows users to define, install, and upgrade applications using **Helm charts**, which are pre-configured Kubernetes resources bundled together.

### **Key Terms in Helm**

1. <mark style="background: #FFB86CA6;">**Chart**</mark> – A Helm package containing Kubernetes manifests, templates, and configurations.
    
2. <mark style="background: #FFB86CA6;">**Release**</mark> – An instance of a Helm chart deployed in a Kubernetes cluster.
    
3. <mark style="background: #FFB86CA6;">**Repository**</mark> – A collection of Helm charts that can be stored and shared.
    
4. <mark style="background: #FFB86CA6;">**Values**</mark> – Configuration settings that allow customization of Helm chart deployments.
    
5. <mark style="background: #FFB86CA6;">**Helm Client</mark>** – The command-line tool used to interact with Helm.
    
6. <mark style="background: #FFB86CA6;">**Helm Library</mark>** – The backend component that processes Helm templates and interacts with Kubernetes.
    
7. <mark style="background: #FFB86CA6;">**Tiller (Helm v2)**</mark> – A deprecated server-side component that managed Helm releases (removed in Helm v3).
    
8. <mark style="background: #FFB86CA6;">**Templates**</mark> – YAML files with placeholders that allow dynamic configuration.
    
9. <mark style="background: #FFB86CA6;">**Hooks**</mark> – Special scripts that run at different stages of a Helm release lifecycle.
    
10. <mark style="background: #FFB86CA6;">**Rollback**</mark> – The ability to revert to a previous Helm release version.