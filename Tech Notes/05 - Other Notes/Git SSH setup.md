---
tags: [git,ssh]
---

</br>

- create the `~/.ssh`folder, if it does not exist

```bash ln:False
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

- create ==SSH== key

```bash ln:False
cd ~/.ssh
ssh-keygen -t ed25519 -C "jeswin.santosh@outlook.com"
# create key with name 'id_ed25519_github'
```

- add SSH key to GitHub at [SSH and GPG keys](https://github.com/settings/keys)

- point the key to be used when encountering URI with name `github.com`
```bash ln:False
cat > ~/.ssh/config << EOF
Host github.com
 HostName github.com
 IdentityFile ~/.ssh/id_ed25519_github
EOF
```