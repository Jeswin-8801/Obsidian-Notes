---
tags: [sso]
---

## Create the Zitadel OAuth app

Follow the wizard and configure the app with the following properties:

- **Name** -> Superset

- **Type** -> Web

- **Authentication Method** -> Code

- **Redirect URI** -> `https://superset.home.local/oauth-authorized/oidc`

> [!note] 
> The redirect URI is in the format `https://<superset-webserver>/oauth-authorized/<provider-name>` as per [Configuring Oauth2 | Superset](https://superset.apache.org/docs/configuration/configuring-superset/#custom-oauth2-configuration)
> 
> Refer to `<provider-name>` from `values.yaml`.

> Finalize by clicking on the _Create_ button, and copy the client ID and the client secret.
