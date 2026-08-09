<div align="center">

# ⚡ NetVar1337

### Offensive Security Researcher · Windows Internals · Game Hacking

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=24&duration=2800&pause=700&color=8B5CF6&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=80&lines=Game+Hacking+%7C+Pentesting+%7C+0-day+Discovery;Reverse+Engineering+%7C+Windows+Internals;AI+Offensive+Security+%7C+Autonomous+Red+Teaming)](https://git.io/typing-svg)

<br>

[![X / Twitter](https://img.shields.io/badge/%2FX-NetVar1337-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/CyberNordicNO)
[![GitHub](https://img.shields.io/badge/GitHub-NetVar1337-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NetVar1337)
[![PurpleAILAB](https://img.shields.io/badge/PurpleAILAB-Co--Owner-8B5CF6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PurpleAILAB)
[![Discord](https://img.shields.io/badge/Discord-%40netvar-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/netvar)

</div>

---

## 🧬 Who Am I

I'm a **security researcher** who lives at the bottom of the stack. My day-to-day is spent tearing apart binaries, walking Windows kernel internals, and turning AI into a weapon for offensive security.

> *"If you understand how the machine thinks, you control the machine."*

I work across the full offensive spectrum — reading game memory at ring-3, emulating kernel drivers at ring-0, and building **AI-native autonomous red-teaming** at the agent-orchestration layer. I'm the **co-owner of [PurpleAILAB](https://github.com/PurpleAILAB)** and its flagship autonomous red-team agent.

---

## 🎯 Specialties

| Domain | Focus |
|--------|-------|
| 🎮 **Game Hacking** | Memory manipulation, internal/external cheats, anti-cheat bypass (EAC, Vanguard, BattlEye), hooking, PCX Enma/AngelScript automation |
| 🛡️ **Penetration Testing** | Red team operations, web/mobile/network exploitation, autonomous kill chains |
| 🧨 **0-Day Discovery** | Vulnerability research, fuzzing, exploit development, variant analysis, patch diffing |
| 🔬 **Reverse Engineering** | IDA Pro / Ghidra, binary instrumentation, unpacking (Themida/VMProtect), protocol & malware analysis |
| 🪟 **Windows Internals** | Kernel drivers, manual mapping, injection, hypervisors/EPT/VMCS, DMA attacks (PCILeech/FPGA), BYOVD |
| 🤖 **AI / Autonomous Offense** | Offensive LLM agents, autonomous red teaming, agent swarms, MCP tooling, LLM security |

---

## 🏆 Flagship — [Decepticon](https://github.com/PurpleAILAB/Decepticon)

<div align="center">

*"Another AI hacker? Let us guess — it runs nmap and writes a report."*

[![Stars](https://img.shields.io/github/stars/PurpleAILAB/Decepticon?style=for-the-badge&label=Stars&color=yellow)](https://github.com/PurpleAILAB/Decepticon/stargazers)
[![Forks](https://img.shields.io/github/forks/PurpleAILAB/Decepticon?style=for-the-badge&label=Forks&color=blue)](https://github.com/PurpleAILAB/Decepticon/forks)
[![License](https://img.shields.io/github/license/PurpleAILAB/Decepticon?style=for-the-badge&color=blue)](https://github.com/PurpleAILAB/Decepticon/blob/main/LICENSE)

</div>

**Decepticon** is a professional **autonomous Red Team agent** — and I'm a **co-owner** of the project. Unlike the "AI hacker" demos that run `nmap` and print a report, Decepticon executes **real attack chains** — reconnaissance, exploitation, privilege escalation, lateral movement, and C2 — the way a real adversary would.

It operates under the discipline that separates red teamers from script kiddies: before a single packet leaves the wire it generates a complete engagement package — **RoE, ConOps, Deconfliction Plan, and OPPLAN** with MITRE ATT&CK mapping — and every action runs inside those rules.

**Key capabilities:**
- 🧵 **Real kill chains** — reads an OPPLAN and pursues objectives through whatever path opens up, pivoting and chaining techniques
- 💻 **Interactive shells, actually** — runs every command inside persistent `tmux` sessions with automatic prompt detection (msfconsole, sliver-client, evil-winrm)
- 🏝️ **Hardened sandbox isolation** — all commands run in an isolated Kali sandbox on a dedicated operational network
- 📊 **State-of-the-art benchmarks** — **102/104 (98.08%)** pass rate on XBOW validation-benchmarks

<!--
  Replace with dynamic badges if you want:
  [![Decepticon](https://github-readme-stats.vercel.app/api/pin/?username=PurpleAILAB&repo=Decepticon&theme=github_dark&hide_border=true)](https://github.com/PurpleAILAB/Decepticon)
-->

→ [Website](https://decepticon.red) · [Docs](https://docs.decepticon.red) · [Live App](https://app.decepticon.red)

---

## 🔥 Featured Projects

### AI & Autonomous Offense

| Project | Description | Stars |
|---------|-------------|-------|
| [**Decepticon**](https://github.com/PurpleAILAB/Decepticon) | Autonomous Red Team agent — real kill chains, RoE/OPPLAN discipline, 98% XBOW pass rate *(co-owner)* | ![5k](https://img.shields.io/badge/5k-8B5CF6?style=flat&logo=github) |
| [**Vigilo**](https://github.com/PurpleAILAB/Vigilo) | AI hacker for Web3 smart contracts — bug bounties, audit contests, real-world exploit thinking | ![60](https://img.shields.io/badge/60-8B5CF6?style=flat&logo=github) |
| [**omniwire**](https://github.com/NetVar1337/omniwire) | Infrastructure layer for AI agent swarms — 88 MCP tools, A2A, OmniMesh VPN, CDP browser, 2FA | ![16](https://img.shields.io/badge/16-181717?style=flat&logo=github) |
| [**free-code**](https://github.com/NetVar1337/free-code) | Free build of Claude Code — telemetry removed, guardrails stripped, all experimental features | — |

### Low-Level / Offensive Security

| Project | Description | Stars |
|---------|-------------|-------|
| [**unleash**](https://github.com/NetVar1337/unleash) | Unleash Claude Code — 113 patches, zero refuse/telemetry, 42 gates. Bun SEA bytecode patcher + TUI + 11-strategy signature scanner | ![61](https://img.shields.io/badge/61-181717?style=flat&logo=github) |
| [**Kevlar**](https://github.com/NetVar1337/Kevlar) | x64 Windows kernel-driver emulation & behavior-analysis harness powered by Unicorn Engine | ![2](https://img.shields.io/badge/2-181717?style=flat&logo=github) |
| [**vibe-island**](https://github.com/NetVar1337/vibe-island) | A Dynamic Island for AI coding tools — macOS, Windows, Linux (Hyprland/Sway/GNOME/KDE) | ![68](https://img.shields.io/badge/68-181717?style=flat&logo=github) |
| [**AiDA-Fork**](https://github.com/NetVar1337/AiDA-Fork) | AI-powered assistant for IDA 9.0+ to accelerate reverse engineering of C++ games | ![1](https://img.shields.io/badge/1-181717?style=flat&logo=github) |
| [**VoidChecksum**](https://github.com/NetVar1337/VoidChecksum) | Security research — RE, pentesting, exploit research, security audits | ![5](https://img.shields.io/badge/5-181717?style=flat&logo=github) |
| [**unknowncheats-mcp**](https://github.com/NetVar1337/unknowncheats-mcp) | MCP server for UnknownCheats & Elitepvpers with automatic Cloudflare bypass | ![4](https://img.shields.io/badge/4-181717?style=flat&logo=github) |
| [**PCILeechGen**](https://github.com/NetVar1337/PCILeechGen) | Firmware generator tool for PCILeech DMA attacks | ![1](https://img.shields.io/badge/1-181717?style=flat&logo=github) |
| [**pcileech-fpga**](https://github.com/NetVar1337/pcileech-fpga) | FPGA modules for PCILeech Direct Memory Access (DMA) attack software | ![1](https://img.shields.io/badge/1-181717?style=flat&logo=github) |

### Reverse Engineering Tooling

| Project | Description |
|---------|-------------|
| [**pcx-ai-toolkit**](https://github.com/NetVar1337/pcx-ai-toolkit) | Source-grounded AI toolkit for Perception.cx Enma & AngelScript — verified docs, API oracle, MCP tools, LSP packages |
| [**enma-lsp-pcx**](https://github.com/NetVar1337/enma-lsp-pcx) | Zero-setup VS Code LSP for Perception.cx Enma (.em) — IntelliSense, type checking, bundler & DAP debugger |
| [**codex-patcher-cc**](https://github.com/NetVar1337/codex-patcher-cc) | CodexCLI patcher — Rust Mach-O patches + wrapper + config installer |
| [**coursera-mcp-rs**](https://github.com/NetVar1337/coursera-mcp-rs) | Coursera MCP server in Rust — 4.9MB binary, 134 tools, async tokio, zero-copy I/O |

### Hardware & Firmware

| Project | Description |
|---------|-------------|
| [**flipperone-mcu-firmware**](https://github.com/NetVar1337/flipperone-mcu-firmware) | Flipper One MCU firmware sources (RP2350 low-power co-processor) |
| [**flipper-profile**](https://github.com/NetVar1337/flipper-profile) | btrfs+overlayfs OS snapshot/profile manager for Flipper One |
| [**linux-rk3576-rocket**](https://github.com/NetVar1337/linux-rk3576-rocket) | RFC patch series — RK3576 support for mainline rocket NPU driver |

---

## 🛠️ Technology Arsenal

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-4B0082?style=for-the-badge&logo=verilog&logoColor=white)

**Offensive Stack:** IDA Pro · Ghidra · x64dbg · WinDbg · HyperDbg · PCILeech · Unicorn Engine · Frida · Volatility · Burp Suite · Metasploit · Cobalt Strike

**AI / Agent Stack:** Claude Code · OpenAI Codex · MCP (Model Context Protocol) · A2A · LangGraph · Agent Swarms · LiteLLM · Prompt Injection & Jailbreak Testing

---

## 📈 GitHub Analytics

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

## 🏆 Trophies

<div align="center">

[![trophy](https://github-profile-trophy.vercel.app/?username=NetVar1337&theme=onedark&no-frame=true&no-bg=true&row=1&column=7)](https://github.com/ryo-ma/github-profile-trophy)

</div>

---

## 🐍 Contribution Graph

<div align="center">

<!--
  Enable the contribution snake by adding the github-snake (Platane/snk) workflow
  to your NetVar1337/NetVar1337 repo, with output/ as the output directory.
-->
![github contribution snake svg](https://github.com/NetVar1337/NetVar1337/blob/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![github contribution snake svg](https://github.com/NetVar1337/NetVar1337/blob/output/github-contribution-grid-snake.svg#gh-light-mode-only)

</div>

---

## 🧭 Current Mission

- 🎮 Deep-diving anti-cheat internals & game engine reversing (Enma / AngelScript automation)
- 🪟 Building **kernel-level** tooling — driver emulation, manual mapping, hypervisor research
- 🧨 Hunting 0-days across security products & Windows internals
- 🤖 Advancing **autonomous red teaming** with Decepticon at PurpleAILAB
- 🧊 Expanding PCILeech / DMA / FPGA attack surface

**Always looking to collaborate** on offensive security research, exploit development, and AI-security projects.

---

<div align="center">

```
   ┌───────────────────────────────────────────────────────┐
   │  if you understand the machine, you become the machine │
   └───────────────────────────────────────────────────────┘
```

**⚡ Stay sharp. Stay low-level. — NetVar1337**

[![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=NetVar1337.NetVar1337)](https://github.com/NetVar1337)
[![X](https://img.shields.io/badge/X-NetVar1337-000000?style=flat&logo=x&logoColor=white)](https://x.com/CyberNordicNO)

</div>