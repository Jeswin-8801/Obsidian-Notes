---
tags: [Embedded-Systems]
---

</br>


==**JTAG**== (Joint Test Action Group) is a standard interface (IEEE 1149.1) used primarily for:

1. **Testing and Debugging** of integrated circuits (ICs) at the board level.
	Set breakpoints, step through code, inspect memory/registers (via tools).
</br>
2. **Programming** devices like microcontrollers, FPGAs, and CPLDs.
	Flash firmware or bitstreams to microcontrollers, FPGAs, and CPLDs.
</br>  
3. <mark style="background: #D2B3FFA6;">**Boundary-Scan Testing**</mark>, allowing access to pins of a chip without physical probes.
   
	It allows you to **test the interconnections between chips on a PCB** without using physical test probes.

</br>

### 🔌 Key Features of the JTAG Interface:

- **Serial Communication**: Operates via a small number of pins, typically:
	- <mark style="background: #FFB86CA6;">TDI</mark> (Test Data In)
	- <mark style="background: #FFB86CA6;">TDO</mark> (Test Data Out)
	- <mark style="background: #FFB86CA6;">TCK</mark> (Test Clock)
	- <mark style="background: #FFB86CA6;">TMS</mark> (Test Mode Select)
	- Optional: <mark style="background: #FFB86CA6;">TRST</mark> (Test Reset)
</br> 
- **Daisy-Chaining**: Multiple devices can be chained together through JTAG, enabling testing and programming via a single interface.
</br>
- **Standardized Protocol**: Originally designed to help with testing circuit boards, it now serves as a low-level debugging interface for many processors and microcontrollers.

</br>

### 🧰 Tools That Use JTAG:

- **OpenOCD** – Open On-Chip Debugger
    
- **Segger J-Link**
    
- **ARM Keil/ULINK**
    
- **Xilinx/Altera programmers**

---

> [!info] 
> Useful resouces:
> [How to use JTAG built-in debugger of the ESP32-S3 in PLATFORMIO - PlatformIO IDE - PlatformIO Community](https://community.platformio.org/t/how-to-use-jtag-built-in-debugger-of-the-esp32-s3-in-platformio/36042)