---
tags: [SSO, Zitadel, homarr]
---

#### Create the app with the settings given below

![[20250620211147_Homarr_Zitadel_Config.png]]

> [!info] Store the <mark style="background: #D2B3FFA6;">Client ID</mark> and <mark style="background: #D2B3FFA6;">Client Secret</mark> so that it can be used later in Kubernetes.

</br>

#### Token Settings

![[20250621220832_token_settings.png]]

- Redirect Settings
	- Redirect URIs: `https://homarr.home.local/api/auth/callback/oidc`
	- Post Logout URIs: `https://homarr.home.local`
	  

#### Add new User

![[20250621232318_zitadel_users_page.png]]

#### Setup Roles for your Project

![[20250621232601_zitadel_project_roles.png]]

#### Setup Grants for your Organization

![[20250621232747_zitadel_organization_grants.png]]

#### Setup Authorizations for the User

![[20250621232852_zitadel_authorization_for_user.png]]

