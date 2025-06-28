---
tags: [networking, VPN]
---


#### 1. Go to Project directory

```bash ln:False
cd ./Tailscale
```

#### 2. Generate Auth Key

![[20250628162531_tailscale_auth_key.png]]

> Paste this key in `secrets.yaml`

</br>

#### 3. Install

> [!note] 
> Before installing, make sure the subnet in `deployment.yaml` is correct.

```bash ln:False
kubectl apply -k .
```

#### 4. Allow Published Subnet

- Click on the More options of the device (three dots).
- Select <mark style="background: #D2B3FFA6;">**Edit route settings**</mark>
- Accept the subnet you configured.

#### 5. Disable key expiry

- Click on the More options of the device (three dots).
- Select <mark style="background: #D2B3FFA6;">**Disable key expiry**</mark>

#### 6. Add Split DNS Nameserver

In the DNS settings page, click on the <mark style="background: #D2B3FFA6;">Add nameserver</mark> dropdown. Select <mark style="background: #D2B3FFA6;">Custom</mark> and enter the following details:

- **Nameserver**: Enter the IP address of your Pi-hole instance.
- **Restrict Domain**: restrict to Homelab services

![[20250628164400_tailscale_dns.png]]