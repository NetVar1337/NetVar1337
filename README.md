<div align="center">

# ⚡ NetVar1337

### Developer · Reverse Engineer · Game Hacker

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=8B5CF6&center=true&vCenter=true&multiline=true&repeat=true&width=820&height=80&lines=Windows+Internals+%7C+Kernel+%7C+DMA;Game+Hacking+%7C+Anti-Cheat+Research;Reverse+Engineering+%7C+AI+Offensive+Tooling)](https://git.io/typing-svg)

<br>

[![X / Twitter](https://img.shields.io/badge/%2FX-NetVar1337-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/CyberNordicNO)
[![GitHub](https://img.shields.io/badge/GitHub-NetVar1337-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NetVar1337)
[![PurpleAILAB](https://img.shields.io/badge/PurpleAILAB-Co--Owner-8B5CF6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PurpleAILAB)
[![Discord](https://img.shields.io/badge/Discord-%40netvar-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/netvar)

</div>

---

## Who I Am

I'm a **developer and security researcher** who works from userland cheats up through kernel drivers, DMA/FPGA, and AI-native offensive tooling.

Day to day that means reverse engineering binaries, mapping Windows internals, building game-hacking and anti-cheat research tooling, and turning agent stacks into real red-team capability.

> *"If you understand how the machine thinks, you control the machine."*

Co-owner of **[PurpleAILAB](https://github.com/PurpleAILAB)** and its autonomous red-team agent stack.

---

## Focus Areas

| Domain | What I build / research |
| -------- | ------------------------- |
| **Game Hacking** | Memory R/W, internals/externals, hooks, offset pipelines, anti-cheat analysis (EAC / Vanguard / BattlEye) |
| **Reverse Engineering** | IDA / Ghidra, unpacking, protocol analysis, binary patching, agentic RE tooling |
| **Windows Internals** | Kernel drivers, manual map / inject, BYOVD, hypervisors (EPT/VMCS), driver emulation |
| **DMA / Hardware** | PCILeech, FPGA firmware, physical-memory attack surface |
| **Offensive AI** | Autonomous red-team agents, MCP tooling, agent infrastructure, LLM security |
| **Systems / Embedded** | C/Rust/Zig tooling, Flipper One firmware & Linux userspace, RK3576 |

---

## Flagship — [Decepticon](https://github.com/PurpleAILAB/Decepticon)

<div align="center">

[![Stars](https://img.shields.io/github/stars/PurpleAILAB/Decepticon?style=for-the-badge&label=Stars&color=yellow)](https://github.com/PurpleAILAB/Decepticon/stargazers)
[![Forks](https://img.shields.io/github/forks/PurpleAILAB/Decepticon?style=for-the-badge&label=Forks&color=blue)](https://github.com/PurpleAILAB/Decepticon/network/members)

</div>

**Decepticon** is a professional **autonomous red-team agent** (co-owned via PurpleAILAB). It runs real attack chains — recon → exploit → privesc → lateral → C2 — under full engagement discipline (RoE, ConOps, deconfliction, OPPLAN + MITRE ATT&CK).

- Real kill chains driven by an OPPLAN, not `nmap` + a PDF
- Interactive shells in persistent `tmux` with prompt-aware operators
- Hardened Kali sandbox on an isolated ops network
- **102/104 (98.08%)** on XBOW validation benchmarks

→ [Website](https://decepticon.red) · [Docs](https://docs.decepticon.red) · [App](https://app.decepticon.red)

---

## Featured Projects

### Reverse Engineering & Low-Level

| Project | Description |
| --------- | ------------- |
| [**Kevlar**](https://github.com/NetVar1337/Kevlar) | x64 Windows kernel-driver emulation & behavior analysis on Unicorn Engine |
| [**unleash**](https://github.com/NetVar1337/unleash) | Bun SEA bytecode patcher — 113 patches, zero refuse/telemetry, interactive TUI |
| [**decepticon-ghidra-mcp**](https://github.com/NetVar1337/decepticon-ghidra-mcp) | Full-featured Ghidra MCP for agentic binary analysis & 0-day workflows |
| [**AiDA-Fork**](https://github.com/NetVar1337/AiDA-Fork) | AI assistant for IDA 9.0+ aimed at C++ game RE |
| [**codex-patcher-cc**](https://github.com/NetVar1337/codex-patcher-cc) | Codex CLI Mach-O patcher + wrapper/installer |

### Game Hacking & Research Tooling

| Project | Description |
| --------- | ------------- |
| [**unknowncheats-mcp**](https://github.com/NetVar1337/unknowncheats-mcp) | MCP server for UC / Elitepvpers with Cloudflare bypass |
| [**dma-ai-toolkit**](https://github.com/NetVar1337/dma-ai-toolkit) | AI-assisted PCILeech / DMA research toolkit |
| [**PCILeechGen**](https://github.com/NetVar1337/PCILeechGen) | PCILeech firmware generator |
| [**pcileech-fpga**](https://github.com/NetVar1337/pcileech-fpga) | FPGA modules for PCILeech DMA |

### Developer Tools & AI Infrastructure

| Project | Description |
| --------- | ------------- |
| [**vibe-island**](https://github.com/NetVar1337/vibe-island) | Dynamic Island for AI coding tools — macOS / Windows / Linux |
| [**omniwire**](https://github.com/NetVar1337/omniwire) | Agent-swarm infrastructure — MCP, A2A, mesh VPN, CDP, 2FA |
| [**mcp-ctl**](https://github.com/NetVar1337/mcp-ctl) | Zero-intervention MCP lifecycle manager (Zig) |
| [**claude-for-firefox**](https://github.com/NetVar1337/claude-for-firefox) | Claude browser extension port for Firefox |

### Embedded / Hardware

| Project | Description |
| --------- | ------------- |
| [**flipctld**](https://github.com/NetVar1337/flipctld) | FlipCTL menu-UI core for Flipper One (C) |
| [**flipper-profile**](https://github.com/NetVar1337/flipper-profile) | btrfs + overlayfs OS profile manager |
| [**linux-rk3576-rocket**](https://github.com/NetVar1337/linux-rk3576-rocket) | Mainline rocket NPU driver patches for RK3576 |
| [**flipperone-mcu-firmware**](https://github.com/NetVar1337/flipperone-mcu-firmware) | RP2350 co-processor firmware sources |

---

## Stack

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Zig](https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**RE / Offense:** IDA Pro · Ghidra · x64dbg · WinDbg · HyperDbg · PCILeech · Unicorn · Frida · Volatility · Burp · Metasploit

**AI / Agents:** Claude Code · Codex · MCP · A2A · agent swarms · binary patching / tooling unlock research

---

## GitHub Analytics

<div align="center">

<a href="https://github.com/NetVar1337">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=NetVar1337&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=NetVar1337&layout=compact&theme=github_dark&hide_border=true" />
</a>

</div>

<br>

<div align="center">

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=NetVar1337&theme=github-dark-blue&hide_border=true&date_format=M%20j%5B%2C%20Y%5D)](https://git.io/streak-stats)

</div>

---

## Current Focus

- Kernel-level tooling — driver emulation, manual mapping, hypervisor research
- Game / anti-cheat reverse engineering and research frameworks
- DMA / PCILeech / FPGA attack-surface expansion
- Autonomous red teaming with Decepticon @ PurpleAILAB
- High-signal developer tools around AI coding agents

**Open to collaboration** on reverse engineering, exploit research, game-security, and offensive AI systems.

---

<div align="center">

```
   ┌───────────────────────────────────────────────────────┐
   │  if you understand the machine, you become the machine │
   └───────────────────────────────────────────────────────┘
```

**Stay sharp. Stay low-level. — NetVar1337**

[![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=NetVar1337.NetVar1337)](https://github.com/NetVar1337)
[![X](https://img.shields.io/badge/X-NetVar1337-000000?style=flat&logo=x&logoColor=white)](https://x.com/CyberNordicNO)

</div>
