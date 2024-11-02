
# Installation

>  ..
>  docker-compose.yaml
>  jenkins_home/
>  Dockerfile
>  entrypoint.sh
>  .

```Dockerfile title:Dockerfile
FROM jenkins/jenkins:lts

# Switch to root user
USER root

# Download and Install JDK 21
RUN apt-get update && \
    apt-get install -y wget && \
    mkdir -p /opt/jdk-21 && \
    wget -q https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb -O /tmp/jdk-21_linux-x64_bin.deb && \
    dpkg -x /tmp/jdk-21_linux-x64_bin.deb /opt/jdk-21 && \
    rm /tmp/jdk-21_linux-x64_bin.deb && \
    ln -s /opt/jdk-21/usr/lib/jvm/jdk-21.0.5-oracle-x64/bin/ /usr/local/bin/jdk-21

# Install Necessary Packages
RUN apt-get update && \
    apt-get install -y \
    nodejs \
    npm \
    python3 \
    python3-pip \
    java-common \
    docker.io && \
    apt-get clean

# Install Ansible
RUN UBUNTU_CODENAME=jammy && \
    wget -O- "https://keyserver.ubuntu.com/pks/lookup?fingerprint=on&op=get&search=0x6125E2A8C77F2818FB7BD15B93C4A3FD7BB9C367" || gpg --dearmour -o /usr/share/keyrings/ansible-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ansible-archive-keyring.gpg] http://ppa.launchpad.net/ansible/ansible/ubuntu $UBUNTU_CODENAME main" || tee /etc/apt/sources.list.d/ansible.list && \
    apt-get update && \
    apt-get -y install ansible

# Setup MAVEN
ENV MAVEN_VERSION 3.9.9
ENV MAVEN_HOME /opt/apache-maven-$MAVEN_VERSION
RUN wget -q https://dlcdn.apache.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz -O /opt/maven.tar.gz -S && \
    tar -xzf /opt/maven.tar.gz -C /opt && \
    rm -f /opt/maven.tar.gz && \
    ln -s $MAVEN_HOME/bin/mvn /usr/local/bin/mvn

# Java Alternate Installations
RUN update-alternatives --install /usr/bin/java java /usr/local/bin/jdk-21/java 2 && \
    update-alternatives --install /usr/bin/java java /opt/java/openjdk/bin/java 1

# Jenv
RUN git clone https://github.com/jenv/jenv.git /opt/jenv && \
    ln -s "/opt/jenv/bin/jenv" "/usr/local/bin/jenv"

# Verify installations
RUN mvn --version && \
    git --version && \
    node --version && \
    npm --version && \
    python3 --version && \
    pip3 --version && \
    docker --version && \
    java --version && \
    ansible --version && \
    update-alternatives --list java && \
    jenv doctor

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# Switch back to the jenkins user
USER jenkins
```

```bash title:entrypoint.sh
#!/bin/bash

printf '\neval "$(jenv init -)"\njenv enable-plugin export\n' >> /root/.bashrc
source /root/.bashrc

jenv add /opt/java/openjdk
jenv add /opt/jdk-21/usr/lib/jvm/jdk-21.0.5-oracle-x64/

jenv doctor

# upstream ENTRYPOINT
exec /usr/bin/tini -- /usr/local/bin/jenkins.sh
```

```yaml title:docker-compose.yaml
services:
	jenkins:
		build: .
		privileged: true
		user: root
		ports:
			- 8080:8080
			- 50000:50000
		container_name: jenkins-server
		volumes:
			- ./jenkins_home:/var/jenkins_home
```

```bash ln:False
$ mkdir jenkins_home
```

- get root password
```bash ln:False
$ docker exec -it jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword
```

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