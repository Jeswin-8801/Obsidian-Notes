---
tags: [automation]
---

**Ansible** is an **open-source IT automation tool** used to:

- Provision infrastructure 
- Configure systems
- Deploy applications
- Orchestrate workflows

It’s **agentless**, written in **Python**, and primarily uses **SSH** for communication.

---

## 🧠 Core Concepts

#### 1. **Control Node**

- The machine (usually your laptop or a server) where Ansible is installed.
- Executes tasks and orchestrates target machines (called **managed nodes**).

#### 2. **Managed Nodes**

- The systems you manage (Linux/Windows servers, network switches, cloud VMs).
- **No agent required** — communication is over **SSH** (Linux) or **WinRM** (Windows).

#### 3. **Inventory**

- A file (usually `inventory.ini` or YAML) that defines **hosts** and **groups** of hosts.
- Can be **static** or **dynamic** (e.g., AWS EC2 inventory plugin).

#### 4. **Modules**

- Units of work (e.g., `apt`, `yum`, `copy`, `user`, `shell`, `ping`).
- Ansible has **hundreds of modules** built-in and community-developed.

#### 5. **Playbooks**

- Written in **YAML**, describe **what to do** and **on which hosts**.
- Use **tasks**, **handlers**, **roles**, and **variables** for reusability and logic.

#### 6. **Roles**

- Directory structure to group tasks, templates, vars, handlers, etc., into reusable packages.
