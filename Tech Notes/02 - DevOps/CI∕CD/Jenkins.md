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