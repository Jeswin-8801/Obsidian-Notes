---
tags: [ubuntu,apt]
---

</br>

Query for the package using `dpkg` before installing:

```bash
#!/bin/bash

install_if_missing() {
    if [ "$#" -eq 0 ]; then
        echo "No packages specified."
        return 1
    fi

    for pkg in "$@"; do
        if dpkg -l | grep -qw "$pkg"; then
            echo "$pkg is already installed. Skipping."
        else
            echo "Installing $pkg..."
            sudo apt install -y "$pkg"
        fi
    done
}
```