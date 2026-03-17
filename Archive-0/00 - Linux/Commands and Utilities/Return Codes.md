---
tags: [linux]
---

</br>

In **Bash**, **return codes** (**exit statuses**) are **integers from 0 to 255** returned by commands to indicate success or failure.


|Code|Meaning|
|---|---|
|<mark style="background: #FFB86CA6;">0</mark>|Success (command ran correctly)|
|<mark style="background: #FFB86CA6;">1</mark>|General error (catch-all for failed commands)|
|<mark style="background: #FFB86CA6;">2</mark>|Misuse of shell builtins (e.g., bad usage)|
|<mark style="background: #FFB86CA6;">126</mark>|Command found but **not executable**|
|<mark style="background: #FFB86CA6;">127</mark>|Command **not found**|
|<mark style="background: #FFB86CA6;">128</mark>|Invalid **exit argument**|
|<mark style="background: #FFB86CA6;">130</mark>|Script **terminated by Ctrl+C** (`128 + 2`)|
|<mark style="background: #FFB86CA6;">>128</mark>|Command exited due to **signal** `N` = `exit code - 128`|

> [!note] 
> Most other return codes (3–125) are **application-defined**.