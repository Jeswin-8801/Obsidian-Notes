---
tags: [networking,dns,homelab, ]
---

</br>

- search for file `/etc/pihole/pihole.toml` and replace the text
```text ln:False
piholePTR = "PI.HOLE"
.
.
domain = "pi.hole"
```
*with*
```text ln:False
piholePTR = "HOSTNAMEFQDN"
.
.
domain = "home.local"
```

- Restart Service
```bash ln:False
service pihole-FTL restart
```

- Check for Failure in Logs if any
```bash ln:False
tail -f /var/log/pihole/webserver.log
```

> On typing `nslookup` in you local windows CMD, you will find the FQDN changed for your DNS.

> Refer: [Configuration - Pi-hole documentation](https://docs.pi-hole.net/ftldns/configfile/#pihole_ptr)

</br>

### Create Valid Self Signed Certificates

> [!info] Refer: [Pi-hole v6: Creating Your Own Self-Signed SSL Certificates](https://gist.github.com/kaczmar2/e1b5eb635c1a1e792faf36508c5698ee#method-1-use-an-internal-certificate-authority-ca-recommended)

1. Create ==CA Certificate== and Key
```bash ln:False
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -days 3650 -keyout homelabCA.key -out homelabCA.crt -subj "/C=IN/O=Homelab CA/CN=HomelabCA"
```

*Add `-nodes` flag if no passphrase is required. Is applicable for the commands that will be used in the following steps.*

> [!note] 
> Store this key and cert in a secure commonly accessible location as this will be the Root CA that will be used to sign all subsequent certs.

2. Modify ==cert.cnf== file

	Use the file in the <mark style="background: #D2B3FFA6;">HomeLab</mark> repo at location <mark style="background: #D2B3FFA6;">Networking/</mark> to suit your webservice properties.

3. Generate Key and CSR

```bash ln:False
openssl req -new -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes -keyout tls.key -out tls.csr -config cert.cnf
```

4. Sign the CSR with the CA

```bash ln:False
openssl x509 -req -in tls.csr -CA homelabCA.crt -CAkey homelabCA.key -CAcreateserial -nodes -out tls.crt -days 365 -sha256 -extfile cert.cnf -extensions v3_ext
```

5. Create a Combined ==tls.pem== File

```bash ln:False
cat tls.key tls.crt | tee tls.pem
```

6. Move the key to Pi-Hole Instance

```bash ln:False
scp tls.pem root@192.168.0.40:/etc/pihole/
```

7. Set Pi-Hole to only serve HTTPS

```bash ln:False
pihole-FTL --config webserver.port '443s, [::]:443s'
```
Where the above IP is the static IP of the VM running Pi-Hole.

</br>

### Add the Root CA to your Local System

Refer: [[Valid Self Signed Certificate#Import CA cert to device]]

> Also Refer: [luizbizzio/pihole-https: 🔒 Enable HTTPS for Pi-hole with automatic SSL certificate generation, Tailscale DNS detection, and cross-platform compatibility for Windows, Linux, macOS, and Android devices.](https://github.com/luizbizzio/pihole-https?tab=readme-ov-file#installing-the-certificate-on-devices-) for other devices.

### Automatically Setup Certs

> [!note] 
> It creates the root CA every single time which is not desirable.
> This is what pi-hole does by default.

> Refer: [TLS/SSL - Pi-hole documentation](https://docs.pi-hole.net/api/tls/?h=domain#adding-the-ca-to-your-browser)

- Restart `pi-hole`
```bash ln:False
rm /etc/pihole/tls*
service pihole-FTL restart
```