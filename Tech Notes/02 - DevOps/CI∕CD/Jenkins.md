---
tags: [CI∕CD]
---

# Installation

> Refer => [Jeswin-8801/Jenkins: A containerized version of Jenkins server with offline setup (preloaded with required plugins) with reverse proxy](https://github.com/Jeswin-8801/Jenkins)

---

# Start New Pipeline

> Get Personal Access Token from https://github.com/settings/tokens

---
# Running Build Job using Jenv

```bash
#!/bin/bash
cd /build-folder
if [ ! -f .java-version ]; then
  jenv local 21
fi
export JAVA_HOME="/root/.jenv/versions/$(cat .java-version)"
cd project-folder
mvn clean install
```

---
# Reset Admin Password

> *For when you lose your admin password*
- copy `config.xml` to local
```bash ln:False
docker cp <containerId>:/var/jenkins_home/config.xml .  
```
- open `config.xml` and change <mark style="background: #FFF3A3A6;">**useSecurity**</mark> to **false**
- copy the updated `config.xml` back into the container.
```bash ln:False
docker cp ./config.xml <containerId>:/var/jenkins_home/config.xml .  
docker restart <containerId>
```

- Go to => `http://<jenkinsUrl>/manage/script`
- Execute:
```java
import hudson.model.User;  
User.getById("<username>",false).addProperty(hudson.security.HudsonPrivateSecurityRealm.Details.fromPlainPassword("<password>"));
```
- open `config.xml` and change <mark style="background: #FFF3A3A6;">**useSecurity**</mark> to **true**
- copy the updated `config.xml` back into the container.
```bash ln:False
docker cp ./config.xml <containerId>:/var/jenkins_home/config.xml .  
docker restart <containerId>
```

