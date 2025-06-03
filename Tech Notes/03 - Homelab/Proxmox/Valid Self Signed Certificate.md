---
tags: [ca-cert,networking]
---

</br>

## Generate CA

1. Generate RSA key
	```bash ln:False
	openssl genrsa -aes256 -out ca-key.pem 4096
	```

2. Generate corresponding CA for above key
	```bash ln:False
	openssl req -new -x509 -sha256 -days 365 -key ca-key.pem -out ca.pem
	```
	*Output*
	```yml ln:False
	Enter pass phrase for ca-key.pem:
	You are about to be asked to enter information that will be incorporated
	into your certificate request.
	What you are about to enter is what is called a Distinguished Name or a DN.
	There are quite a few fields but you can leave some blank
	For some fields there will be a default value,
	If you enter '.', the field will be left blank.
	-----
	Country Name (2 letter code) [AU]:IN
	State or Province Name (full name) [Some-State]:Karnataka
	Locality Name (eg, city) []:Bangalore
	Organization Name (eg, company) [Internet Widgits Pty Ltd]:homelab
	Organizational Unit Name (eg, section) []:
	Common Name (e.g. server FQDN or YOUR name) []:homelab
	Email Address []:
	```

	> [!note] 
	> Remember to add an apt Organization Name as the key will be referred to by that name when stored on your system.
	> And also the main fqdn for wildcard matches.

	> View the contents of the cert using:
	> ```bash ln:False
	> openssl x509 -in ca.pem -text | less
	> ```

</br>

## Generate Certificate

1. Generate RSA key

	> we do not provide the flag `-aes` as we need to later copy the key

	```bash ln:False
	openssl genrsa -out cert-key.pem 4096
	```

2. Create a certificate Signed Request from above key

	```bash ln:False
	openssl req -new -sha256 -subj "/CN=homelab" -key cert-key.pem -out cert.csr
	```

3. Create extfile

	```bash ln:False
	echo "subjectAltName=DNS:*.homelab.local,IP:192.168.0.20" >> extfile.cnf
	```

4. Generate certificate from csr

```bash ln:False
openssl x509 -req -sha256 -days 365 -in cert.csr -CA ca.pem -CAkey ca-key.pem -out cert.pem -extfile extfile.cnf -CAcreateserial
```

</br>

## Combine Certificates

```bash ln:False
cat cert.pem ca.pem | tee fullchain.pem
```

</br>

## Add certs to Nginx Conf

> [!caution] Do this only if you have `nginx` setup on your Proxmox instance else run the next section.

```bash ln:False
sudo mkdir -p /etc/nginx/ssl
sudo cp fullchain.pem /etc/nginx/ssl/proxmox.homelab.local.pem
sudo cp cert-key.pem /etc/nginx/ssl/proxmox.homelab.local-key.pem
sudo chown root:root /etc/nginx/ssl/*.pem
sudo chmod 600 /etc/nginx/ssl/*.pem
```

- change the Proxmox DNS FQDN to the required one configured for the wildcard domain set above in your local DNS.

- change the following lines in the file:
```text title:/etc/nginx/sites-available/proxmox.conf
upstream proxmox {
    server "proxmox.homelab.local";
}
.
.
server {
	.
	.
	ssl_certificate /etc/nginx/ssl/proxmox.homelab.local.pem;
    ssl_certificate_key /etc/nginx/ssl/proxmox.homelab.local-key.pem;
    .
    .
}
```

- restart nginx
```bash ln:False
sudo systemctl restart nginx
```

> Finally, upload the ca certs to your local device from which Proxmox is accessed from: [[#Import CA cert to device]]

</br>

## Upload Custom Certificate on Proxmox

> [!note] 
> Run this step if you do not have nginx configured.

![[20250601133020_proxmox_upload_cert.png]]

1. Paste the contents of private key
```bash ln:False
cat cert-key.pem
```

2. Paste the contents of the fullchain key
```bash ln:False
cat fullchain.pem
```

</br>

## Import CA cert to device

> Run the following commands in windows system Powershell as ==administrator==:

```bash ln:False
scp jeswins@192.168.0.20:~/Downloads/CA-certs/ca.pem .
```


```powershell ln:False
Import-Certificate -FilePath "ca.pem" -CertStoreLocation Cert:\LocalMachine\Root
```

> Verify using the app ==certmgr==