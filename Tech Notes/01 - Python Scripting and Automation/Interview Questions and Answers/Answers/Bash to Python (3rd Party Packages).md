
## Problem:

>A bash script is using 3rd party packages to collect performance data of drives Convert the script to python.

- an example of a Bash script that collects performance data of drives
```bash
#!/bin/bash

# Install the necessary packages
sudo apt-get install sysstat smartmontools hdparm -y

# Collect drive performance data
echo "Collecting drive performance data..."
iostat -dx 1 5 > drive_performance.txt
smartctl -a /dev/sda >> drive_performance.txt
hdparm -tT /dev/sda >> drive_performance.txt

echo "Data collection complete. Results saved in drive_performance.txt"
```

- when converted to Python
```python
import os
import subprocess

def install_packages():
    packages = ["sysstat", "smartmontools", "hdparm"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", package, "-y"], check=True)

def collect_performance_data():
    with open("drive_performance.txt", "w") as file:
        # Run iostat
        file.write("Running iostat...\n")
        iostat_output = subprocess.run(["iostat", "-dx", "1", "5"], capture_output=True, text=True)
        file.write(iostat_output.stdout)

        # Run smartctl
        file.write("\nRunning smartctl...\n")
        smartctl_output = subprocess.run(["smartctl", "-a", "/dev/sda"], capture_output=True, text=True)
        file.write(smartctl_output.stdout)

        # Run hdparm
        file.write("\nRunning hdparm...\n")
        hdparm_output = subprocess.run(["hdparm", "-tT", "/dev/sda"], capture_output=True, text=True)
        file.write(hdparm_output.stdout)

    print("Data collection complete. Results saved in drive_performance.txt")

def main():
    install_packages()
    collect_performance_data()

if __name__ == "__main__":
    main()
```

> Corresponding sample Ansible Playbook

```yaml
- name: Test drives across multiple servers
  hosts: all
  become: yes
  tasks:
    - name: Ensure Python is installed
      apt:
        name: python3
        state: present

    - name: Copy the Python script to the remote server
      copy:
        src: /local/path/to/drive_test_script.py
        dest: /tmp/drive_test_script.py
        mode: '0755'

    - name: Run the Python script
      command: python3 /tmp/drive_test_script.py
      register: script_output

    - name: Display the script output
      debug:
        var: script_output.stdout

    - name: Gather results
      fetch:
        src: /tmp/drive_performance.txt
        dest: /local/path/to/results/{{ inventory_hostname }}/drive_performance.txt
        flat: yes
```

1. Ensures Python is installed on the remote servers.
2. Copies your Python script to the `/tmp` directory on each remote server.
3. Runs the Python script on each remote server.
4. Displays the output of the Python script.
5. Fetches the results from each remote server to a local path, organized by the hostname of each server.