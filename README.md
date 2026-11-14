# YBDOS-Emulator

⚠️ **IMPORTANT DISCLAIMER:** 
This is a Python-based 16-bit DOS Emulator & Debugger (Official Release), **NOT a real operating system!** DO NOT expect it to replace MS-DOS/FreeDOS or run complex DOS games. It is built purely for learning low-level hardware interactions, CPU instruction emulation, and custom interrupt hooks (INT 21H/10H/16H). It currently supports simple `.COM` programs (like the included `CAL.COM`).

## 🚀 Core Features

- **Engine**: Powered by `Unicorn` for 8086 CPU emulation and `Keystone` for real-time assembly parsing.
- **Custom BIOS**: Authentic BIOS POST (Power-On Self-Test) animation and simulated memory scanning.
- **Interrupt Hooks**: Custom `INT 21H` (DOS API), `INT 10H` (Video), and `INT 16H` (Keyboard) implemented purely in Python.
- **Virtual File System (VFS)**: Fully implemented path dictionary system with `cd` and `dir` commands. Supports mounting real physical directories.
- **ZIP Mounting**: Can mount `.zip` archives directly as virtual drives and traverse internal directories.
- **Classic UI**: Retro full-uppercase 8.3 filename formatting and DOS visual experience.
- **JemmEx-style Panic**: Classic JemmEx crash screen with register snapshots and `0x0D`, `0x0E` exception handling.
- **Time Travel**: Successfully runs a 1998 DOS program (`CAL.COM`), rendering a perfect calendar!

## 🛠️ How to Test

1. Download and extract `YBDOSv1.00_Release.zip` from the **Releases** section.
2. Run the main executable.
3. Type the following commands at the `-` or `C:\>` prompt to test:
   - `dir` (List directory contents)
   - `cd [folder]` (Change directory)
   - `n CAL.COM` (Specify the program to load)
   - `l` (Load into virtual memory)
   - `g` (Go! Watch the 1998 magic happen)

## 📅 Roadmap

- [ ] Real MBR boot sector parsing (`.bin`)
- [ ] `.EXE` (MZ header) loader support
- [ ] Real-time rendering for VGA VRAM (`0xB8000`)
