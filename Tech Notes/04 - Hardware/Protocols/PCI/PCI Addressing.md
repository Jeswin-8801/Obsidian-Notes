---
tags: [pci]
---

</br>

### PCI Addressing Format (Config Space Access)

A standard **PCI configuration address** is 32 bits wide and is structured like this:

|Bits|Field|Description|
|---|---|---|
|31|Enable Bit|Set to 1 to indicate config access|
|30–24|Reserved|Not used|
|23–16|<mark style="background: #FFB86CA6;">Bus Number</mark>|Selects PCI bus (0–255) <mark style="background: #D2B3FFA6;">2<sup>8</sup></mark>|
|15–11|<mark style="background: #FFB86CA6;">Device Number</mark>|Selects device (0–31) <mark style="background: #D2B3FFA6;">2<sup>5</sup></mark>|
|10–8|<mark style="background: #FFB86CA6;">Function Number</mark>|Selects function (0–7) <mark style="background: #D2B3FFA6;">2<sup>3</sup></mark>|
|7–2|Register Number|Selects register offset (0–63 dwords) <mark style="background: #D2B3FFA6;">2<sup>6</sup></mark>|
|1–0|Always 00|Because registers are 32-bit aligned|


- **Device Number (5 bits)**:
    - 2⁵ = **32 possible devices** per PCI bus → numbered **0–31**
- **Function Number (3 bits)**:
    - 2³ = **8 possible functions** per device → numbered **0–7**
    - This allows for **multifunction devices** (like a GPU with audio and video).

Thus, on any given **PCI bus**, you can address:


```bash ln:False
32 devices × 8 functions = 256 total functions per bus
```

> A ==PCI bus== (Peripheral Component Interconnect bus) is a **communication pathway** that connects peripheral devices (like network cards, storage controllers, or graphics cards) to the CPU and memory through the motherboard's chipset.