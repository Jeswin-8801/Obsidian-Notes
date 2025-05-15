---
tags: [CI∕CD]
---


<mark style="background: #FFB86CA6;color:white">GitLab CE</mark>

>  gitlab
├──  docker-compose.yaml
├──  config
│   └──  gitlab.rb
├──  logs
└──  data

```yaml title:docker-compose.yaml
services:
  gitlab:
    image: gitlab/gitlab-ce
    container_name: gitlab-server
    ports:
      - "443:443"
      - "80:80"
      - "22:22"
    volumes:
      - ./config:/etc/gitlab
      - ./logs:/var/log/gitlab
      - ./data:/var/opt/gitlab
    shm_size: "256m"
    restart: unless-stopped
```

```bash ln:False
$ mkdir config data logs
```

```bash ln:False
$ cat config/gitlab.rb
gitlab_rails['lfs_enabled'] = true
```

- get Password (username: `root`)
```bash ln:False
$ docker exec -it gitlab-server grep 'Password:' /etc/gitlab/initial_root_password
```



