# YBDOS-Emulator
> ⚠️ **IMPORTANT DISCLAIMER:**
> This is a **Python-based 16-bit DOS Emulator & Debugger (Experimental Beta)**, NOT a real operating system!
> **DO NOT** expect it to replace MS-DOS/FreeDOS or run complex DOS games. 
> It is built purely for learning low-level hardware interactions, CPU instruction emulation, and custom interrupt hooks (INT 21H/10H/16H). It currently only supports simple dependency-free `.COM` programs (like the included `CAL.COM`).

## 🚀 Core Features

- **Engine**: Powered by `Unicorn` for 8086 CPU emulation and `Keystone` for real-time assembly parsing.
- **Custom BIOS**: Authentic BIOS POST (Power-On Self-Test) animation and simulated memory scanning.
- **Interrupt Hooks**: Custom `INT 21H` (DOS API), `INT 10H` (Video), and `INT 16H` (Keyboard) implemented purely in Python.
- **JemmEx-style Panic**: Classic JemmEx crash screen with register snapshots and `0x0D`, `0x0E` exception handling.
- **Time Travel**: Successfully runs a 1998 DOS program (`CAL.COM`), rendering a perfect calendar!

## 🛠️ How to Test

1. Download and extract `YBDOSv1.00_Beta.zip` from the **Releases** section.
2. Run the main executable (or the corresponding `.COM` files).
3. Type the following commands at the `-` prompt to test:
   - `n CAL.COM` (Specify the program)
   - `l` (Load into virtual memory)
   - `g` (Go! Watch the 1998 magic happen)

## 📅 Roadmap
- [ ] `.EXE` (MZ header) loader support
- [ ] Real-time rendering for VGA VRAM (`0xB8000`)

---
*Created by Cyber Lord. 2026.*
