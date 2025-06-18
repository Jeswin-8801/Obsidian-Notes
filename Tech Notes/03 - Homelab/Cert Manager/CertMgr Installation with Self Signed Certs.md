---
tags: [networking, kubernetes, ]
---

</br>

> [!important] 
> If you have followed through the [[Rancher Installation]], then you will have installed ==cert manager==. So, the only change to be made is to skip step 1 and replace `install` with `upgrade` in step 2.

## Install using Helm

1. Add helm repo
```bash ln:False
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

2. Install <mark style="background: #D2B3FFA6;">cert-manager</mark>
```bash ln:False
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.18.0 \
  --set crds.enabled=true \
  --set webhook.timeoutSeconds=4 \
  --set replicaCount=2 \
  --set podDisruptionBudget.enabled=true \
  --set podDisruptionBudget.minAvailable=1
```

</br>

## Create certs

1. Create Custom directory
```bash ln:False
mkdir certmanager
cd certmanager
```

2. Download necessary files
```bash ln:False
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/Kubernetes/CertManager/spwn-root-ca.yaml
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/Kubernetes/CertManager/spnw-intermediate-ca1.yaml
```

3. Create the self signed root CA
```bash ln:False
kubectl -n cert-manager apply -f spnw-root-ca.yaml
```

- View cert information

	```bash ln:False
	kubectl get secret spnw-root-ca-secret -n cert-manager -o jsonpath='{.data.tls\.crt}' |  base64 --decode | openssl x509 -noout -text
	```

> [!note] 
> The secret `spnw-root-ca-secret` has multiple filenames, `tls.crt` contains the certificate, `tls.key` contains the private key. (Refer: [[#Access Certs and Keys]])

4. Create the intermediate CA
```bash ln:False
kubectl -n cert-manager apply -f spnw-intermediate-ca1.yaml
```

> To verify both secrets have been created successfully
> ```bash ln:False
> kubectl describe ClusterIssuer -n cert-manager
> ```

#### Verify signing of Intermediate CA by the Root CA

```bash ln:False
openssl verify -CAfile <(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode) <(kubectl -n cert-manager get secret spnw-intermediate-ca1-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode)
```

You will get the following output:
```text ln:False
/dev/fd/61: OK
```

</br>

## Access Certs and Keys

- Root CA cert (<mark style="background: #D2B3FFA6;">tls.crt</mark>)
```bash ln:False
kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode
```

- Root CA key (<mark style="background: #D2B3FFA6;">tls.key</mark>)
```bash ln:False
kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.key}' | base64 --decode
```

</br>

## Issue a Test Certificate

1. Download file
```bash ln:False
wget https://raw.githubusercontent.com/Jeswin-8801/HomeLab/Kubernetes/CertManager/test-cert.yaml
```

2. Apply Config
```bash ln:False
kubectl apply -f test-cert.yaml
```

3. Verify cert chain
```bash ln:False
openssl verify -CAfile <(kubectl -n cert-manager get secret spnw-root-ca-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode) -untrusted  <(kubectl -n cert-manager get secret spnw-intermediate-ca1-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode) <(kubectl -n cert-test get secret test-server-secret -o jsonpath='{.data.tls\.crt}' | base64 --decode)
```

*OR*

```bash ln:False
OLDIFS=$IFS; IFS=':' certificates=$(kubectl get secret test-server-secret -n cert-test -o json | jq -r '.data["tls.crt"]' | base64 --decode | sed -n '/-----BEGIN/,/-----END/{/-----BEGIN/ s/^/:/; p}'); for certificate in ${certificates#:}; do echo $certificate | openssl x509 -noout  -ext subjectAltName -subject -issuer; echo; done; IFS=$OLDIFS
```

4. Delete after testing
```bash ln:False
kubectl delete -f test-cert.yaml
```

